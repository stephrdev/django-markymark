Changelog
=========

3.0.0 (2022-09-12)
------------------

* Drop support for Django < 3.2, add support for 3.2
* Drop support for Python < 3.8


2.1.0 (2018-09-11)
------------------

* Add setting to switch icon library for markdown editor to FontAwesome 4


2.0.0 (2018-07-27)
------------------

* THIS IS A BREAKING RELEASE, if you need Django < 1.11 please stick to the 1.1.0 release.
* Drop Python < 3 support
* Drop Django < 1.11 support
* Cleanup code and add some more documentation


1.1.0 (2017-04-21)
------------------

* add table support including new button in editor


1.0.5 (2017-04-20)
------------------

* drop py26 support
* Fix anylink pop up, make it more flexible for custom project urls


1.0.4 (2017-02-21)
------------------

* Fix styling when using markymark in inlines with django-cms / djangocms-admin-style
* Force Pillow version for py26


1.0.0 (2016-11-24)
------------------

* Add support for Django 1.9
* Fix styling when using markymark with django-cms / djangocms-admin-style
* Improve autolink extension to prevent double-linking
* Javascript bugfixes


0.9.3 (2016-10-05)
------------------

* fix issue - `MarkdownField should handle widget instances as well #7 <https://github.com/stephrdev/django-markymark/issues/7>`_
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
