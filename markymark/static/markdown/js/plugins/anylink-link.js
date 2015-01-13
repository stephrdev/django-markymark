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

	groupPlugins.data.push({
		name: 'cmdAnylinkLink',
		title: 'Link',
		hotkey: 'Ctrl+L',
		icon: {
			glyph: 'glyphicon glyphicon-link',
			fa: 'fa fa-link-o'
		},
		callback: function(e) {
			var self = this,
				oldDissmissFn = window.dismissRelatedImageLookupPopup;

			window.dismissRelatedLookupPopup = function(popup, id) {
				popup.close();

				window.dismissRelatedImageLookupPopup = oldDissmissFn;

				if (id) {
					e.replaceSelection('[link:' + id + ']');
				}
			};

			window.open('/admin/anylink/anylink/?_popup=1', 'Link', 'width=800,height=600');
		}
	});
})(window.jQuery || window.django.jQuery);
