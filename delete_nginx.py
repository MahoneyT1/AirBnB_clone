sudo systemctl stop nginx
sudo apt-get remove --purge nginx nginx-common
sudo apt-get autoremove
sudo apt-get autoclean
sudo rm -rf /etc/nginx
sudo rm -rf /var/www/html
sudo apt-get update
sudo apt-get install nginx
sudo systemctl enable nginx
sudo systemctl status nginx
