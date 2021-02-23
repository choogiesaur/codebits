from PIL import Image

# Resize specified PNG file to 256x256 using Python Imaging Library
def resize_png(file_name):
	im = Image.open(file_name)
	
	newsize = (256, 256)
	im2 = im.resize(newsize)
	im2.save(file_name)

resize_png('temp.png')
