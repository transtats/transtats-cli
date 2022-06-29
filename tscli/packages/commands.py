# Copyright 2018 Red Hat, Inc.
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


@click.group()
def package():
    """Package related operations"""


@package.command()
@click.option(
    '--server-url', envvar='TRANSTATS_SERVER', help="Transtats Server URL")
@click.option(
    '--token', envvar='TOKEN', help="Transtats API token")
@click.option("--upstream-url", is_flag=False,
              help="source repository url like github or gitlab")
@click.option("--transplatform-slug", is_flag=False,
              help="platform slug like WLTEFED for fedora weblate")
@click.option("--release-stream", is_flag=False,
              help="product like fedora")
@click.option(
    '--json', is_flag=True, envvar='JSON_OUTPUT', help="Print in JSON format")
@click.argument('package_name')
@click.pass_obj
def add(app_context, server_url, token, package_name, upstream_url,
        transplatform_slug, release_stream, json):
    """Add a package to Transtats server."""
    api_obj = ConsumeAPIs(server_url or app_context.server_url) if json \
        else TextOutputAPIs(server_url or app_context.server_url)

    response = api_obj.add_package(package_name, upstream_url,
                                   transplatform_slug, release_stream)
    if isinstance(response, dict):
        app_context.print_r(response)


@package.command()
@click.option(
    '--server-url', envvar='TRANSTATS_SERVER', help="Transtats Server URL")
@click.option("--exist", is_flag=True,
              help="Determine if the package exist in Transtats or not.")
@click.option("--health", is_flag=True,
              help="Get package health")
@click.option(
    '--json', is_flag=True, envvar='JSON_OUTPUT', help="Print in JSON format")
@click.argument('package-name')
@click.pass_obj
def status(app_context, server_url, package_name, exist, health, json):
    """Translation status of a package.
       e.g. transtats package anaconda """
    api_obj = ConsumeAPIs(server_url or app_context.server_url) if json \
        else TextOutputAPIs(server_url or app_context.server_url)

    if exist:
        response = api_obj.package_status(package_name, exist=True, health=None)
    elif health:
        response = api_obj.package_status(package_name, exist=None, health=True)
    else:
        response = api_obj.package_status(package_name, exist=None, health=None)
    if isinstance(response, dict):
        app_context.print_r(response)
