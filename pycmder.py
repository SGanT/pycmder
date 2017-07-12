#!/usr/bin/python
import sh
import json
import argparse

parser = argparse.ArgumentParser(description='Tool which executes specific commands in directories')
parser.add_argument('path', action='store', help='Path to JSON file, which contains specific data')
JSON_file = parser.parse_args().path

file = open(JSON_file, 'r')
data = file.read()
json = json.loads(data)

def wrapper(func, *args):
	func(*args)

for path in json:
	print('\n    * Moving to ' + path['path'] + '\n')
	sh.cd(path['path'])
	method = getattr(sh, path['util'])

	files = ''
	for arg in path['args']:
		arg = arg.strip();
		if len(path['flags']) > 0:
			wrapper(method, arg, path['flags'])
		else:
			method(arg)
		print('\n    * Executed '+path['util'] +' '+arg+' \n')
