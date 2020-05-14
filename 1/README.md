# Challenge #1
**Url**: http://www.pythonchallenge.com/pc/def/map.html
<br/>
## Problem Statement
![ChallengePic_1](http://www.pythonchallenge.com/pc/def/map.jpg)
<br/>
**Hint**: Everybody thinks twice before solving this.<br/>
```python
CODE = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"
```
## Resolution
### Approach 1
At first, it may seem as if they want us to convert every character of the "code" following the values
(M, Q, G) to every key (K, O, E).

```python
decode_keys = {'k': 'm', 'o': 'q', 'e': 'g'}

def key_to_value(c, map_dict):
    if c in map_dict:
        return map_dict[c]
    else:
        return c

dec_list = [key_to_value(c, decode_keys) for c in CODE]
decoding = ''.join(dec_list)
print(decoding)
```

> "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr ammnsrcpq ypc dmp. bmglg gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmlg. sqglg qrpglg.myicrpylq() gq pcammmclbcb. lmu ynnjw ml rfc spj."


If we do this, the result remains ilegible, so it looks as if we should try another approach.


### Approach 2

Every key is displaced 2 positions from its value, so maybe we should displace every letter on the string 2 positions.
```python
def key_to_value(c):
    if c not in (' ', '.', "'", '(', ')'):
        decoded_c = ord(c) + 2
        decoded_c = decoded_c - 26 if decoded_c > 122 else decoded_c
        return chr(decoded_c)
    else:
        return c

dec_mapping = map(key_to_value, CODE)
decoding = ''.join(dec_mapping)
print(decoding)
```
> i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url. 

If the same function is applied to the last part of the url we get:
> ocr

This leads us to: http://www.pythonchallenge.com/pc/def/ocr.html

