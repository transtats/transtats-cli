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

import click
from tscli.restapi import ConsumeAPIs
from tscli.textoutput import TextOutputAPIs


@click.command()
@click.option(
    '--server-url', envvar='TRANSTATS_SERVER', help="Transtats Server URL")
@click.option("--detail", is_flag=True,
              help="For individual packages grouped by languages.")
@click.option("--locale", is_flag=False,
              help="For individual language specific output.")
@click.option(
    '--json', is_flag=True, envvar='JSON_OUTPUT', help="Print in JSON format")
@click.argument('release-slug')
@click.pass_obj
def release(app_context, server_url, detail, release_slug, locale, json):
    """Translation status of a release slug/branch.
       e.g. transtats release fedora-29 """
    api_obj = ConsumeAPIs(server_url or app_context.server_url) if json \
        else TextOutputAPIs(server_url or app_context.server_url)

    if detail:
        if locale:
            print("Ignoring locale option as detail option also given")
        response = api_obj.release_status(release_slug, locale=None,
                                          detail=True)
    elif locale:
        response = api_obj.release_status(release_slug, locale, detail=False)
    else:
        response = api_obj.release_status(release_slug)

    if isinstance(response, dict):
        app_context.print_r(response)


@click.command()
@click.option(
    '--server-url', envvar='TRANSTATS_SERVER', help="Transtats Server URL")
@click.option(
    '--json', is_flag=True, envvar='JSON_OUTPUT', help="Print in JSON format")
@click.argument('coverage-rule')
@click.pass_obj
def coverage(app_context, server_url, coverage_rule, json):
    """Translation coverage as per coverage rule.
       e.g. transtats coverage rhinstaller """

    api_obj = ConsumeAPIs(server_url or app_context.server_url) if json \
        else TextOutputAPIs(server_url or app_context.server_url)

    response = api_obj.rule_coverage(coverage_rule)
    if isinstance(response, dict):
        app_context.print_r(response)
