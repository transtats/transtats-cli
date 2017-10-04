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

import os
import json
import click

import tscli.config

from tscli.common import commands as common
from tscli.translations import commands as trans


class AppContext(object):
    """
    CLI Application Context Data
    """
    def __init__(self, app_config):
        self.version = "0.1.0"

        for attrib, value in app_config.items():
            setattr(self, str(attrib), value)

    @staticmethod
    def print_r(result_dict):
        click.echo(json.dumps(result_dict, indent=4, sort_keys=True))


@click.group()
@click.pass_context
def entry_point(ctx):
    config_path = os.path.join(str(os.path.expanduser("~")) +
                               "/.config/", "transtats.conf")
    try:
        # Parse Config
        with open(config_path) as config_file:
            config_data = json.loads(config_file.read())
    except (IOError, Exception):
        click.echo("Config file could not be loaded.")
        exit(1)
    else:
        ctx.obj = AppContext(config_data)

ts_config_file = tscli.config.get_config()

entry_point.add_command(common.version)
entry_point.add_command(trans.status)
entry_point.add_command(trans.coverage)
entry_point.add_command(trans.workload)
