import csv
from sand_file import *
import datetime
import time

def read_all(filename):
	all_files={}
	f_read = csv.reader(open(filename), delimiter = '|')
	for line in f_read:
		file_path = line[1]
		if file_path in all_files:
			all_files[file_path].add_data(line)
		else:
			all_files[file_path] = Sand_file(line)
	return all_files

all = read_all('soft_sys_sandbox.txt')
print all[all.keys()[0]].size
print all[all.keys()[0]].date
print all[all.keys()[0]].date_modified

