#!/usr/bin/python3

from fabric.api import run, put, env, sudo, local
from os.path import isdir, exists
from datetime import datetime
import os


# environment variables for this fabric file
env.user = 'ubuntu'
env.hosts = ['3.85.54.81', '52.91.132.58']
env.key_filename = '~/.ssh/school'

def do_pack() -> str:
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

def do_deploy(archive_path):
    """Write a Fabric script that creates and distributes an
    archive to your web servers, using the function deploy
    """
    if not os.path.exists(archive_path):
        print(f"Archive path {archive_path} does not exist")
        return False
    try:
        # Define paths
        file_name = os.path.basename(archive_path)
        no_ext = file_name.split('.')[0]
        upload_path = f'/tmp/{file_name}'
        uncompress_path = f'/data/web_static/releases/{no_ext}/'
        symbolic_link_path = '/data/web_static/current'

        print(f"Uploading {archive_path} to {upload_path}")
        put(archive_path, upload_path)
        
        print(f"Creating directory {uncompress_path}")
        run(f'sudo mkdir -p {uncompress_path}')
        
        print(f"Uncompressing {upload_path} to {uncompress_path}")
        run(f'sudo tar -xzvf {upload_path} -C {uncompress_path}')
        
        print(f"Removing uploaded archive {upload_path}")
        run(f'sudo rm {upload_path}')
        
        print(f"Removing unnecessary folders")
        run(f'sudo rm -rf {uncompress_path}images {uncompress_path}styles')
        
        print(f"Moving files from {uncompress_path}web_static to {uncompress_path}")
        run(f'sudo mv {uncompress_path}web_static/* {uncompress_path}')
        
        print(f"Removing web_static folder {uncompress_path}web_static/")
        run(f'sudo rm -rf {uncompress_path}web_static/')
        
        print(f"Removing existing symbolic link {symbolic_link_path}")
        run(f'sudo rm -rf {symbolic_link_path}')
        
        print(f"Creating new symbolic link from {uncompress_path} to {symbolic_link_path}")
        run(f'sudo ln -s {uncompress_path} {symbolic_link_path}')
        
        print("Starting or reloading nginx")
        run('sudo systemctl start nginx || true')
        run('sudo nginx -t')
        run('sudo systemctl reload nginx || sudo systemctl start nginx')

        print("New version deployed!")
        return True
    except Exception as e:
        print(f"Deployment failed: {e}")
        return False

def deploy():
    """The script should take the following steps:
    Call the do_pack() function and store the path of the
    created archive
    """

    path_to_achieved_folder = do_pack()

    if path_to_achieved_folder is False:
        return False

    # check the return value of doploy if it return
    path_created = do_deploy(path_to_achieved_folder)

    if path_created is False:
        return False
    return True