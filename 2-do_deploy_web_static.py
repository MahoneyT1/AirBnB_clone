from fabric.api import run, put, env, sudo
import os

env.hosts = ['3.85.54.81', '52.91.132.58']

def do_deploy(archive_path):
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