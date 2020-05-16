# Challenge #11
**Url**: http://www.pythonchallenge.com/pc/return/5808.html
<br/>
## Problem Statement
![ChallengePic_11](cave.jpg)
## Resolution
No hint given, but we can read *'odd even'* at the page header and the image is called *'cave.jpg'*.

Looking closely, the images may seem to be composed of 2 different images, as there are 2 patterns corresponding to even pixels and odd pixels.
In order to retrieve both images, we can implement the following code: 
 
```python
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
```
> ![evil](evil.png)

Which leads us to http://www.pythonchallenge.com/pc/return/evil.html
