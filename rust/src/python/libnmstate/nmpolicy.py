# SPDX-License-Identifier: LGPL-2.1-or-later


import json

from .clib_wrapper import net_state_from_policy


def gen_net_state_from_policy(policy, cur_state):
    return json.loads(net_state_from_policy(policy, cur_state))
