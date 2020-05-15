import re
import zipfile

import requests

# Get url
link = "http://www.pythonchallenge.com/pc/def/channel.zip"
f = requests.get(link)

# Download ZIP file
with open('channel.zip', 'wb') as file:
    file.write(f.content)

with zipfile.ZipFile('channel.zip', 'r') as zip_ref:
    next_step = '90052'

    while True:
        next_file = ''.join((next_step, '.txt'))

        # Get zip comment from next file
        encoded = zip_ref.getinfo(next_file).comment
        decoding = encoded.decode('utf-8')
        print(*decoding, end='')
        with zip_ref.open(next_file, 'r') as f:
            content = f.read().decode('utf-8')
            # print(content)
            try:
                decoding = re.findall('Next nothing is ([0-9]+)', content)
                next_step, = decoding
            except ValueError:
                break
