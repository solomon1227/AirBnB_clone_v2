#!/usr/bin/python3
"""
Do clean function added - for cleaning older version
"""

from fabric.api import *
from datetime import datetime
import os

env.hosts = ['54.237.25.186', '100.25.21.22']


def do_clean(number=0):
    """Delete out-of-date archives"""
    if number == 0 or number == 1:
        number = 2 # Keep only the most recent and second most recent versions
    else:
        number += 1

    with lcd("versions"):
        local("ls -t | tail -n +{} | xargs -I {{}} rm -- {{}}".format(number))

    with cd("/data/web_static/releases"):
        run("ls -t | tail -n +{} | xargs -I {{}} rm -rf -- {{}}".format(number))
