from markymark.widgets import MarkdownTextarea


class TestMarkdownTextarea:
    def test_attrs(self):
        rendered = MarkdownTextarea().render('testfield', '')
        assert '<textarea' in rendered
        assert 'data-provide="markdown"' in rendered
        assert 'data-iconlibrary' not in rendered

    def test_attrs_iconlibrary(self, settings):
        settings.MARKYMARK_ICONLIBRARY = 'fa5'

        rendered = MarkdownTextarea().render('testfield', '')
        assert 'data-iconlibrary="fa5"' in rendered

    def test_media(self):
        widget = MarkdownTextarea()
        assert 'markymark/js/markdown-editor.js' in widget.media._js
        assert 'markymark/extensions/clean.js' in widget.media._js
        assert 'markymark/extensions/anylink.js' in widget.media._js
        assert 'markymark/css/markdown-editor.css' in widget.media._css['all']
