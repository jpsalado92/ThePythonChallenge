import requests
from PIL import Image
import numpy as np

# Image URL
link = "http://www.pythonchallenge.com/pc/def/oxygen.png"

# Download Image
f = requests.get(link)
with open('oxygen.png', 'wb') as file:
    file.write(f.content)

# Get image as numpy array
png = Image.open('oxygen.png')
image_array = np.array(png)

# Decoding grayscale message
encoding = []
for n, col in enumerate(image_array[50]):
    d1, d2, d3, _ = col
    if d1 == d2 == d3 and (not n % 7):
        encoding.append(d1)
print(''.join([chr(c) for c in encoding]))

# Decoding second message
encoding = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print(''.join([chr(c) for c in encoding]))
