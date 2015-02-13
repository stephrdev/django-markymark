import os
import sys
import codecs
from setuptools import setup, find_packages


version = '0.5'


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
    'django>=1.6',
    'markdown==2.5.2'
]


test_requirements = [
    'py==1.4.26',
    'pyflakes==0.8.1',
    'pytest==2.6.4',
    'pytest-cache==1.0',
    'pytest-cov==1.7.0',
    'pytest-flakes==0.2',
    'pytest-pep8==1.0.6',
    'pytest-django==2.7.0',
    'cov-core==1.15.0',
    'coverage==3.7.1',
    'execnet==1.2.0',
    'pep8==1.5.7',
    'mock==1.0.1',
    'factory_boy==2.4.1',
    'django-filer==0.9.9',
    'django-anylink==0.1.0',
]


setup(
    name='django-markymark',
    version=version,
    description=(
        'django-markymark provides helpers and tools to integrate markdown '
        'into your editor.'),
    long_description=read('README.rst') + '\n\n' + read('CHANGELOG.rst'),
    author='Moccu GmbH & Co. KG',
    author_email='info@moccu.com',
    url='https://github.com/moccu/django-markymark/',
    packages=find_packages(exclude=[
        'markymark.tests',
        'examples',
        'examples.example',
        'examples.example.app',
    ]),
    install_requires=install_requirements,
    extras_require={
        'tests': test_requirements,
        'filer': ['django-filer==0.9.9', ],
        'anylink': ['django-anylink==0.1.0', ],
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
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    zip_safe=False,
)
