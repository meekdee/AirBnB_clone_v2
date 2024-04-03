#!/usr/bin/python3
"""Fabric script that creates and distributes an archive to my web servers
"""
from fabric.api import *
from datetime import datetime
import os

env.hosts = ["54.157.143.129", "100.25.191.64"]
env.user = "ubuntu"


def do_pack():
    """Creates an archive from the web_static folder"""
    local('mkdir -p versions')
    now = datetime.now()
    date_time = now.strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(date_time)
    result = local("tar -czvf {} web_static".format(archive_path))
    if result.failed:
        return None
    return archive_path


def do_deploy(archive_path):
    """Distributes an archive to my web servers"""
    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        file_name = archive_path.split('/')[-1]
        folder_name = file_name.split('.')[0]
        release_folder = '/data/web_static/releases/{}'.format(folder_name)
        run('sudo mkdir -p {}'.format(release_folder))
        run('sudo tar -xzf /tmp/{} -C {}/'.format(file_name, release_folder))
        run('sudo rm /tmp/{}'.format(file_name))
        run('sudo mv {}/web_static/* {}/'.format(release_folder, release_folder))
        run('sudo rm -rf {}/web_static'.format(release_folder))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {} /data/web_static/current'.format(release_folder))
        return True
    except Exception:
        return False

def deploy():
    """Creates and distributes an archive to my web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
