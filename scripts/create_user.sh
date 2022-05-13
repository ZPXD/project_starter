# How it works:

echo "1. Script will create new user."
echo "2. ...and user home folder /home/user_name"
echo "3. ...and ssh key pair within /home/user_name.ssh folder"
echo "4. Login is allowed by a key only."
echo "5. Sudo is allowed with no password (good luck)."
echo "6. Add user to groups 'sudo' and 'www-data'"
echo " "


# Some constans

read -p 'Username (allowed characters: a-z, A-Z, 0-9, -, _, for more see NAME_REGEX): ' user_name

# To be developed - options:

password=None # yes/no
groups=None # standard / others
allow_sudo=None # yes/no

# Create user.

adduser $user_name --gecos GECOS --disabled-password --force-badname
adduser $user_name sudo
adduser $user_name www-data

# Allow user to use sudo without password.

echo "$user_name ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# What now.

echp " "
echo "What now?"
echo " "
echo "1. User server_keys_computer_side.py on Your computer to create pair of keys, or just run:
echo " " 
echo "ssh-keygen -t rsa -b 4096 -N '' -f SCIEZKA_DO_KLUCZA \<<< y"
echo "ssh-copy-id -i SCIEZKA_DO_KLUCZA LOGIN@IP_ADDR -f"
echo " "
echo "In case of any troubles say so on ZPXD discord (open server)."
echo " " 

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

echo "RLY."
