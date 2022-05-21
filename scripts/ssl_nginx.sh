# Usage:
# sudo bash ssl_nginx.sh $domain

domain=$1
sudo apt update
sudo apt install python3-certbot-nginx
sudo pip install pyOpenSSL --upgrade
sudo certbot --nginx -d $domain -d www.$domain
