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


@click.command()
@click.argument('package-name')
def status(package_name):
    """Translation status of a package."""
    click.echo("%s Status" % package_name)


@click.command()
@click.argument('graph-rule')
def coverage(graph_rule):
    """Translation coverage as per graph rule."""
    click.echo("Graph rule %s" % graph_rule)


@click.command()
@click.option("--detail", is_flag=True, help="For individual packages grouped by languages.")
@click.argument('release-branch')
def workload(detail, release_branch):
    """Translation workload of a release branch."""
    if detail:
        click.echo("detail view")
    click.echo("Translation Workload %s" % release_branch)
