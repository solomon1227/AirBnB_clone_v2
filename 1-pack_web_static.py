#!/usr/bin/python3
from fabric.api import local
from datetime import datetime


def do_pack():
    """Pack the web static folder in to .tgz file format"""
    try:
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = "web_static_" + current_time + ".tgz"
        local("mkdir -p versions")
        local("tar -cvzf versions/{} web_static".format(archive_name))
        return "versions/{}".format(archive_name)
    except Exception as e:
        return None
