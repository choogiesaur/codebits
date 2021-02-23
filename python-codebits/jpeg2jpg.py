import glob
import os

# Really just a file renamer; needed it for a finicky program that wouldn't accept '.jpeg'
for file in glob.glob('*.jpeg'):
	new_file = file.replace('jpeg', 'jpg')
	os.rename(file, new_file)
