import requests
import re

link = "http://www.pythonchallenge.com/pc/def/equality.html"
f = requests.get(link)
mess = re.findall('<!--(.+?)-->', f.text.replace('\n', ''))
print(mess)

match = "".join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', *mess))
print(match)