import requests
import re

link = "http://www.pythonchallenge.com/pc/def/ocr.html"
f = requests.get(link)
instructions, mess = re.findall('<!--(.+?)-->', f.text.replace('\n', ''))
print(instructions)
print(set(mess))


def decode(c):
    if "a" <= c <= "z":
        return c
    else:
        return ""


decoding = [decode(c) for c in mess]
print(''.join(decoding))

