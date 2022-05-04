# How it works:

echo "1. Script will create new user."
echo "2. ...and user home folder /home/user_name"
echo "3. ...and ssh key pair within /home/user_name.ssh folder"
echo "4. Login is allowed by a key only."
echo "5. Sudo is allowed with no password (good luck)."
echo "6. Add user to groups 'sudo' and 'www-data'"
echo " "


# Some constans

user_name=$(read -p 'Username (allowed characters: a-z, A-Z, 0-9, -, _, for more see NAME_REGEX): ')
klucz=zpxd_
klucz+=$user_name
server_ip=`curl -s http://checkip.amazonaws.com`


# To be developed - options:

password=None # yes/no
groups=None # standard / others
allow_sudo=None # yes/no
key=None # yes/no


# Create user.

adduser $user_name --gecos GECOS --disabled-password --force-badname
adduser $user_name sudo
adduser $user_name www-data


# Allow user to use sudo without password.

echo "$user_name ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers


# RSA Keys Pair.

mkdir /home/$user_name/.ssh
chmod 700 /home/$user_name/.ssh

ssh-keygen -t rsa -b 4096 -f /home/$user_name/.ssh/$klucz -C $user_name -N ''
cat /home/$user_name/.ssh/$klucz.pub > /home/$user_name/.ssh/authorized_keys
chmod 600 /home/$user_name/.ssh/authorized_keys
chmod 600 /home/$user_name/.ssh/$klucz
chown -R $user_name:$user_name /home/$user_name/.ssh


# What now.

echp " "
echo "What now?"
echo " "
echo "1. In your computer terminall/powershell go to .ssh folder and download the key:"
if [ $(getent passwd ubuntu) ] ; then
	cp -f /home/$user_name/.ssh/$klucz /home/ubuntu/$klucz
	echo "scp -i twoj_klucz_z_aws.pem ubuntu@$server_ip:/home/ubuntu/$klucz $klucz"
else
	cp -f /home/$user_name/.ssh/$klucz /root/$klucz
	echo "scp root@$server_ip:/root/$klucz $klucz"
fi

echo " "
echo "2. Update your ~/.ssh/config file (add lines below and ensure unique Host's names):"
echo " "

echo "Host xd_root"
echo "	HostName $server_ip"
echo "	User root"
echo " "
echo "Host xd_$user_name"
echo "	HostName $server_ip"
echo "	User $user_name"
echo "	IdentityFile "~/.ssh/$klucz""

echo " "
echo "3. Log in to server from Your terminal/powershell using:"
echo " "
echo "ssh xd_$user_name"

echo " "
echo "4. Concider to block loging in to your server by root."
echo " "
