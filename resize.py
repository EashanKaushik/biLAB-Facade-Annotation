from PIL import Image
import os

CURRENT_DIR = os.getcwd()
IMAGE_DIR = os.path.join(CURRENT_DIR, "images")

RESIZED_IMAGE = os.path.join(CURRENT_DIR, "resized_images")

if os.path.isdir(RESIZED_IMAGE):
    os.rmdir(RESIZED_IMAGE)

os.mkdir(RESIZED_IMAGE)

for image_path in os.listdir(IMAGE_DIR):
    image = Image.open(os.path.join(IMAGE_DIR, image_path))
    image = image.resize((1024, 1024), Image.ANTIALIAS)
    image.save(fp=os.path.join(RESIZED_IMAGE, image_path))
