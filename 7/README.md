# Challenge #7
**Url**: http://www.pythonchallenge.com/pc/def/oxygen.html
<br/>
## Problem Statement
![ChallengePic_7](http://www.pythonchallenge.com/pc/def/oxygen.png)
<br/>

## Resolution
There is no hint given, but the page header states *'smarty'*, and the picture shows some kind of stream with a strange pixel row inside of it. <br>
If we check the page source, there are no additional clues, so this might have something to do with the gray row inside the picture.<br/>
In order to check what that grayscale row is about, first, we will download the image and analyze it using numpy:
```python
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
```
Using some open-source software like GIMP, we can find that the image has about 95 files of pixels, and that the grayscale message is repeated from about row 45 to row 50. Also, every block is repeated around every 7 columns. Note that grayscale pixels have the same value for the first, second, and third image depth components. <br>
Implementing the following code, we can translate this message according to the ascii table:
```python
# Decoding grayscale message
encoding = []
for n, col in enumerate(image_array[50]):
    d1, d2, d3, _ = col
    if d1 == d2 == d3 and (not n % 7):
        encoding.append(d1)
print(''.join([chr(c) for c in encoding]))
```
> smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]

Applying the same logic again:
```python
# Decoding second message
encoding = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print(''.join([chr(c) for c in encoding]))
```
> integrity

Which leads us to the next challenge in http://www.pythonchallenge.com/pc/def/integrity.html