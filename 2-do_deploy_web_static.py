#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""


from fabric.api import env, run, put
from os import path, environ
env.hosts = ['54.237.25.186', '100.25.21.22']


def do_deploy(archive_path):
    '''Deploys an archive to the web servers.'''

    if not path.exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        filename = path.basename(archive_path)
        filename_without_extension = path.splitext(archive_filename)[0]
        release_folder = "/data/web_static/releases/{}".format(filename_without_extension)
        run("mkdir -p {}".format(release_folder))
        run("tar -xzf /tmp/{} -C {}".format(archive_filename, release_folder))
        run("rm /tmp/{}".format(archive_filename))
        run("rm -f /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(release_folder))
        return True
    except Exception as e:
        return False

