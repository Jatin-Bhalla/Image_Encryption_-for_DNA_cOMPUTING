import numpy as np
from PIL import Image
#python imaging library :PIL
#np is used to create arrays and perform numerical operations.
#PIL is used to read the image file.numpy
img = np.array(Image.open("satellite.jpg"))
print(img)
