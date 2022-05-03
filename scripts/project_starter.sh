# Some constans:
project_user = root # change it
project_repo = https://github.com/ZPXD/what_what.git # change it
projects_folder = /var/www


# Check if you are a root.

if [ $USER == "root"  ] ; then
    echo "USER to root - OK"
else
    echo "PRZELOGUJ SIE NA ROOTa, wpisz:"
    echo "sudo su"
    exit
fi


# Check domain.

server_ip=`curl -s http://checkip.amazonaws.com`
dns_ip=$(host $domena | grep address | awk 'NR==1{ print $4 }')
#dns_ip=$(host $domena | awk '{ print $4 }')
if [ "$server_ip" = "$dns_ip" ] ; then
    echo "DOMENA OK"
else
    echo "DOMENA NIE OK"
fi


# Server preparation.

apt update --yes

systemctl stop apache
apt remove apache2 --yes
apt install nginx --yes
systemctl enable nginx
systemctl start nginx


# Soft

# Required soft.
apt install curl --yes
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
git clone https://github.com/ZPXD/project_starter.git $projects_folder


# Project.

git clone $project_repo $projects_folder
project_name=$(basename `git rev-parse --show-toplevel`)
project_folder=/$projects_folder/$

# Environment.

venv=$project_folder/$projects_name/$project_namevenv

python3 -m venv $venv
source $venv/bin/activate

export FLASK_APP=app.py
pip3 install -r $project_folder/$projects_name/requirements.txt


# Server files landing.
python3 $project_folder/project_starter/scripts/project_starter.sh $project_folder $project_name $domena 

# Grant user the rights to the project folder.
chown -R $project_user:$project_user $project_folder
systemctl enable $project_name

# Done.
python3 $projects_folder/projects_strater/scripts/banner.py

echo " "
echo "gz"
