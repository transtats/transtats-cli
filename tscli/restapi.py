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


import requests


class ConsumeAPIs(object):
    """
    Consume Transtats APIs
    """
    base_URL = None
    middle_URL = "api"

    ERR_JSON = {"Error": "Some thing unexpected happened."}

    def __init__(self, base_url):
        """
        Constructor
        :param base_url: Server Base URL
        """
        self.base_URL = base_url \
            if base_url.endswith("/") else base_url + "/"

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

    @property
    def server_version(self):
        """
        Fetch transtats server version
        :return: dict
        """
        ENDPOINT = "/ping"
        return self._call_api(ENDPOINT)

    def package_status(self, package):
        """
        Fetch package status
        """
        ENDPOINT = "/package/" + package + "/"
        return self._call_api(ENDPOINT)

    def rule_coverage(self, graph_rule):
        """
        Fetch graph rule coverage
        """
        ENDPOINT = "/coverage/" + graph_rule + "/"
        return self._call_api(ENDPOINT)

    def release_status(self, release, detail=None):
        """
        Fetch release status
        """
        ENDPOINT = "/release/" + release + "/"
        if detail:
            ENDPOINT = ENDPOINT + "detail"
        return self._call_api(ENDPOINT)
