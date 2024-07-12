#!/usr/bin/python3
"""
script based on the file 2-do_deploy_web_static.py that creates and
distributes an archive to the web servers
"""

from fabric.api import env, local, run, lcd, cd
from datetime import datetime
from os import listdir
env.hosts = ['54.237.25.186', '100.25.21.22']



def do_clean(number=0):
    """Delete out-of-date archives"""
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
