#!/usr/bin/python3
"""
Packing a web_static to deploy
"""


from fabric.api import local
from datetime import datetime


def do_pack():
    """Pack the web static folder in to .tgz file format"""
    try:
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        archive_name = "versions/web_static_" + current_time + ".tgz"
        command = 'tar -czvf {} web_static && echo "web_static packed: {} -> $(du -b {})Bytes"'.format(archive_name, archive_name, archive_name)
        local(command)
        return (archive_name)
    except Exception as e:
        return None
