(function (jQuery) {
	'use strict';

	$ = jQuery;

	function initMarkdown () {
		var $el = $(this);

		if ($el.data('markdown')) {
			$el.data('markdown').showEditor();
			return;
		}

		$el.markdown({
			hiddenButtons: ['cmdImage', 'cmdQuote', 'cmdUrl'],
			reorderButtonGroups: ['groupFont', 'groupMisc', 'groupUtil', 'groupPlugins'],
			resize: true,
			rows: 10,
		});
	};

	$(document).ready(function() {
		$('textarea[data-provide="init-markdown"]').each(initMarkdown);
	});

})(window.jQuery || window.django.jQuery);
