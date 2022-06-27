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

    def test_version_cli(self):
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
        transtats package stats <package>
        """
        from tscli import entry_point

        with patch('requests.get') as mock_request_get:
            mock_request_get.return_value = \
                test_data.mock_package_status()
            runner = CliRunner()
            result = runner.invoke(entry_point, ['package', 'stats', 'systemd'])
            self.assertEqual(result.exit_code, 0)
            self.assertIn('systemd', result.output)
            self.assertIn('Branch', result.output)
            self.assertIn('percentage_calculated_on', result.output)

    def test_package_status_exist(self):
        """
        transtats package --exist stats <package>
        """
        from tscli import entry_point

        with patch('requests.get') as mock_request_get:
            mock_request_get.return_value = \
                test_data.mock_package_status_exist()
            runner = CliRunner()
            result = runner.invoke(entry_point, ['package', 'stats', '--exist',
                                                 'gnome-shell', '--json'])
            self.assertEqual(result.exit_code, 0)
            self.assertIn('gnome-shell', result.output)
            self.assertIn('true', result.output)

    def test_package_status_health(self):
        """
        transtats package --health stats <package>
        """
        from tscli import entry_point

        with patch('requests.get') as mock_request_get:
            mock_request_get.return_value = \
                test_data.mock_package_status_health()
            runner = CliRunner()
            result = runner.invoke(entry_point, ['package', 'stats', '--health',
                                                 'abrt', '--json'])
            self.assertEqual(result.exit_code, 0)
            self.assertIn('abrt', result.output)
            self.assertIn('fedora-30', result.output)

    def test_package_status_health_in_sync(self):
        """
        transtats package --health stats <package>
        """
        from tscli import entry_point

        with patch('requests.get') as mock_request_get:
            mock_request_get.return_value = \
                test_data.mock_package_status_health_in_sync()
            runner = CliRunner()
            result = runner.invoke(entry_point, ['package', 'stats', '--health',
                                                 'authconfig', '--json'])
            self.assertEqual(result.exit_code, 0)
            self.assertIn('authconfig', result.output)
            self.assertIn('are in sync', result.output)

    def test_coverage_rule(self):
        """
        transtats coverage <graph_rule>
        """
        from tscli import entry_point

        with patch('requests.get') as mock_request_get:
            mock_request_get.return_value = \
                test_data.mock_coverage_rule()
            runner = CliRunner()
            result = runner.invoke(entry_point, ['coverage', 'rhinstaller'])
            self.assertEqual(result.exit_code, 0)
            self.assertIn('Branch : fedora-30', result.output)
            self.assertIn('Coverage Rule : rhinstaller', result.output)

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

    def test_job_run_upstream(self):
        """
        transtats job run --repo-type=<type> --repo-branch=<branch> <job-type> <package>
        """
        from tscli import entry_point

        with patch('requests.get') as mock_request_get:
            with patch('requests.post') as mock_request_post:
                mock_request_get.return_value = \
                    test_data.mock_package_exists()
                mock_request_post.return_value = \
                    test_data.mock_job_run_syncupstream()
                runner = CliRunner()
                result = runner.invoke(entry_point,
                                       ['job', 'run', '--repo-type', 'l10n',
                                        '--repo-branch', 'main', 'syncupstream', 'iok'])
                self.assertEqual(result.exit_code, 0)
                self.assertIn('Success', result.output)
                self.assertIn('Job_Id', result.output)

    def test_job_run_stringchange(self):
        """
        transtats job run <job-type> <package> --release-slug <release>
        """
        from tscli import entry_point

        with patch('requests.get') as mock_request_get:
            with patch('requests.post') as mock_request_post:
                mock_request_get.return_value = \
                    test_data.mock_package_exists()
                mock_request_post.return_value = \
                    test_data.mock_job_run_stringchange()
                runner = CliRunner()
                result = runner.invoke(entry_point,
                                       ['job', 'run', 'stringchange', 'iok',
                                        '--release-slug', 'fedora-29'])
                self.assertEqual(result.exit_code, 0)
                self.assertIn('Success', result.output)
                self.assertIn('Job_Id', result.output)

    def test_job_log(self):
        """
        transtats job log <job-id>
        """
        from tscli import entry_point

        with patch('requests.get') as mock_request_get:
            mock_request_get.return_value = \
                test_data.mock_job_log()
            runner = CliRunner()
            result = runner.invoke(entry_point,
                                   ['job', 'log',
                                    '6c919e29-6738-4549-b298-852ff947c023'])

            self.assertEqual(result.exit_code, 0)
            self.assertIn('Job End time', result.output)
            self.assertIn('Job Start time', result.output)
            self.assertIn('Job Type', result.output)
