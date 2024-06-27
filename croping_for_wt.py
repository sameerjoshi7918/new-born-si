import os
from PIL import Image

im = Image.open(r"images\myfirst.png")
im.show()
left = 1
top = 2
right = 512
bottom = 700
im1 = im.crop((left, top, right, bottom))
if os.path.exists(r'images\cropped_myfirst.png'):
    os.remove(r'images\cropped_myfirst.png')
    im1.save(r'images\cropped_myfirst.png')
else:
    im1.save(r'images\cropped_myfirst.png')
im1.show()
