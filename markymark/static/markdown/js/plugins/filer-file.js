(function($) {
	var
		buttons = $.fn.markdown.defaults.buttons,
		groupLink,
		cmdImageIndex,
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
			var self = this,
				oldDissmissFn = window.dismissRelatedImageLookupPopup;

			window.dismissRelatedImageLookupPopup = function(popup, id, thumbnail) {
				popup.close();

				window.dismissRelatedImageLookupPopup = oldDissmissFn;

				self.$image
					.data('id', id)
					.css('background-image', 'url("' + thumbnail + '")')
					.addClass('has-image');
			};

			window.open('/admin/filer/folder/?_popup=1&_pick=file', 'Filer', 'width=800,height=600');
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
						this.editor.replaceSelection('[file:' + id + ']');
						this.close();
					}

					break;
			}
		}
	};

	for (var section in buttons) {
		for (var i in buttons[section]) {
			if (buttons[section][i].name === 'groupLink') {
				groupLink = buttons[section][i];
				for (var x in groupLink.data) {
					if (groupLink.data[x].name === 'cmdImage') {
						cmdImageIndex = x;
						break;
					}
				}
			}
		}
	}

	groupLink.data[cmdImageIndex] = {
		name: 'cmdFilerFile',
		title: 'Image/Video',
		hotkey: 'Ctrl+G',
		icon: {
			glyph: 'glyphicon glyphicon-picture',
			fa: 'fa fa-picture-o'
		},
		callback: function(e) {
			new FilerFileDialog(e);
		}
	};
})(window.jQuery || window.django.jQuery);
