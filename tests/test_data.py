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


def mock_package_status_exist():
    """
    package_status_exist mock value
    """
    mock_rep = Mock()
    mock_rep.ok = True
    mock_rep.json.return_value = {
        "gnome-shell": True
    }
    return mock_rep


def mock_package_status_health():
    """
    package_status_health mock value
    """
    mock_rep = Mock()
    mock_rep.ok = True
    mock_rep.json.return_value = {
        "abrt": {
            "fedora-30": {
                "Arabic": 2,
                "Basque": 3,
                "Esperanto": 7,
                "Friulian": 24,
                "Serbian": 14,
                "Turkish": 13,
                "Urdu": 3
            },
            "fedora-31": {
                "Friulian": 24
            }
        }
    }
    return mock_rep


def mock_package_status_health_in_sync():
    """
    package_status_health mock value
    """
    mock_rep = Mock()
    mock_rep.ok = True
    mock_rep.json.return_value = {
        "authconfig": "Translation platform statistics are in sync with the build system."
    }
    return mock_rep


def mock_package_add():
    """
    package_add mock value
    """
    mock_rep = Mock()
    mock_rep.ok = True
    mock_rep.json.return_value = {
        "abrt": "Package added Successfully."
    }
    return mock_rep


def mock_coverage_rule():
    """
    rule_coverage mock value
    """
    mock_rep = Mock()
    mock_rep.ok = True
    mock_rep.json.return_value = {
        "coverage": {
            "evolution": {
                "translation_platform": {
                    "German": {
                        "Total": 5600,
                        "Translated": 5482,
                        "Untranslated": 102,
                        "Remaining": 1.82
                    },
                },
                "build_system": {
                    "f30": {
                        "German": {
                            "Total": 1841,
                            "Translated": 1841,
                            "Untranslated": 0,
                            "Remaining": 0
                        },
                    }
                }
            },
            "libuser": {
                "translation_platform": {
                    "German": {
                        "Total": 301,
                        "Translated": 301,
                        "Untranslated": 0,
                        "Remaining": 0
                    },
                },
                "build_system": {
                    "f30": {
                        "Statistics": "Not Synced with Build System for f30"
                    }
                }
            },
            "release": "fedora-30",
            "coverage_rule": "rhinstaller"
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


def mock_release_status_by_locale():
    """
    release_status_by_locale mock value
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
            "Calculated on": "Messages",
            "locale": "ja_JP"
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


def mock_package_exists():
    """
    package_exists mock value
    """
    mock_rep = Mock()
    mock_rep.ok = True
    mock_rep.json.return_value = {
        "iok": True
    }
    return mock_rep


def mock_job_run_syncupstream():
    """
    job_run mock value
    """
    mock_rep = Mock()
    mock_rep.ok = True
    mock_rep.json.return_value = {
        "Success": "Job created and logged. "
                   "URL: http://localhost:8080/jobs/log/e41ee603-9bdc-4640-83f3-aa8c82263831/detail",
        "job_id": "e41ee603-9bdc-4640-83f3-aa8c82263831"
    }
    return mock_rep


def mock_job_run_stringchange():
    """
    job_run mock value
    """
    mock_rep = Mock()
    mock_rep.ok = True
    mock_rep.json.return_value = {
        "Success": "Job created and logged. "
                   "URL: http://test.transtats.org/jobs/log/bda71131-d177-44d9-9ee7-5df53f03c024/detail",
        "job_id": "bda71131-d177-44d9-9ee7-5df53f03c024"
    }
    return mock_rep


def mock_job_log():
    """
    job_log mock value
    """
    mock_rep = Mock()
    mock_rep.ok = True
    mock_rep.json.return_value = {
        "id": "bda71131-d177-44d9-9ee7-5df53f03c024",
        "type": "stringchange",
        "start_time": "2018-08-03 11:39:00",
        "end_time": "2018-08-03 11:39:02",
        "result": True,
        "remarks": "iok",
        "YML_input": "job: exception: raise execution: sequential name: string change package: iok",
        "log_output": {
            "Clone Repository": {
                "2018-08-03 11:39:01.006607": "Start cloning https://pagure.io/iok.git repository.",
                "2018-08-03 11:39:01.730884": " :: Cloning git repo completed., .git, "
            },
            "Generate POT File": {
                "2018-08-03 11:39:02.022360": " :: POT file generated successfully. [ iok.pot ], "
            },
            "Calculate Differences": {
                "2018-08-03 11:39:02.142378": "No new or updated messages found."
            },
            "Download platform POT file": {
                "2018-08-03 11:39:02.134145": "POT downloaded successfully. "
                                              "URL: https://fedora.../pot?docId=iok"
            }
        }
    }
    return mock_rep
