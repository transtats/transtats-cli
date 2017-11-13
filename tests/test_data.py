# Copyright 2017 Red Hat, Inc.
# All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from mock import Mock


def mock_server_version():
    """
    server_version mock value
    """
    mock_rep = Mock()
    mock_rep.ok = True
    mock_rep.json.return_value = {
        "server": "Transtats 0.1.3"
    }
    return mock_rep


def mock_package_status():
    """
    package_status mock value
    """
    mock_rep = Mock()
    mock_rep.ok = True
    mock_rep.json.return_value = {
        "systemd": {
            "translation_stats": {
                "Upstream": {
                    "French": 100,
                    "Japanese": 0.0,
                    "Spanish": 100,
                    "Russian": 100,
                    "German": 100
                }
            },
            "percentage_calculated_on": "Messages"
        }
    }
    return mock_rep


def mock_rule_coverage():
    """
    rule_coverage mock value
    """
    mock_rep = Mock()
    mock_rep.ok = True
    mock_rep.json.return_value = {
        "coverage": {
            "branch": "Fedora 27",
            "translation_stats": {
                "Chinese (Simplified)": {
                    "python-meh": 100.0,
                    "anaconda": 98.92,
                    "pykickstart": 100.0,
                    "blivet": 100.0
                },
                "German": {
                    "python-meh": 100.0,
                    "anaconda": 99.25,
                    "pykickstart": 93.71,
                    "blivet": 100.0
                }
            },
            "graph_rule": "rhinstaller"
        }
    }
    return mock_rep


def mock_release_status():
    """
    release_status mock value
    """
    mock_rep = Mock()
    mock_rep.ok = True
    mock_rep.json.return_value = {
        "fedora-27": {
            "anaconda": {
                "Total": 12080,
                "Translated": 11191,
                "Untranslated": 876,
                "Remaining": 7.25
            },
            "abrt": {
                "Total": 4760,
                "Translated": 4495,
                "Untranslated": 262,
                "Remaining": 5.5
            },
            "Calculated on": "Messages"
        }
    }
    return mock_rep


def mock_release_workload_detail():
    """
    release_workload_detail mock value
    """
    mock_rep = Mock()
    mock_rep.ok = True
    mock_rep.json.return_value = {
        "German": {
            "anaconda": {
                "Total": 1208,
                "Translated": 1199,
                "Untranslated": 9,
                "Remaining": 0.75
            },
            "abrt": {
                "Total": 476,
                "Translated": 476,
                "Untranslated": 0,
                "Remaining": 0.0
            },
            "Calculated on": "Messages"
        },
        "Japanese": {
            "abrt": {
                "Total": 476,
                "Translated": 390,
                "Untranslated": 86,
                "Remaining": 18.07
            },
            "python-meh": {
                "Total": 23,
                "Translated": 20,
                "Untranslated": 3,
                "Remaining": 13.04
            },
            "Calculated on": "Messages"
        },
        "Release": "fedora-27",
    }
    return mock_rep
