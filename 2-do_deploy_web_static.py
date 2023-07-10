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
        file_withoutext = path.splitext(filename)[0]
        sudo("mkdir -p /data/")
        sudo("chown -R $USER:$USER /data/")
        release_folder = "/data/web_static/releases/{}".format(file_withoutext)
        sudo("mkdir -p {}".format(release_folder))
        sudo("tar -xzf /tmp/{} -C {}".format(filename, release_folder))
        sudo("rm /tmp/{}".format(filename))
        sudo('mv -u {}/web_static/* {}'.format(release_folder, release_folder))
        sudo("rm -f /data/web_static/current")
        sudo("ln -s {} /data/web_static/current".format(release_folder))
        print("A new version deployed")
        return True
    except Exception as e:
        print("Failed: {}".format(e))
        return False
