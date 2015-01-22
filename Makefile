.PHONY: tests coverage coverage-html devinstall tox docs clean
APP=markymark
COV=markymark
OPTS=

help:
	@echo "tests - run all tests"
	@echo "coverage - run all tests with coverage enabled"
	@echo "coverage-html - run all tests with coverage html export enabled"
	@echo "devinstall - install all packages required for development"
	@echo "docs - generate Sphinx HTML documentation, including API docs"
	@echo "clean-build - Clean build related files"

tests:
	py.test ${OPTS} ${APP}

coverage:
	coverage run `which py.test` ${OPTS} ${APP}
	coverage report -m --include=${COV}* --omit='*/tests*'

coverage-html:
	coverage run `which py.test` ${OPTS} ${APP}
	coverage html -d htmlcov --include=${COV}* --omit='*/tests*'

devinstall:
	pip install -e .
	pip install -e .[tests]
	pip install -r requirements-docs.txt

docs: clean-build
	pip install -e .
	pip install -r requirements-docs.txt
	sphinx-apidoc --force -o docs/source/modules/ markymark markymark/settings.py markymark/tests/
	$(MAKE) -C docs clean
	$(MAKE) -C docs html

clean-build:
	@rm -fr build/
	@rm -fr dist/
	@rm -fr *.egg-info src/*.egg-info
	@rm -fr htmlcov/
	$(MAKE) -C docs clean
