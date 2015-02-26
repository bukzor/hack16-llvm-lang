#!/usr/bin/env python

from __future__ import unicode_literals
from setuptools import find_packages
from setuptools import setup


def main():
    setup(
        name='mylang',
        version='0.0.0dev0',
        description="hackathon16: a silly llvm compiler",
        long_description=None,
        url='https://github.com/bukzor/hack16-llvm-lang',
        author='Buck Evan',
        author_email='buck@yelp.com',
        platforms='all',
        license='MIT',
        classifiers=[
            # TODO
        ],
        packages=find_packages('.', exclude=('tests*',)),
        install_requires=[
            # none, yet
        ],
        entry_points={
            'console_scripts': [
                # # 'venv-update = venv_update:main',
                # none, yet
            ],
        },
    )  # pragma: no cover: covered by tox

if __name__ == '__main__':
    exit(main())
