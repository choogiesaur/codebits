import urllib2, re

# Ran this on source for page on bulbapedia that had pokemon GBC sprites
source = open('source.txt').read()
for link in re.findall('archives.bulbagarden.net(.*?).png', source):
	print('archives.bulbagarden.net'+link+'.png')
