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

from tabulate import tabulate
from tscli.restapi import ConsumeAPIs


class TextOutputAPIs(object):
    """
    Plain text output for Transtats APIs
    """
    def __init__(self, base_url):
        """
        Constructor
        :param base_url: Server Base URL
        """
        self.raw_data = ConsumeAPIs(base_url)

    @property
    def server_version(self):
        """
        Fetch transtats server version
        """
        dict_data = self.raw_data.server_version
        for machine_name, machine_value in dict_data.items():
            if machine_value == "Not Found":
                print("Server version information is not available")
                return
            else:
                print("Transtats server : {0}".format(
                    "".join(machine_value.split()[1:])))
        return

    def package_status(self, package):
        """
        Fetch package status
        """
        table_headers = ["Language", "Completion %"]
        json_data = self.raw_data.package_status(package)

        # Get key pkg_name and its value
        for pkg_name, pkg_value in json_data.items():
            if pkg_value == "Not Found":
                print("Package not available on transtats server")
                return
            print("Package : {0}".format(pkg_name))

            for lvl2_name, lvl2_value in pkg_value.items():
                # This gives language and its status percentage
                if isinstance(lvl2_value, dict):
                    print("")
                    for b_keys, b_values in lvl2_value.items():
                        print("Branch : {0}".format(b_keys))
                        print(tabulate(sorted(b_values.items()),
                                       table_headers))
                        print("")
                else:
                    print("{0}: {1}".format(lvl2_name, lvl2_value))

        return

    def rule_coverage(self, graph_rule):
        """
        Fetch graph rule coverage
        """
        table_headers = ["Package", "Completed %"]
        json_data = self.raw_data.rule_coverage(graph_rule)

        rule = list(json_data.values())[0]
        if rule == "Not Found":
            print("Rule does not exist, Please enter valid graph rule name.")
            return

        for key, value in rule.items():
            if key == "branch":
                branch_info = value
            if key == "translation_stats":
                lang_stats = value
            if key == "graph_rule":
                rule_name = value

        print("Graph Rule : {0}".format(rule_name))
        print("Branch : {0}".format(branch_info))
        print("")
        for lang_name, pkg_stats in lang_stats.items():
            print("Language : {0}".format(lang_name))
            print(tabulate(sorted(pkg_stats.items()), table_headers))
            print("")

        return

    def release_status(self, release, locale=None, detail=None):
        """
        Fetch release status
        """
        table_headers = ["Package", "Total", "Translated",
                         "Untranslated", "Remaining"]
        print_data = []
        count_method = ""

        if detail:
            json_data = self.raw_data.release_status(release, locale=None,
                                                     detail=True)

            for lang_name, pkg_stats in json_data.items():
                if pkg_stats == "Release not found":
                    print("Release does not exist, Please enter "
                          "valid release name.")
                    return
                if lang_name == "Release":
                    rel_branch = pkg_stats
                    print("Release status for : {0}".format(rel_branch))
                else:
                    print_data = []
                    for pkg_name, stats in pkg_stats.items():
                        stat_list = []
                        if pkg_name != "Calculated on":
                            stat_list.append(pkg_name)
                            stat_list.append(stats.get('Total', 0))
                            stat_list.append(stats.get('Translated', 0))
                            stat_list.append(stats.get('Untranslated', 0))
                            stat_list.append("{}%".format(str(stats.get(
                                'Remaining', 0))))
                            print_data.append(stat_list)
                        else:
                            count_method = stats
                    print("Language : {0}".format(lang_name))
                    print("Calculated on : {0}".format(count_method))
                    print("")
                    print(tabulate(sorted(print_data), table_headers))
                    print("")
        elif locale:
            json_data = self.raw_data.release_status(release, locale,
                                                     detail=False)

            pkg_stats = list(json_data.values())[0]
            rel_branch = list(json_data.keys())[0]
            print_data = []
            not_a_pkg_elements = ("Calculated on", "locale")

            if type(pkg_stats) == str:
                print("Either release " + release + " does not exists or "
                      "locale " + locale + " does not belong to "
                      "requested release " + release)
                return
            for pkg_name, stats in pkg_stats.items():
                stat_list = []
                if pkg_name not in not_a_pkg_elements:
                    stat_list.append(pkg_name)
                    stat_list.append(stats.get('Total', 0))
                    stat_list.append(stats.get('Translated', 0))
                    stat_list.append(stats.get('Untranslated', 0))
                    stat_list.append("{}%".format(str(stats.get(
                                'Remaining', 0))))
                    print_data.append(stat_list)
                elif pkg_name == "Calculated on":
                    count_method = stats
            print("Release status for : {0}".format(rel_branch))
            print("Locale : {0}".format(locale))
            print("Calculated on : {0}".format(count_method))
            print("")
            print(tabulate(sorted(print_data), table_headers))
            print("")
        else:
            json_data = self.raw_data.release_status(release)

            rel_branch = list(json_data.keys())[0]
            rel_data = list(json_data.values())[0]
            if rel_data == "Release not found":
                print("Release does not exist, Please enter valid "
                      "release name.")
                return

            for pkg_name, pkg_stats in rel_data.items():
                stat_list = []
                if pkg_name != "Calculated on":
                    stat_list.append(pkg_name)
                    stat_list.append(pkg_stats.get('Total', 0))
                    stat_list.append(pkg_stats.get('Translated', 0))
                    stat_list.append(pkg_stats.get('Untranslated', 0))
                    stat_list.append("{}%".format(str(pkg_stats.get(
                        'Remaining', 0))))
                    print_data.append(stat_list)
                else:
                    count_method = pkg_stats
            print("Release status for : {0}".format(rel_branch))
            print("Calculated on : {0}".format(count_method))
            print("")
            print(tabulate(sorted(print_data), table_headers))

        return
