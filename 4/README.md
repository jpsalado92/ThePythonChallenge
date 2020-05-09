# Challenge #4
**Url**: http://www.pythonchallenge.com/pc/def/linkedlist.php<br/>
## Problem Statement
![ChallengePic_1](http://www.pythonchallenge.com/pc/def/chainsaw.jpg)<br/>

## Resolution
The page header states "follow the chain" and the picture shows some kind of mechanism. There is no hint given, so first we check the source code,
we find the following hidden comment:
> urllib may help. DON'T TRY ALL NOTHINGS, since it will never end. 400 times is more than enough.

We can also find that the picture has a link 
>"linkedlist.php?nothing=12345"

Up to here, it looks as if they want is to follow some kind of pace.
We can automate the trail using python just like this: 

```python
import requests
import re

# Get source code
link = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
f = requests.get(link)

# Get pattern for the next url
decoding = re.findall('<a href="linkedlist.php(.+?)">', f.text.replace('\n', ''))
next_url = ''.join((link, *decoding))

# Automating the trail
while True:
    f = requests.get(next_url)
    
    # Stop looking if we find a html pattern    
    if '.html' in f.text:
        match = f.text
        break

    else:
        decoding = re.findall('([0-9]+)', f.text)

    next_url = ''.join((next_url, *decoding))
    next_url = re.sub('[0-9]+', *decoding, next_url)
```

Following the trail, we find some **corner cases**.<br/>
* The first one appears when reaching http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=16044, and it states that we should divide this number by two.<br/>
This is easily handled by including the following code in the loop:
``` python
elif f.text == "Yes. Divide by two and keep going.":
    decoding = int(*decoding)
    decoding = [str(int(decoding / 2))]
```
* The other one appears at http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=82682. The message states that there may appear misleading numbers in the text and that we should only consider those that are preceded by _"and the next nothing is"_<br/>
In order to fix change the pattern in the regular expression:
``` python
decoding = re.findall('and the next nothing is ([0-9]+)', f.text)
```
Finally, we reach http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=66831, that leads us to http://www.pythonchallenge.com/pc/def/peak.html
