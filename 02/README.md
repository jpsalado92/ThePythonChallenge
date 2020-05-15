# Challenge #2
**Url**: http://www.pythonchallenge.com/pc/def/ocr.html
<br/>
## Problem Statement
![ChallengePic_2](http://www.pythonchallenge.com/pc/def/ocr.jpg)
<br/>
**Hint**: recognize the characters. maybe they are in the book, but MAYBE they are in the page source.
## Resolution
The hint leads us to the page source, if we open it, we can read some instructions and see a big mess of characters.

In order to extract it we can use the "request" and "re" modules as follows:
```python
import requests
import re

link = "http://www.pythonchallenge.com/pc/def/ocr.html"
f = requests.get(link)
instructions, mess = re.findall('<!--(.+?)-->', f.text.replace('\n', ''))
print(instructions)
print(mess)
```
> find rare characters in the mess below: <br>
> %%$@_$^__#)^)&!_+]!*@&^}@ [...]

To find those "rare" characters, we can simply use the set() function.
```python
set(mess)
```
> {'$', '}', '%', '!', 'a', '[', '&', '*', '^', 'i', '@', '{', 't', ']', '+', '_', 'u', '(', 'e', ')', 'q', '#', 'l', 'y'}

So, it appears there are some letters among all the special chracters. We can get rid of them using a simple list comprehension.
```python
def decode(c):
    if "a" <= c <= "z":
        return c
    else:
        return ""


decoding = [decode(c) for c in mess]
print(''.join(decoding))
```
> equality

This leads us to: http://www.pythonchallenge.com/pc/def/equality.html
