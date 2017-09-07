#!/usr/bin/env python
"""transtats command line tool"""
from setuptools import setup, find_packages


setup(
    name='transtats-cli',
    version='0.1.0',
    description="Command line tool for transtats",
    platforms=["Linux"],
    packages=find_packages(),
    author="Sundeep Anand",
    author_email="suanand@redhat.com",
    url="http://transtats.org",
    license="Apache License 2.0",
    install_requires=[
        'Click', 'requests'
    ],
    scripts=["transtats"],
    # entry_points='''
    #     [console_scripts]
    #     transtats=cli:entry_point
    # ''',
    classifiers=[
        'License :: OSI Approved :: Apache License 2.0 (Apache-2.0)',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
    ],
)
