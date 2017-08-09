#!/usr/bin/env python
"""transtats command line tool"""
from setuptools import setup


setup(
    name='transtats-cli',
    version='0.1.0',
    description="Command line tool for transtats",
    long_description="Command line tool for Transtats server",
    platforms=["Linux"],
    py_modules=['transtats'],
    author="Sundeep Anand",
    author_email="suanand@redhat.com",
    url="https://transtats.org",
    license="Apache License 2.0",
    install_requires=[
        'Click', 'requests'
    ],
    entry_points='''
        [console_scripts]
        transtats=cli:entry_point
    ''',
)
