#!/usr/bin/python3
"""
Packing a web_static to deploy
"""


from fabric.api import local
from datetime import datetimei
from os.path import isdir


def do_pack():
    """generates a tgz archive"""
    try:
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(current_time)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None
