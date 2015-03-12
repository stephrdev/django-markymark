(function($) {
	var
		buttons = $.fn.markdown.defaults.buttons,
		groupLink,
		cmdUrlIndex
	;

	for (var section in buttons) {
		for (var i in buttons[section]) {
			if (buttons[section][i].name === 'groupLink') {
				groupLink = buttons[section][i];
				for (var x in groupLink.data) {
					if (groupLink.data[x].name === 'cmdUrl') {
						cmdUrlIndex = x;
						break;
					}
				}
			}
		}
	}

	groupLink.data[cmdUrlIndex] = {
		name: 'cmdAnylinkLink',
		title: 'Link',
		hotkey: 'Ctrl+L',
		icon: {
			glyph: 'glyphicon glyphicon-link',
			fa: 'fa fa-link-o'
		},
		callback: function(e) {
			var self = this,
				originalAnyLinkCallback = window.AnyLinkAddOrChangeWidget.callback,
				params,
				win;

			params = '_popup=1&aoc=1';
			value = 'add';

			window.AnyLinkAddOrChangeWidget.callback = function(win, link_id, link_name) {
				win.close();

				window.AnyLinkAddOrChangeWidget.callback = originalAnyLinkCallback;

				e.replaceSelection('[link:' + link_id + ']');
			};

			win = window.open(
				'/admin/anylink/anylink/' + value + '/?' + params,
				'Link',
				'width=800,height=600,resizable=yes,scrollbars=yes'
			);

			win.focus();
			return false;
		}
	};
})(window.jQuery || window.django.jQuery);
