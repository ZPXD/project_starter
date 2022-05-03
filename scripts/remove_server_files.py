import os

def remove_files(project_name, domain):
    os.system('sudo rm /etc/nginx/sites-available/{}'.format(domain))
    os.system('sudo rm /etc/nginx/sites-enabled/{}'.format(domain)
    os.system('sudo rm /etc/systemd/system/{}.service'.format(project_name))

if __name__ == '__main__':
    if len(sys.argv) == 3:
        project_name = sys.argv[1]
        project_name = sys.argv[2]
        remove_files(project_name, domain)
        print('done')
