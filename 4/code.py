import requests
import re

# Get source code
link = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
f = requests.get(link)

# Get pattern for the next url
decoding = re.findall('<a href="linkedlist.php(.+?)">', f.text.replace('\n', ''))
next_url = ''.join((link, *decoding))
print(next_url)

while True:
    f = requests.get(next_url)
    print(f.text)

    if '.html' in f.text:
        match = f.text
        break

    elif f.text == "Yes. Divide by two and keep going.":
        decoding = int(*decoding)
        decoding = [str(int(decoding / 2))]

    else:
        decoding = re.findall('and the next nothing is ([0-9]+)', f.text)

    next_url = ''.join((next_url, *decoding))
    next_url = re.sub('[0-9]+', *decoding, next_url)
    print(next_url)

next_url = link.replace('linkedlist.php', match)
print(next_url)
