import re

import pytest
from filer.models.filemodels import File

from markymark.templatetags.markup import markdown_filter

from markymark.tests.factories.files import FileFactory


@pytest.mark.django_db
class TestFilerFileExtension:
    def setup(self):
        self.file = FileFactory.create()

    def test_invalid_tag(self):
        assert markdown_filter('foo [image:123] bar') == ('<p>foo [image:123] bar</p>')

    def test_image_not_found_debug(self, settings):
        settings.DEBUG = True

        with pytest.raises(File.DoesNotExist):
            markdown_filter('[file:999]')

    def test_image_not_found_no_debug(self, settings):
        settings.DEBUG = False

        assert markdown_filter('foo [file:999] bar') == ('<p>foo  bar</p>')

    def test_render_success(self):
        rendered = '<p><a href="{0}">{0}</a></p>'.format(self.file.url)
        assert re.match(
            rendered, markdown_filter('[file:{0}]'.format(self.file.pk)))
