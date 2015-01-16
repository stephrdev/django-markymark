from django.utils.safestring import SafeText

from markymark.templatetags.markup import markdown_filter


class TestMarkdownFilter:
    teststring = (
        'Test 123\n'
        '<strong>Test</strong>\n'
        '*foo*'
    )

    def test_without_safe_extension(self):
        expected = markdown_filter(self.teststring)
        assert expected == (
            '<p>Test 123\n'
            '<strong>Test</strong>\n'
            '<em>foo</em></p>'
        )
        assert type(expected) is SafeText

    def test_without_safe_extension_and_other(self):
        expected = markdown_filter(self.teststring, 'nl2br')
        assert expected == (
            '<p>Test 123<br />\n'
            '<strong>Test</strong><br />\n'
            '<em>foo</em></p>'
        )
        assert type(expected) is SafeText
