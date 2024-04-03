#!/usr/bin/python3
"""
Fabric script that generates a .tg.z archive from the contents
of the web_static folder of the AirBnB Clone repo
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """ Generates a .tgz archive from the contents of the web_static folder
    """
    try:
        current_time = datetime.utcnow().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(current_time)
        local("mkdir  -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception:
        return None
