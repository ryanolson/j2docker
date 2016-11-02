#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'PyYAML>=3.12',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='j2docker',
    version='0.1.0',
    description="Basiccc templating for Dockerfiles",
    long_description=readme + '\n\n' + history,
    author="Ryan Olson",
    author_email='rmolson@gmail.com',
    url='https://github.com/ryanolson/j2docker',
    packages=[
        'j2docker',
    ],
    package_dir={'j2docker':
                 'j2docker'},
    entry_points={
        'console_scripts': [
            'j2docker=j2docker.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='j2docker',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
