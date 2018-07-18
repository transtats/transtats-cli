# Copyright 2017, 2018 Red Hat, Inc.
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

from __future__ import absolute_import

import os
from unittest import TestCase
from click.testing import CliRunner
from mock import patch
from tests import test_data


class TestTranstatsCLI(TestCase):
    """
    Transtats CLI basic tests
    """

    def setUp(self):
        os.environ["TRANSTATS_TEST_CONFIG"] = 'true'

    def tearDown(self):
        del os.environ["TRANSTATS_TEST_CONFIG"]

    def test_cli_version(self):
        """
        transtats version
        """
        from tscli import entry_point

        runner = CliRunner()
        result = runner.invoke(entry_point, ['version'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn('client', result.output)

    def test_server_version(self):
        """
        transtats version --server
        """
        from tscli import entry_point

        with patch('requests.get') as mock_request_get:
            mock_request_get.return_value = \
                test_data.mock_server_version()
            runner = CliRunner()
            result = runner.invoke(entry_point, ['version', '--server'])
            self.assertEqual(result.exit_code, 0)
            self.assertIn('server', result.output)

    def test_package_status(self):
        """
        transtats status <package>
        """
        from tscli import entry_point

        with patch('requests.get') as mock_request_get:
            mock_request_get.return_value = \
                test_data.mock_package_status()
            runner = CliRunner()
            result = runner.invoke(entry_point, ['package', 'systemd'])
            self.assertEqual(result.exit_code, 0)
            self.assertIn('systemd', result.output)
            self.assertIn('Branch', result.output)
            self.assertIn('percentage_calculated_on', result.output)

    def test_rule_coverage(self):
        """
        transtats coverage <graph_rule>
        """
        from tscli import entry_point

        with patch('requests.get') as mock_request_get:
            mock_request_get.return_value = \
                test_data.mock_rule_coverage()
            runner = CliRunner()
            result = runner.invoke(entry_point, ['coverage', 'rhinstaller'])
            self.assertEqual(result.exit_code, 0)
            self.assertIn('Branch', result.output)
            self.assertIn('Graph Rule', result.output)

    def test_release_status(self):
        """
        transtats status <release>
        """
        from tscli import entry_point

        with patch('requests.get') as mock_request_get:
            mock_request_get.return_value = \
                test_data.mock_release_status()
            runner = CliRunner()
            result = runner.invoke(entry_point, ['release', 'fedora-27'])
            self.assertEqual(result.exit_code, 0)
            self.assertIn('fedora-27', result.output)
            self.assertIn('Calculated on', result.output)

    def test_release_status_json(self):
        """
        transtats status <release> --json
        """
        from tscli import entry_point

        with patch('requests.get') as mock_request_get:
            mock_request_get.return_value = \
                test_data.mock_release_status()
            runner = CliRunner()
            result = runner.invoke(entry_point, ['release', '--json',
                                                 'fedora-27'])
            self.assertEqual(result.exit_code, 0)
            self.assertIsInstance(eval(result.output), dict)
            self.assertIn('fedora-27', result.output)
            self.assertIn('Calculated on', result.output)

    def test_release_status_detail(self):
        """
        transtats status <release> --detail
        """
        from tscli import entry_point

        with patch('requests.get') as mock_request_get:
            mock_request_get.return_value = \
                test_data.mock_release_workload_detail()
            runner = CliRunner()
            result = runner.invoke(entry_point,
                                   ['release', 'fedora-27', '--detail'])
            self.assertEqual(result.exit_code, 0)
            self.assertIn("Release", result.output)
            self.assertIn('Calculated on', result.output)

    def test_release_status_by_locale(self):
        """
        transtats status <release> --locale
        """
        from tscli import entry_point

        with patch('requests.get') as mock_request_get:
            mock_request_get.return_value = \
                test_data.mock_release_status_by_locale()
            runner = CliRunner()
            result = runner.invoke(entry_point,
                                   ['release', 'fedora-27',
                                       '--locale', 'ja_JP'])
            self.assertEqual(result.exit_code, 0)
            self.assertIn('fedora-27', result.output)
            self.assertIn('Calculated on', result.output)
            self.assertIn('Locale', result.output)
