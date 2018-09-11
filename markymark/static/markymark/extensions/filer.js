(function($) {
	var
		group = $.fn.markdown.defaults.buttons[0].filter(function(group) {
			return group.name == 'groupLink';
		})[0],
		buttonIndex = group.data.findIndex(function(button) {
			return button.name == 'cmdImage';
		})
		FilerFileDialog = function() {
			this.initialize.apply(this, arguments);
		}
	;

	FilerFileDialog.prototype = {
		initialize: function(editor) {
			this.editor = editor;
			this.render();
			this.bindEvents();
		},

		render: function() {
			this.$overlay	= $('<div />');
			this.$container = $('<div />');
			this.$header 	= $('<h2>Image/Video</h2>');
			this.$image 	= $('<div>Choose image or video.</div>');
			this.$close		= $('<a href="#">X</a>');
			this.$submit	= $('<button>Insert</button>');

			this.$header.append(this.$close);

			this.$overlay.addClass('filer-file-overlay');
			this.$container.addClass('filer-file-container');
			this.$header.addClass('filer-file-header');
			this.$image.addClass('filer-file-image');
			this.$close.addClass('filer-file-close');
			this.$submit.addClass('filer-file-submit');

			this.$overlay.append(this.$container);
			this.$container.append(this.$header);
			this.$container.append(this.$image);
			this.$container.append(this.$submit);
			$('body').append(this.$overlay);
		},

		bindEvents: function() {
			var self = this;

			self.$overlay.on('click', function() {
				self.onClick.apply(self, arguments);
			});
		},

		unbindEvents: function() {
			this.$overlay.off('click');
		},

		close: function() {
			this.unbindEvents();
			this.$overlay.remove();
		},

		openFilerPopup: function() {
			var
				self = this,
				originalDismissAddRelatedObjectPopup = window.dismissAddRelatedObjectPopup,
				baseUrl = window.location.pathname.substring(0, window.location.pathname.indexOf('/admin/'))
			;

			window.dismissRelatedImageLookupPopup = function(popup, id, thumbnail) {
				popup.close();

				window.dismissRelatedImageLookupPopup = originalDismissAddRelatedObjectPopup;

				self.$image
					.data('id', id)
					.css('background-image', 'url("' + thumbnail + '")')
					.addClass('has-image');
			};

			window.open(
				baseUrl + '/admin/filer/folder/?_popup=1&_pick=file',
				'Filer',
				'width=800,height=600,resizable=yes,scrollbars=yes'
			).focus();
			return false;
		},

		onClick: function(e) {
			var $target = $(e.target);

			e.preventDefault();

			switch (true) {
				case $target.hasClass('filer-file-overlay'):
				case $target.hasClass('filer-file-close'):
					this.close();

					break;
				case $target.hasClass('filer-file-image'):
					this.openFilerPopup();

					break;
				case $target.hasClass('filer-file-submit'):
					var id = this.$image.data('id');

					if (id) {
						var selected = this.editor.getSelection();
						this.editor.replaceSelection('[file:' + id + ']');
						this.editor.setSelection(selected.start, selected.start);
						this.close();
					}

					break;
			}
		}
	};

	group.data[buttonIndex] = {
		name: 'cmdFilerFile',
		title: 'Image/Video',
		hotkey: 'Ctrl+G',
		icon: {
			fa: 'fas fa-image',
			fa4: 'fa fa-image'
		},
		callback: function(e) {
			new FilerFileDialog(e);
		}
	};
})(window.jQuery || window.django.jQuery);
