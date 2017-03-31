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
				originalDismissAddAnotherPopup = window.dismissAddAnotherPopup,
				originalDismissAddRelatedObjectPopup = window.dismissAddRelatedObjectPopup,
				win,
				projectURL = location.pathname.split('/')[1];

			window.dismissAddRelatedObjectPopup = function(win, link_id) {
				var selected = e.getSelection();
				e.replaceSelection('[link:' + link_id + ']');
				e.setSelection(selected.start, selected.start);

				win.close();

				window.dismissAddAnotherPopup = originalDismissRelatedLookupPopup;
				window.dismissAddRelatedObjectPopup = originalDismissAddRelatedObjectPopup;
			};

			if (projectURL == 'admin') {
				var projectNAME = '';
			} else {
				var projectNAME = '/' + projectURL;
			}

			window.dismissAddAnotherPopup = window.dismissAddRelatedObjectPopup;
			win = window.open(
				projectNAME + '/admin/anylink/anylink/add/?_popup=1',
				'Link',
				'width=800,height=600,resizable=yes,scrollbars=yes'
			);

			win.focus();
			return false;
		}
	};
})(window.jQuery || window.django.jQuery);
