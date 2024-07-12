#!/usr/bin/python3
"""This method copies files from web_static
and convert it into .tgz file, compressing
"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """This method copies files from web_static
    and convert it into .tgz file, compressing
    """

    local('sudo mkdir -p versions')

    # Generate the timestamped archive name
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(timestamp)
    archive_path = "versions/{}".format(archive_name)

    # Create the archive
    result = local("sudo tar -czvf {} web_static".format(archive_path))

    # Check if the archive was created successfully
    if result.failed:
        return None
    else:
        return archive_path

