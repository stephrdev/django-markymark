from django.utils.safestring import SafeText

from markymark.templatetags.markup import markdown_filter


class TestMarkdownFilter:
    teststring = (
        'Test 123\n'
        '<strong>Test</strong>\n'
        '*foo*'
    )

    def test_with_safe_extension(self):
        retval = markdown_filter(self.teststring, 'safe')
        assert retval == (
            '<p>Test 123\n'
            '[HTML_REMOVED]Test[HTML_REMOVED]\n'
            '<em>foo</em></p>'
        )
        assert type(retval) is SafeText

    def test_with_safe_extension_and_other(self):
        retval = markdown_filter(self.teststring, 'safe,nl2br')
        assert retval == (
            '<p>Test 123<br />\n'
            '[HTML_REMOVED]Test[HTML_REMOVED]<br />\n'
            '<em>foo</em></p>'
        )
        assert type(retval) is SafeText

    def test_without_safe_extension(self):
        retval = markdown_filter(self.teststring)
        assert retval == (
            '<p>Test 123\n'
            '<strong>Test</strong>\n'
            '<em>foo</em></p>'
        )
        assert type(retval) is SafeText

    def test_without_safe_extension_and_other(self):
        retval = markdown_filter(self.teststring, 'nl2br')
        assert retval == (
            '<p>Test 123<br />\n'
            '<strong>Test</strong><br />\n'
            '<em>foo</em></p>'
        )
        assert type(retval) is SafeText
