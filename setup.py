import codecs
import os
from setuptools import setup, find_packages


install_requirements = [
    'django>=1.5',
    'markdown==2.5.2',
    'django-filer==0.9.8',
    'django-floppyforms==1.3.0',
    'django-anylink==0.1.0',
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
    'factory_boy==2.4.1'
]


doc_requirements = [
    'sphinx',
    'sphinx_rtd_theme',
]


def read(*parts):
    filename = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(filename, encoding='utf-8') as fp:
        return fp.read()


setup(
    name='django-markymark',
    version='0.1',
    description='',
    long_description=read('README.md'),
    author='Moccu GmbH & Co. KG',
    author_email='info@moccu.com',
    url='',
    packages=find_packages(),
    install_requires=install_requirements,
    extras_require={
        'docs': doc_requirements,
        'tests': test_requirements,
    },
    include_package_data=True,
    license='MIT',
    keywords='django static html',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
