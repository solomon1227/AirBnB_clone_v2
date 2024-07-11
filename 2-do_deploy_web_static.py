#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""


from fabric.api import env, run, put, local
from os import path, environ
from datetime import datetime

env.hosts = ['100.26.236.93', '54.160.114.138']
env.user = 'ubuntu'

def do_pack():
    """Pack the web static folder in to .tgz file format"""
    try:
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        local("chown -hR $USER:$USER versions")
        archive_name = "versions/web_static_" + current_time + ".tgz"
        local("tar -cvzf {} web_static".format(archive_name))
        return (archive_name)
    except Exception as e:
        return None

def do_deploy(archive_path):
    '''Deploys an archive to the web servers.'''

    if not path.exists(archive_path):
        return False
    try:
        run("mkdir -p /data/web_static/releases/")
        put(archive_path, "/tmp/")
        filename = path.basename(archive_path)
        file_withoutext = path.splitext(filename)[0]
        run("chown -hR $USER:$USER /data/")
        release_folder = "/data/web_static/releases/{}".format(file_withoutext)
        run("mkdir -p {}".format(release_folder))
        run("tar -xzf /tmp/{} -C {}".format(filename, release_folder))
        run("rm /tmp/{}".format(filename))
        run('mv -u {}/web_static/* {}'.format(release_folder, release_folder))
        run("rm -f /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(release_folder))
        print("A new version deployed")
        return True
    except Exception as e:
        print("Failed: {}".format(e))
        return False
