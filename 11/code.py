from PIL import Image
import numpy as np

png = Image.open('cave.jpg')
org_image = np.array(png)

image_1 = np.empty((480, 640, 3), dtype=np.uint8)
image_2 = image_1.copy()

for n1, row in enumerate(org_image):
    for n2, pixel in enumerate(row):
        if (n1 + n2) % 2 == 0:
            image_1[n1, n2] = pixel
        else:
            image_2[n1, n2] = pixel

image_1 = Image.fromarray(image_1)
image_1.show()

image_2 = Image.fromarray(image_2)
image_2.show()
