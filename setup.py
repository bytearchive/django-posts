import os
from setuptools import setup, find_packages

import posts


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-posts',
    version=posts.__version__,
    description='A generic posts app for django',
    long_description=read('README.md'),
    license='MIT License',
    author='Richard Stromer',
    author_email='richard.stromer@byteweaver.org',
    url='https://github.com/byteweaver/django-posts',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django',
    ],
)
