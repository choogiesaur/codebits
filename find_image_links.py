import urllib2, re
source = open('source.txt').read()

for link in re.findall('archives.bulbagarden.net(.*?).png', source):
	print('archives.bulbagarden.net'+link+'.png')
