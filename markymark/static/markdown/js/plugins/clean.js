(function($) {
	var groups = $.fn.markdown.defaults.additionalButtons,
		groupPlugins;

	for (var i in groups) {
		if (groups[i].name === 'groupPlugins') {
			groupPlugins = groups[i];
			break;
		}
	}

	if (!groupPlugins) {
		groupPlugins = {
			name: 'groupPlugins',
			data: []
		};

		$.fn.markdown.defaults.additionalButtons.push(groupPlugins);
	}

	function cleanText (text) {
		var
			// \u2028, \u2029 are newlines defined by unicode spec, \u0085 is
			// used by some very old machines, better safe than sorry!
			lines = text.split(/[\n\u0085\u2028\u2029]|\r\n?/g),
			result = [],
			replacement
		;

		$.each(lines, function() {
			result.push(this.replace(/\s+$/, ''));
		});

		replacement = $.trim(result.join('\n'));

		// Replace too many newlines
		replacement = replacement.replace(/(\n\n)(\n+)?/g, '$1');

		return replacement;
	};

	groupPlugins.data.push({
		name: 'cmdClean',
		title: 'Clean',
		icon: {
			glyph: 'glyphicon glyphicon-bug',
		},
		callback: function(e) {
			// Replace selection with cleaned text.
			var
				cursor = e.getSelection(),
				replacement,
				newEnd
			;

			if (cursor.text) {
				// The user selected some text, clean only the selection
				replacement = cleanText(cursor.text);
				e.replaceSelection(replacement);
				newEnd = cursor.start + replacement.length;
				e.setSelection(newEnd, newEnd);
			} else {
				// Clean the whole text area
				replacement = cleanText(e.getContent());
				e.setContent(replacement);
			}
		}
	});
})(window.jQuery || window.django.jQuery);
