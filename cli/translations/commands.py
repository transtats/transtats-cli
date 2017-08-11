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

import click
from cli.restapi import ConsumeAPIs


@click.command()
@click.argument('package-name')
@click.pass_obj
def status(app_context, package_name):
    """Translation status of a package."""
    api_obj = ConsumeAPIs(app_context.server_url)
    response = api_obj.package_status(package_name)
    if isinstance(response, dict):
        app_context.print_r(response)


@click.command()
@click.argument('graph-rule')
@click.pass_obj
def coverage(app_context, graph_rule):
    """Translation coverage as per graph rule."""
    api_obj = ConsumeAPIs(app_context.server_url)
    response = api_obj.rule_coverage(graph_rule)
    if isinstance(response, dict):
        app_context.print_r(response)


@click.command()
@click.option("--detail", is_flag=True, help="For individual packages grouped by languages.")
@click.argument('release-branch')
@click.pass_obj
def workload(app_context, detail, release_branch):
    """Translation workload of a release branch."""
    api_obj = ConsumeAPIs(app_context.server_url)
    response = {}
    if detail:
        response = api_obj.release_workload(release_branch, detail=True)
    else:
        response = api_obj.release_workload(release_branch)
    if isinstance(response, dict):
        app_context.print_r(response)
