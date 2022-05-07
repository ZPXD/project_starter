# Project starter

# Change some constans below


# Some constans:

domena=$1
project_name=$2
project_user=$3
project_repo=$4
projects_folder=/var/www


# Check if you are a root.

if [ $USER == "root"  ] ; then
    echo "USER to root - OK"
else
    echo "PRZELOGUJ SIE NA ROOTa, wpisz:"
    echo "sudo su"
    exit
fi


# Check domain.

apt update --yes
apt install curl --yes
server_ip=`curl -s http://checkip.amazonaws.com`
dns_ip=$(host $domena | grep address | awk 'NR==1{ print $4 }')
#dns_ip=$(host $domena | awk '{ print $4 }')
if [ "$server_ip" = "$dns_ip" ] ; then
    echo "DOMENA OK"
else
    echo "DOMENA NIE OK"
fi


# Server preparation.

apt update --yes # Already updated

systemctl stop apache
apt remove apache2 --yes
apt install nginx --yes
systemctl enable nginx
systemctl start nginx


# Soft

# Required soft.

apt install curl --yes # Already installed
apt install git --yes

# Python 3.

apt install python3-pip --yes 
apt install python3-dev --yes 
apt install python3-venv --yes 
apt install build-essential --yes 
apt install libssl-dev --yes 
apt install libffi-dev --yes
apt install python3-setuptools --yes

# Useful.

apt install nano --yes
apt install tree --yes


# Places for project.

mkdir $projects_folder
chown -R www-data:www-data $projects_folder
chmod -R 775 $projects_folder


# Project starter.

git clone https://github.com/ZPXD/project_starter.git $projects_folder/project_starter


# Project.

project_folder=$projects_folder/$project_name
git clone $project_repo $project_folder


# Environment.

project_venv=$project_folder/$project_name
project_venv+=venv
activate_venv_path=$project_venv
activate_venv_path+=/bin/activate

python3 -m venv $project_venv
source $activate_venv_path

export FLASK_APP=app.py
pip3 install -r $project_folder/requirements.txt
pip3 install gunicorn

# Server files landing.
python3 $projects_folder/project_starter/scripts/project_starter.py $projects_folder $project_name $domena 

# Create user.
bash $projects_folder/project_starter/scripts/create_user.sh


# Cybersecurity Tower scripts:
git clone https://github.com/ZPXD/project_starter.git $projects_folder/tower_cybersecurity

# Configure sshd_config.
bash $projects_folder/tower_cybersecurity/scripts/config_sshd_config.py
echo "Logging in by password by root is not allowed now. Use $project_user key login."

# Allow no password sudo for user.
bash $projects_folder/tower_cybersecurity/scripts/nopassword_sudo.py $project_user 1


# Grant user the rights to the projects folder and all projects within.
chown -R $project_user:$project_user $projects_folder
systemctl enable $project_name

# Done.
pip3 install lolpython
python3 $projects_folder/project_starter/scripts/banner.py

echo " "
echo "gz"


