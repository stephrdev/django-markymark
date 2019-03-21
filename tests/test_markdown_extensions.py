import django
import pytest
from anylink.models import AnyLink

from markymark.templatetags.markymark import markdown_filter
from markymark.widgets import MarkdownTextarea


@pytest.mark.skipif(django.VERSION[0] >= 2, reason='Requires Django<2')
@pytest.mark.django_db
class TestFilerFileExtension:

    def setup(self):
        from .factories.files import FileFactory, ImageFactory

        self.file = FileFactory.create()
        self.image = ImageFactory.create()

    def test_invalid_tag(self):
        assert markdown_filter('foo [file:123 bar') == ('<p>foo [file:123 bar</p>')

    def test_file_not_found_debug(self, settings):
        from filer.models.filemodels import File
        settings.DEBUG = True

        with pytest.raises(File.DoesNotExist):
            markdown_filter('[file:999]')

    def test_file_not_found_no_debug(self, settings):
        settings.DEBUG = False
        assert markdown_filter('foo [file:999] bar') == ('<p>foo  bar</p>')

    def test_file_render_success(self):
        expected = '<p><a href="{0}">{0}</a></p>'.format(self.file.url)
        assert expected == markdown_filter('[file:{0}]'.format(self.file.pk))

    def test_image_render_success(self):
        expected = '<p><img src="{0}" alt="{1}" title="{2}"></p>'.format(
            self.image.url, self.image.default_alt_text, self.image.default_caption)
        assert expected == markdown_filter('[file:{0}]'.format(self.image.pk))

    def test_media(self):
        widget = MarkdownTextarea()
        assert 'markymark/extensions/filer.css' in widget.media._css['all']
        assert 'markymark/extensions/filer.js' in widget.media._js


@pytest.mark.django_db
class TestAnylinkExtension:

    def setup(self):
        self.link = AnyLink.objects.create(link_type='external_url', external_url='/test/')

    def test_invalid_tag(self):
        assert markdown_filter('foo [link:123 bar') == ('<p>foo [link:123 bar</p>')

    def test_link_not_found_debug(self, settings):
        settings.DEBUG = True
        with pytest.raises(AnyLink.DoesNotExist):
            markdown_filter('[link:999]')

    def test_link_not_found_no_debug(self, settings):
        settings.DEBUG = False
        markdown_filter('[link:999]') == '<p></p>'

    def test_file_render_success(self):
        expected = '<p><a href="{0}" title="" target="_self"></a></p>'.format(
            self.link.external_url)
        assert expected == markdown_filter('[link:{0}]'.format(self.link.pk))

    def test_file_render_target_success(self):
        self.link.target = '_blank'
        self.link.save()
        expected = (
            '<p><a href="{0}" title="" target="_blank" '
            'rel="noreferrer noopener"></a></p>'
        ).format(self.link.external_url)
        assert expected == markdown_filter('[link:{0}]'.format(self.link.pk))


class TestAutoLinkExtension:

    def test_valid_http_link(self):
        url = 'https://www.youtube.com/watch?v=FTuFVwnrcts'
        expected = '<p><a href="{0}">{0}</a></p>'.format(url)
        assert expected == markdown_filter(url)

    def test_valid_mailto_link(self):
        url = 'mailto:test@example.com'
        expected = '<p><a href="{0}">test@example.com</a></p>'.format(url)
        assert expected == markdown_filter(url)

    def test_invalid_link(self):
        url = 'www.example.com'
        expected = '<p>{0}</p>'.format(url)
        assert expected == markdown_filter(url)

    def test_dont_render_link_twice_url(self):
        url = '<a href="http://www.example.com/">test</a>'
        expected = '<p>{0}</p>'.format(url)
        assert expected == markdown_filter(url)

    def test_dont_render_link_twice_name(self):
        url = '<a href="http://www.example.com/">http://www.example.com/</a>'
        expected = '<p>{0}</p>'.format(url)
        assert expected == markdown_filter(url)

    def test_dont_hijack_images(self):
        md = '![](https://mirrors.creativecommons.org/presskit/icons/cc.large.png)'
        expected = (
            '<p><img alt="" src="https://mirrors.creativecommons.org/presskit/'
            'icons/cc.large.png" /></p>'
        )
        assert markdown_filter(md) == expected
