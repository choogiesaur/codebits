from pprint import pprint

# Take a text file with lines in the format:
# <key>|<val>
# and generate a dictionary using the key-val pairs

with open('pokemon_links.txt') as f:
	link_dict = {}
	for line in f:
		(key, val) = line.split('|')
		link_dict[key] = val

	pprint(link_dict)
