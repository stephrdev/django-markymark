(function($) {
	var
		group = $.fn.markdown.defaults.buttons[0].filter(function(group) {
			return group.name == 'groupLink';
		})[0],
		buttonIndex = group.data.findIndex(function(button) {
			return button.name == 'cmdUrl';
		})
	;

	group.data[buttonIndex] = {
		name: 'cmdAnylinkLink',
		title: 'Link',
		hotkey: 'Ctrl+L',
		icon: {
			fa: 'fas fa-link',
			fa4: 'fa fa-link'
		},
		callback: function(e) {
			var
				self = this,
				originalDismissAddRelatedObjectPopup = window.dismissAddRelatedObjectPopup,
				baseUrl = window.location.pathname.substring(0, window.location.pathname.indexOf('/admin/'))
			;

			window.dismissAddRelatedObjectPopup = function(popup, link_id) {
				var selected = e.getSelection();
				e.replaceSelection('[link:' + link_id + ']');
				e.setSelection(selected.start, selected.start);

				popup.close();

				window.dismissAddRelatedObjectPopup = originalDismissAddRelatedObjectPopup;
			};

			window.open(
				baseUrl + '/admin/anylink/anylink/add/?_popup=1',
				'Anylink',
				'width=800,height=600,resizable=yes,scrollbars=yes'
			).focus();
			return false;
		}
	};
})(window.jQuery || window.django.jQuery);
