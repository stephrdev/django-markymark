Changelog
=========

1.0.0 (2016-11-24)
------------------

* Add support for Django 1.9
* Fix styling when using markymark with django-cms / djangocms-admin-style
* Improve autolink extension to prevent double-linking
* Javascript bugfixes


0.9.3 (2016-10-05)
------------------

* fix issue - `MarkdownField should handle widget instances as well #7 <https://github.com/moccu/django-markymark/issues/7>`_
* adjust install requirements to use 'official' python Markdown package
* some improvements


0.9.2 (2016-02-03)
------------------

* fix javascript - js was renamed from dismissAddAnotherPopup to dismissAddRelatedObjectPopup


0.9.1 (2015-09-24)
------------------

* fix MardownTextarea widget


0.9.0 (2015-09-24)
------------------

* add django 1.8 and python 3.5 support


0.8.3 (2015-07-08)
------------------

* fix - make "$" available in function only in markdown-editor.js


0.8.2 (2015-04-22)
------------------

* Add python 2.6 support
* Add support for south


0.8.1 (2015-03-16)
------------------

* Small style fix for preview button


0.8.0 (2015-03-12)
------------------

* Refactor JavaScript part of plugins to replace existing icons
* Fix bug in anylink js integration to avoid blank window after save


0.7.2 (2015-03-09)
------------------

* Fix anylink javascript to link to 'add' view


0.7.1 (2015-03-09)
------------------

* Remove padding from textarea


0.7 (2015-03-09)
----------------

* Fix release


0.6 (2015-03-09)
----------------

* Rework extensions to allow js/css files to be defined directly on each extension
* The return value of :func:`~markymark.utils.render_markdown` is now marked as safe
* Allow template-names to be overwritten
* Made settings easier to be overwritten, you can now
  import default settings from :mod:`markymark.defaults`
* Fixed contrib.anylink to avoid name clashes with other
  extensions named "link"
* Fix fullscreen icon integration


0.5 (2015-02-13)
----------------

* Removed anylink and filer extensions from being autoloaded.
* Removed dependency on floppyforms.


0.2..0.4 (2015-01-22)
---------------------

* General cleanups and bugfixes.


0.1 (2015-01-22)
----------------

* Initial release.
