# pip install opencv-python
# pip install opencv-contrib-python (for extra modules)
# https://github.com/Saafke/EDSR_Tensorflow/tree/master/models
# download EDSR_x3.pb from above

# This program reads first command line argument, and upscales image by 3x
# using a pretrained model.
# usage: python upscale.py image.jpg

import cv2
from cv2 import dnn_superres
import sys

# Create an SR object
sr = dnn_superres.DnnSuperResImpl_create()

# Read image
image = cv2.imread('./' + sys.argv[1])

# Read the desired model
path = "EDSR_x3.pb"
sr.readModel(path)

# Set the desired model and scale to get correct pre- and post-processing
sr.setModel("edsr", 3)

# Upscale the image
result = sr.upsample(image)

# Save the image
cv2.imwrite("./upscaled.png", result)
