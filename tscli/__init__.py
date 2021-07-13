# Copyright 2017-2021 Red Hat, Inc.
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
import click

from tscli.common import commands as common
from tscli.config import get_config, get_config_item
from tscli.stats import commands as trans
from tscli.jobs import commands as jobs

APP_VERSION = "0.5.0"


class AppContext(object):
    """
    CLI Application Context Data
    """
    def __init__(self):
        self.version = APP_VERSION
        self.config = get_config()
        self.server_url = get_config_item(
            self.config, 'server', 'server_url'
        )

    @staticmethod
    def print_r(result_dict):
        click.echo(json.dumps(result_dict, indent=4, sort_keys=True))


@click.group()
@click.pass_context
def entry_point(ctx):
    """
    Transtats CLI to communicate with server
    """
    ctx.obj = AppContext()


entry_point.add_command(common.version)
entry_point.add_command(trans.package)
entry_point.add_command(trans.release)
entry_point.add_command(trans.coverage)
entry_point.add_command(jobs.job)
