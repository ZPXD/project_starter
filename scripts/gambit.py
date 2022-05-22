import os
import sys
import json
import string
import random

from datetime import datetime



''''
Two hands gambit - living script.


This script data is self-actualising.
Each program run updates program itself.

You use 2 hands gambit when you want to have 
fg. growing / self-actualising config file within your script.

Two hands Gambit - 2 functions to import or copy and paste into your program.


# Demonstration.

git clone https://github.com/ZPXD/project_starter.git
python3 project_starter/scripts/gambit.py


# In action: (just paste it anywhere, it should work ~everywhere where linux, python and git is).

import os
os.system('git clone https://github.com/ZPXD/project_starter.git')

from project_starter.script.gambit import second_hand, first_hand

config = {'a':1,'b':2}

def your_part(data):
    # YOUR PROGRAM HERE - UPDATE config
    import random, string
    random_key = random.choice(string.ascii_lowercase)
    value = len(data.keys()) ** 2
    config[random_key] = value
    return config

if __name__ == "__main__":
    second_hand()
    config = your_part(config)
    fist_hand(config, 'config')


Use with dignity and reason.

ZPXD, Łukasz Pintal.
'''




# 1. Living data. It's crutial how you name it.  You need to pass this name to the gambit.

data = {
    "a": 4,
    "b": 2,
    "z": 9,
    "i": 9,
    "m": 16,
    "l": 25,
}

program_path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


# 2. Program body. This is the part of the program. It could be 1 or 10000 lines.


# YOUR CODE GOES HERE. THIS IS EXAMPLE.

def add_value(data):
	random_key = random.choice(string.ascii_lowercase)
	value = len(data.keys()) ** 2
	data[random_key] = value
	return data


# ...


# 3. Two gambit functions. One to run before your script and one to run after it.


def first_hand(living_data=None, living_data_name='data'):
	'''
	Creates copy of script where you use it but with actualised data.

	living_data: dict
	'''

	# Hands.
	first_hand = program_path + '/' + sys.argv[0].split('/')[-1]
	second_hand = first_hand.replace(sys.argv[0].split('/')[-1], 'second_hand_{}'.format(sys.argv[0].split('/')[-1]))

	# Hide second hand.
	if 'second_hand' in os.listdir():
		os.system('rm {}'.format(second_hand))
	
	# Move script to second hand.
	with open(first_hand, 'r') as woah:
		this_file = woah.readlines()
		new_file = ''
		data_part, done = False, False
		for line in this_file:
			if line.startswith(living_data_name) and not done:
				data_part = True
			if line.startswith('}') and not done:
				data_part = False
				done = True
				data_string = json.dumps(living_data, indent=4)[:-1]
				new_file += living_data_name + ' = ' +  data_string
			if not data_part:
				new_file += line
		with open(second_hand, 'w') as temp:
			temp.write(new_file)

	# Move second hand.
	os.system('python3 {}'.format(second_hand))

def second_hand():
	'''
	Move updated script back to first hand.
	'''

	# Hands.
	second_hand = program_path + '/' + sys.argv[0].split('/')[-1]
	first_hand = second_hand.replace('second_hand_', '')

	# Move script from second hand back to first.
	if 'second_hand' in sys.argv[0]:
		os.system('cp {} {}'.format(second_hand, first_hand))
		os.system('rm {}'.format(second_hand))
		sys.exit(0)


# 4. Sequence. Second hand -> your program -> first hand.

if __name__ == '__main__':
	second_hand()
	data = add_value(data)
	first_hand(data, 'data')