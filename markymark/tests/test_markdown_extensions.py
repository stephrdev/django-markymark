from anylink.models import AnyLink
import pytest
from filer.models.filemodels import File

from markymark.templatetags.markup import markdown_filter
from markymark.tests.factories.files import FileFactory, ImageFactory


@pytest.mark.django_db
class TestFilerFileExtension:

    def setup(self):
        self.file = FileFactory.create()
        self.image = ImageFactory.create()

    def test_invalid_tag(self):
        assert markdown_filter('foo [file:123 bar') == ('<p>foo [file:123 bar</p>')

    def test_file_not_found_debug(self, settings):
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
        expected = '<p><img src="{0}"/></p>'.format(self.image.url)
        assert expected == markdown_filter('[file:{0}]'.format(self.image.pk))


@pytest.mark.django_db
class TestLinkExtension:

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


class TestAutoLinkExtension:

    def test_valid_http_link(self):
        url = 'https://www.youtube.com/watch?v=FTuFVwnrcts'
        expected = '<p><a href="{0}">{0}</a></p>'.format(url)
        assert expected == markdown_filter(url)

    def test_valid_mailto_link(self):
        url = 'mailto://info@moccu.com'
        expected = '<p><a href="{0}">{0}</a></p>'.format(url)
        assert expected == markdown_filter(url)

    def test_invalid_link(self):
        url = 'www.moccu.com'
        expected = '<p>{0}</p>'.format(url)
        assert expected == markdown_filter(url)
