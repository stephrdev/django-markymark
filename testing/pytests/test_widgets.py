from markymark.widgets import MarkdownTextarea


class TestMarkdownTextarea:

    def test_attrs(self):
        rendered = MarkdownTextarea().render('testfield', '')
        assert '<textarea' in rendered
        assert 'data-provide="markdown"' in rendered

    def test_media(self):
        widget = MarkdownTextarea()
        assert 'markdown/js/markdown.js' in widget.media._js
        assert 'markdown/js/markdown-editor.js' in widget.media._js
        assert 'markdown/js/plugins/clean.js' in widget.media._js
        assert 'markdown/js/plugins/anylink-link.js' in widget.media._js
        assert 'markdown/js/plugins/filer-file.js' in widget.media._js
        assert 'markdown/css/markdown-editor.css' in widget.media._css['all']
        assert 'markdown/css/markdown-editor-adminfix.css' in widget.media._css['all']
        assert 'markdown/css/plugins/filer-file.css' in widget.media._css['all']
