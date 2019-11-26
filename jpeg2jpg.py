import glob
import os

for file in glob.glob('*.jpeg'):
	new_file = file.replace('jpeg', 'jpg')
	os.rename(file, new_file)
	