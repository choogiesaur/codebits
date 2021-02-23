from PIL import Image  # Python Image Library - Image Processing\
import glob

# globs through directory for .png files, converts them using PIL (or Pillow) to .jpg
for file in glob.glob("*.png"):
	print file
	im = Image.open(file)
	rgb_im = im.convert('RGB')
	rgb_im.save(file.replace("png", "jpg"), quality=95)
