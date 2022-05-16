import os
import sys
import requests
import webbrowser


'''
docs.py


Gets list of all libraries (imported by "import") in python file.
Display list of links to libraries documentations (or to google search).
Option: open all documentations in browser new window for you. 

Use it wisely.


ZPXD, Łukasz Pintal
'''



source = 'http://www.pykruter.pl/czytaj_dokumentacje_bo_madre_sa_i_przydatne'
google_search_url = "www.google.com/search?q={}+documentation+python"



def get_mapping_from_source(source):
	'''
	Get mapping of libraries documentations links to libraries names.
	'''
	try:
		mapping = requests.get(source).json()
	except:
		mapping = {}
	return mapping

def list_libraries(python_file_path):
	'''
	Opens Python file by a file path and gets list of all used libraries (their names).
	'''
	python_file = open(python_file_path).readlines()
	libraries = []
	for line in python_file:
		if 'import' in line:
			line = line.split()
			if line[0] == 'from':
				library = line[1]
			elif line[0] == 'import':
				library = line[1]
			if '.' in library:
				library = library.split('.')[0]
			library = library.lower()
			libraries.append(library)

	libraries = list(set(libraries))
	return libraries

def get_documentations_for_libraries(libraries):
	'''
	For each library gets either link to it's documentation or 
	propose a google search link to find it yourself.
	'''
	mapping = get_mapping_from_source(source)
	print(mapping.keys())
	library_info = {}
	for library in libraries:
		if library in mapping.keys():
			documentation_url = mapping[library]
			# TBD - versions, info, checks.
			# ...
		else:
			documentation_url = google_search_url.format(library)
			# TBD - versions, info, checks.
			# ...
		library_info[library] = {}
		library_info[library]['documentation_url'] = documentation_url
	return library_info


def display_libraries_info(library_info):
	'''
	Shows info about libraries and links to their doc's in terminal.
	'''
	
	info_template = "{:30} {}"
	for library in library_info.keys():
		documentation_url = library_info[library]['documentation_url']
		line_with_info = info_template.format(library, documentation_url)
		print(line_with_info)
	
def open_documentations_in_browser(library_info):
	'''
	Opens all libraries documentation url's (or google search placeholders) in
	'''
	print()
	open_documentations = input('This is experimental part. Press [y] + [enter] to open all documentations in new browser window.')
	open_new_window = 0
	if open_documentations.lower() == "y":
		for library in library_info.keys():
			documentation_url = library_info[library]['documentation_url']
			try:
				if open_new_window != 1:
					webbrowser.open(documentation_url, new=1)
					open_new_window = 1
				else:
					webbrowser.open(documentation_url, new=2)

			except:
				print()
				print("Can't open documentations in browser, open them yourself :)")

def read_the_docs(python_file_path):
	'''
	Main.
	'''

	# Get info.
	libraries = list_libraries(python_file_path)
	library_info = get_documentations_for_libraries(libraries)

	# Display info.
	display_libraries_info(library_info)

	# Open documentations.
	open_documentations_in_browser(library_info)



if __name__ == "__main__":

	if len(sys.argv) == 2:
		python_file_path = sys.argv[1]
	else:
		print('Usage:\n')
		print('python3 docs.py /path/to/python/script.py')
		sys.exit(0)

	read_the_docs(python_file_path)