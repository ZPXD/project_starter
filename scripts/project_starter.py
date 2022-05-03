import os
import sys


def create_nginx_and_gunicorn_files(projects_folder, project_name, domain):
	'''
	Creates both nginx and gunicorn files for domain and aplication.

	Starts it.
	'''

	# CHECK 1 - Projects present.
	
	print(projects_folder, project_name, domain)
	pf_files = os.listdir(projects_folder)
	if 'project_starter' in pf_files and project_name in pf_files:
		pass
	else:
		print('No project_starter and/or no project in projects folder.')
		print()
		print('git clone https://github.com/ZPXD/project_starter.git {}'.format(projects_folder))
		print('git clone <project.git> {}'.format(projects_folder))
		print()
		print('Replace <project.git> with project git.')


	# CHECK 2 - Project name.

	if ' ' in project_name:
		print('Your project has space in name. Change repository name or press whateva and good luck.')
		whateva = input('Write "whateva" and press enter to continue or any other keys to rename project:')
		if whateva != 'whateva':
			sys.exit(0)


	# Nginx file landing:
	
	nginx_file = ''
	nginx_file_template = os.path.join(projects_folder, 'project_starter', 'server_files', 'simple_nginx_file')
	nginx_file_template = open(nginx_file_template).readlines()
	for line in nginx_file_template:
		l = line.strip()
		if l.startswith('server_name'):
			line = line.replace('DOMAIN', project)
		if l.startswith('root') or l.startswith('proxy_pass'):
			line = line.replace('PROJECT_NAME', project_name)
		nginx_file += line + '\n'

	with open("/etc/nginx/sites-available/{}".format(domain), "w") as f:
		f.write(nginx_file)
	
	os.system('sudo ln -s /etc/nginx/sites-available/{} /etc/nginx/sites-enabled/'.format(domain))


	# Paths.
	
	project_path = os.path.join(projects_folder, project_name)
	project_venv_path = os.path.join(project_path, '{}venv'.format(project_name) )

	# Gunicorn file landing.

	# Side note: gunicorn file is quite crazy now. To be upgraded. (But it runs.)
	
	gunicorn_file = ''
	gunicorn_file_template = os.path.join(projects_folder, 'project_starter', 'server_files', 'simple_gunicorn_file')
	gunicorn_file_template = open(gunicorn_file_template).readlines() 
	for l in gunicorn_file_template:
		if l.startswith('User'):
			l = 'User=root'
		elif l.startswith('WorkingDirectory'):
			l = 'WorkingDirectory={}'.format(project_path)
		elif l.startswith('Environment'):
			l = 'Environment="PATH={}/bin"'.format(project_venv_path)
		elif l.startswith('ExecStart'):
			l = 'ExecStart={}/bin/gunicorn --workers 3 --bind unix:{}.sock -m 007 app:app'.format(project_venv_path, project_name)
		gunicorn_file += l + '\n'
		
	where_it_needs_to_be = '/etc/systemd/system/{}.service'.format(project_name)
	with open(where_it_needs_to_be, "w") as f:
		f.write(gunicorn_file)
	
	print(where_it_needs_to_be, where_it_needs_to_be)
	
	# Start it.
	
	os.system('systemctl daemon-reload')
	os.system('systemctl start {}.service'.format(project_name))
	os.system('systemctl restart nginx')
	# rly?


if __name__ == '__main__':

	if len(sys.argv) == 4:
		projects_folder = sys.argv[1]
		project_name = sys.argv[2]
		domain = sys.argv[3]
		create_nginx_and_gunicorn_files(projects_folder, project_name, domain)
		print('kk done')
