import os

'''
In case if Flask output print act wierd and you are in a hurry.

cp ?/project_starter/scripts/terminal_print.py where/your/script/is/terminal_print.py

from terminal_print import tp
tp('something')

ZPXD, Łukasz Pintal.
'''

def tp(line):
	with open('output.txt', 'w') as f:
			f.write(line)
			f.write('')
	with open('output.txt', 'r') as f:
		print(f.read())
	os.system('cat output.txt')
	os.system('rm output.txt')
