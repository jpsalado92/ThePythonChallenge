# Challenge #10
**Url**: http://www.pythonchallenge.com/pc/return/bull.html
<br/>
## Problem Statement
![ChallengePic_10](bull.jpg)
## Resolution
The hint states the following
>len(a[30]) = ?

Also, if we click at the bull/cow, we can a list named "a"
> a = [1, 11, 21, 1211, 111221, 
 
This seems to be some kind of sequence, with a little bit of research, you can determine that this is a **look&say sequence**.

In order to find the solution, which would be the length of the 30th number of the sequence, we can implement the following: 

 
```python
import re

a = ['1']
for n in range(31):
    last_element = a[-1]
    buffer = []

    groups = re.findall(r"((.)\2*)", last_element)

    for group, _ in groups:
        element_count = last_element.count(group)
        buffer.append(str(len(group)))
        buffer.append(group[0])

    a.append(''.join(buffer))
    print("Round: {}".format(n))
    print(last_element)
    print("Len of element in sequence: {}".format(len(last_element)), end='\n\n')
```
> Round: 29<br/>
> 3113112221131112311332111213122112 [...]<br/>
> Len of element in sequence: 4462<br/>
><br/>
> Round: 30<br/>
> 1321132132211331121321231231121113 [...]<br/>
> Len of element in sequence: **5808**<br/>

Which leads us to http://www.pythonchallenge.com/pc/return/5808.html
