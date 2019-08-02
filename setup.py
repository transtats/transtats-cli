#!/usr/bin/env python
"""transtats command line interface"""

import os
from setuptools import setup, find_packages
from tscli import APP_VERSION


with open(
        os.path.join(os.path.dirname(__file__), "requirements.txt"), 'rb'
) as require:
    REQUIRE = require.read().decode('utf-8').splitlines() + ['setuptools']


setup(
    name='transtats-cli',
    version=APP_VERSION,
    description="Command line interface for transtats",
    platforms=["Linux"],
    packages=find_packages(),
    author="Sundeep Anand",
    author_email="suanand@fedoraproject.org",
    url="http://transtats.org",
    license="Apache License 2.0",
    install_requires=REQUIRE,
    setup_requires=["flake8"],
    test_suite="tests.tscli_test_suit",
    scripts=["transtats"],
    data_files=[('/usr/share/man/man1', ['docs/man/transtats.1']),
                ('/usr/share/bash-completion/completions',
                 ['conf/bash-completion/transtats.bash'])],
    # entry_points='''
    #     [console_scripts]
    #     transtats=tscli:entry_point
    # ''',
    classifiers=[
        'License :: OSI Approved :: Apache License 2.0 (Apache-2.0)',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
