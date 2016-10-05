import os
import sys
import codecs
from setuptools import setup, find_packages


version = '0.9.3'


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    print('You probably want to also tag the version now:')
    print('  git tag -a %s -m "version %s"' % (version, version))
    print('  git push --tags')
    sys.exit()


def read(*parts):
    filename = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(filename, encoding='utf-8') as fp:
        return fp.read()


install_requirements = [
    'django>=1.6,<1.9',
    'Markdown>=2.6,<2.7',
]

if sys.version_info < (2, 7):
    install_requirements = [
        'django<1.7',  # 1.6.x is last version to support py26
        'markdown-py26-support==2.6.2',
    ]


test_requirements = [
    'tox',
    'tox-pyenv',
    'pytest==2.8.0',
    'pytest-cache==1.0',
    'pytest-cov==2.1.0',
    'pytest-django==2.8.0',
    'pytest-flakes==1.0.1',
    'pytest-pep8==1.0.6',
    'cov-core==1.15.0',
    'mock==1.3.0',
    'factory-boy==2.5.2',
    'django-filer<1.3.0',
    'django-anylink',
]


setup(
    name='django-markymark',
    version=version,
    description=(
        'django-markymark provides helpers and tools to integrate markdown '
        'into your editor.'),
    long_description=read('README.rst'),
    author='Moccu GmbH & Co. KG',
    author_email='info@moccu.com',
    url='https://github.com/moccu/django-markymark/',
    packages=find_packages(exclude=[
        'testing',
        'testing.pytests',
        'examples',
        'examples.example',
        'examples.example.app',
    ]),
    install_requires=install_requirements,
    extras_require={
        'tests': test_requirements,
        'filer': ['django-filer>=1.2.0,<1.3.0', ],
        'anylink': ['django-anylink', ],
    },
    include_package_data=True,
    license='Apache License (2.0)',
    keywords=['markdown', 'django'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Framework :: Django',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    zip_safe=False,
)
