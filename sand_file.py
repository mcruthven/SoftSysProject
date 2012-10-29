from time import *

class Sand_file(object):
	def get_attrs(self):
		return [('date', str),
			('path_name', str), 
			('protection_bits', str), 
			('inode_number', int), 
			('hard_links', int), 
			('user_ID', str), 
			('group_ID', str), 
			('date_created', float) , 
			('date_modified', float), 
			('date_accessed', float), 
			('size', int)]

	def __init__(self, info):
		""" takes in info, a list of blah, blah, and blah """
		attrs = self.get_attrs()
		for i, part in enumerate(info):
			cast = attrs[i][1]
			if i in [0, 8, 9, 10]:
				setattr(self, attrs[i][0], [cast(part)])
			else:
				setattr(self,attrs[i][0],cast(part))

	def add_data(self, info):
		attrs = self.get_attrs()
		self.date.append(info[0])
		self.date_modified.append(info[-3])
		self.date_accessed.append(info[-2])
		self.size.append(info[-1])
		