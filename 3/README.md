# Challenge #2
**Url**: http://www.pythonchallenge.com/pc/def/equality.html<br/>
## Problem Statement
![ChallengePic_1](http://www.pythonchallenge.com/pc/def/bodyguard.jpg)<br/>
**Hint**: One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.

## Resolution
There isn't much information showing, but if we check the page source just as in the previous example, we can find again another code chunk. 
In order to extract it we can use the "request" and "re" modules as follows:
```python
import requests
import re

link = "http://www.pythonchallenge.com/pc/def/equality.html"
f = requests.get(link)
mess = re.findall('<!--(.+?)-->', f.text.replace('\n', ''))
print(mess)
```
> kAewtloYgcFQaJNhHVGxXDiQmzjfcpYbzxlWrV [...]

Also, the page header says "re", so the solution is possibly related to regular expresions. 
We will first try finding a pattern in which one lower case letter is surrounded by exactly 3 upper case letters in each side.

```python
match = "".join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', *mess))
print(match)
```
> 'linkedlist'

This leads us to: http://www.pythonchallenge.com/pc/def/linkedlist.html




