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

from cli.common import commands as common
from cli.translations import commands as trans


class AppContext(object):
    """
    CLI Application Context Data
    """
    def __init__(self):
        self.version = "0.1.0"


@click.group()
@click.pass_context
def entry_point(ctx):
    ctx.obj = AppContext()

entry_point.add_command(common.version)
entry_point.add_command(trans.status)
entry_point.add_command(trans.coverage)
entry_point.add_command(trans.workload)
