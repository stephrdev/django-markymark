from markymark.widgets import MarkdownTextarea


class TestMarkdownTextarea:

    def test_attrs(self):
        retval = MarkdownTextarea().render('testfield', '')
        assert '<textarea' in retval
        assert 'data-provide="markdown"' in retval

    def test_media(self):
        widget = MarkdownTextarea()
        assert 'markdown/js/markdown.js' in widget.media._js
        assert 'markdown/js/markdown-editor.js' in widget.media._js
        assert 'markdown/js/plugins/filer-image.js' in widget.media._js
        assert 'markdown/js/plugins/teaser-break.js' in widget.media._js
        assert 'markdown/css/markdown-editor.css' in widget.media._css['all']
        assert 'markdown/css/plugins/filer-image.css' in widget.media._css['all']
