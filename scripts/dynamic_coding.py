import os
import threading
import time

'''
Dynamic coding example.

This script will create script dynamically and starts it.


Usage:
1. Update files_list - add file paths to files_list or don't and see demonstration.
2. Add something to any of files you are watching (or chante any file in a demonstration 'xd')


ZPXD, Łukasz Pintal.
'''



# Add list of files to watch here.

files_list = [
	# ...
	# ...
]

def generate_files(files_list):
	'''
	If no file paths list given, it will create data for demonstration.
	'''
	if not files_list:
		here = os.getcwd()
		files_folder = here + '/' + 'xd'
		os.mkdir(files_folder)
		for i in range(100):
			path = files_folder + '/' + 'file_wooooah_the_fileee_{}.txt'.format(i)
			with open(path, 'w+') as f:
				f.write(str(i))
		files_list = os.listdir(os.getcwd() + '/xd')
		files_list = [os.getcwd() + '/xd/' + f for f in files_list]
	return files_list

def create_file_watcher(files_list):
	'''
	Creates script that watches for any changes in all files defined by you.
	'''

	guardian_path = os.getcwd() + '/' + 'i_see_my_files.py'

	# Watcher blueprint.
	file_watcher = '''
import os
import threading

def i_see_my_files(file):
	yeah_echo = 0
	while True:
		yeah = os.stat(file).st_mtime
		if yeah_echo != yeah:
			yeah_echo = yeah
			print(file.split('/')[-1], yeah)
	'''

	# Guardian blueprint.
	template = '''
guardian_{} = threading.Thread(target=i_see_my_files, args=['{}'])
guardian_{}.start()
	'''

	# Create guardians.
	for i, name in enumerate(files_list):
		short_name = name.split('/')[-1].split('.')[0]
		item = template.format(str(i), name, str(i))
		file_watcher += item + '\n'

	# Save watcher as a script.
	with open(guardian_path, 'w') as f:
		f.write(file_watcher)

	# All guardians runs in background simultaneously.
	time.sleep(1)
	os.system('python3 {}'.format(guardian_path))
	
	# Use info.
	time.sleep(1)
	print()
	print()
	print('Now change any of files you are watching. (or any in folder /xd )')
	print('You can add a function at the end of watcher to react anytime anything changes.')



if __name__ == '__main__':
	files_list = generate_files(files_list)
	create_file_watcher(files_list)