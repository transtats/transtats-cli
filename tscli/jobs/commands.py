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
def job():
    """Job related operations"""


@job.command()
@click.option(
    '--server-url', envvar='TRANSTATS_SERVER', help="Transtats Server URL")
@click.option(
    '--token', envvar='TOKEN', help="Transtats API token")
@click.option("--build-system", is_flag=False,
              help="build system like koji")
@click.option("--build-tag", is_flag=False,
              help="build tag like f29")
@click.option("--release-slug", is_flag=False,
              help="release name like fedora-29")
@click.option(
    '--json', is_flag=True, envvar='JSON_OUTPUT', help="Print in JSON format")
@click.argument('job_type')
@click.argument('package_name')
@click.pass_obj
def run(app_context, server_url, token, job_type, package_name, build_system,
        build_tag, release_slug, json):
    """Runs a job and/or show the job log. Available job-types are
       syncupstream, syncdownstream, stringchange."""
    api_obj = ConsumeAPIs(server_url or app_context.server_url) if json \
        else TextOutputAPIs(server_url or app_context.server_url)

    response = api_obj.job_run(job_type, package_name, build_system,
                               build_tag, release_slug)
    if isinstance(response, dict):
        app_context.print_r(response)


@job.command()
@click.option(
    '--server-url', envvar='TRANSTATS_SERVER', help="Transtats Server URL")
@click.option(
    '--json', is_flag=True, envvar='JSON_OUTPUT', help="Print in JSON format")
@click.argument('job_id')
@click.pass_obj
def log(app_context, server_url, job_id, json):
    """Show the log for a given job id.
       e.g. transtats job log <job-id>"""
    api_obj = ConsumeAPIs(server_url or app_context.server_url) if json \
        else TextOutputAPIs(server_url or app_context.server_url)

    response = api_obj.job_log(job_id)
    if isinstance(response, dict):
        app_context.print_r(response)
