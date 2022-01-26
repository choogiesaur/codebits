from PIL import Image
import os
import img2pdf
import io

# Collect .tif files in folder
for root, dirs, files in os.walk(".", topdown=False):
    tifs = [os.path.join(root, name) for name in files if name.endswith('.tif')]
print(tifs)

# Open each as a Pillow image
pillow_images = [Image.open(name) for name in tifs]

# Array to store each image, converted to bytes
images_as_bytes = []

for i in range(len(pillow_images)):
    # Make an empty byte array
    byte_array = io.BytesIO()
    
    # Save image to byte array, format PNG
    pillow_images[i].save(byte_array, format='PNG')
    
    # Reassign value to the actual bytes (not stream object)
    byte_array = byte_array.getvalue()
    images_as_bytes.append(byte_array)
    
# Save in-memory image data to PDF. Convert function is called on array of images which will become the PDF pages
with open("name.pdf","wb") as f:
    f.write(img2pdf.convert(images_as_bytes))
