# Challenge #8
**Url**: http://www.pythonchallenge.com/pc/def/oxygen.html
<br/>
## Problem Statement
![ChallengePic_8](http://www.pythonchallenge.com/pc/def/integrity.jpg)
<br/>

## Resolution
This was pretty hard to figure out, the heading states "working hard?" and you see a bee. Also, there if you click in the bee, it leads you to, possibly, the next challenge. However, you need some credentials to get in there.
<br/>
If you check the page source, you find some 'un' and 'pw' fields in the hint, so those might be the credentials, but they seem kind of encoded right? Well, to handle this, the creators of the challenge wanted you to think like this:
Working hard? Bees are busy too!, which leads to Bz2, which is a compressing format. The headers of the 'un' and 'pw' fields could also be a good hint.
 
```python
import bz2

un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

print(bz2.decompress(un))
print(bz2.decompress(pw))
```
>b'huge'<br/>
b'file'

Which leads us to the next challenge in http://www.pythonchallenge.com/pc/return/good.html
