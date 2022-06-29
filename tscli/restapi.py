# Copyright 2017-2019 Red Hat, Inc.
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

import json
import requests

from tscli.config import get_config, get_config_item


class ConsumeAPIs(object):
    """
    Consume Transtats APIs
    """
    base_URL = None
    middle_URL = "api"

    ERR_JSON = {"Error": "Something unexpected happened."}

    def __init__(self, base_url):
        """
        Constructor
        :param base_url: Server Base URL
        """
        self.base_URL = base_url \
            if base_url.endswith("/") else base_url + "/"
        self.config = get_config()
        self.token = get_config_item(
            self.config, 'server', 'token')

    def _call_api(self, endpoint):
        """
        Single point to call API
        """
        try:
            response = requests.get(self.base_URL + self.middle_URL + endpoint)
        except Exception:
            return self.ERR_JSON
        else:
            return response.json() if response.ok else self.ERR_JSON

    def _read_token(self):
        """
        Read the token value
        """
        return self.token

    def _send_api(self, endpoint, payload):
        """
        Single point to send API
        """
        head = {'Authorization': 'token {}'.format(self._read_token()),
                'Content-Type': 'application/json'}
        try:
            response = requests.post(self.base_URL + self.middle_URL + endpoint,
                                     headers=head, data=json.dumps(payload))
        except Exception:
            return self.ERR_JSON

        return response.json() if response.ok else self.ERR_JSON

    @property
    def server_version(self):
        """
        Fetch transtats server version
        :return: dict
        """
        ENDPOINT = "/ping"
        return self._call_api(ENDPOINT)

    def package_status(self, package, exist=None, health=None):
        """
        Fetch package status
        """
        ENDPOINT = "/package/" + package
        if exist:
            ENDPOINT = ENDPOINT + "/exist"
        elif health:
            ENDPOINT = ENDPOINT + "/health"

        return self._call_api(ENDPOINT)

    def rule_coverage(self, coverage_rule):
        """
        Fetch graph rule coverage
        """
        ENDPOINT = "/coverage/" + coverage_rule
        return self._call_api(ENDPOINT)

    def release_status(self, release, locale=None, detail=None):
        """
        Fetch release status
        """
        ENDPOINT = "/release/" + release
        if detail:
            ENDPOINT = ENDPOINT + "/detail"
        elif locale:
            ENDPOINT = ENDPOINT + "/locale/" + locale
        return self._call_api(ENDPOINT)

    def job_log(self, job_id):
        """
        Fetch the logs for the given job id
        """
        ENDPOINT = "/job/" + job_id + "/log"
        return self._call_api(ENDPOINT)

    def job_run(self, job_type, package_name, build_system=None, build_tag=None,
                release_slug=None, repo_type=None, repo_branch=None):
        """
        Submit the job for the given job type and package name
        """
        ENDPOINT = "/job/run"
        _ENDPOINT = "/package/" + package_name + "/exist"
        pkg_exists = self._call_api(_ENDPOINT)
        if list(pkg_exists.values())[0]:
            if job_type == "syncupstream":
                payload = {'job_type': job_type, 'package_name': package_name,
                           'repo_type': repo_type, 'repo_branch': repo_branch}
            elif job_type == "syncdownstream":
                payload = {'job_type': job_type, 'package_name': package_name,
                           'build_system': build_system,
                           'build_tag': build_tag}
            elif job_type == "stringchange":
                payload = {'job_type': job_type, 'package_name': package_name,
                           'release_slug': release_slug}
            else:
                return {"job_type": "Invalid job type"}
        else:
            return {"pkg_error": "Given package does not exists"}

        return self._send_api(ENDPOINT, payload)

    def add_package(self, package_name, upstream_url, transplatform_slug, release_stream):
        """
        Create a new package at Transtats Server
        """
        ENDPOINT = "/package/create"
        payload = {
            "package_name": package_name,
            "upstream_url": upstream_url or "",
            "transplatform_slug": transplatform_slug or "",
            "release_streams": release_stream or ""
        }

        return self._send_api(ENDPOINT, payload)
