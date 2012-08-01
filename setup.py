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
    license='BSD',
    author='noxan',
    author_email='noxan@redmoonstudios.de',
    url='https://github.com/noxan/django-posts',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django',
    ],
    tests_require=[
        'django-nose',
        'coverage',
        'django-coverage',
    ],
)
