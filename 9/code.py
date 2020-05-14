import re

import matplotlib.pyplot as plt
import requests
from requests.auth import HTTPBasicAuth

url = 'http://www.pythonchallenge.com/pc/return/good.html'
data = requests.get(url, auth=HTTPBasicAuth('huge', 'file')).content.decode()
match = re.search(r'first:\n([\d,\n]+)\n\nsecond:\n([\d,\n]+)\n\n-->', data)
first, second = [match.group(i).replace('\n', '').split(',') for i in [1, 2]]

first = list(map(int, first))
second = list(map(int, second))

union = first + second
x_vals = union[::2]
y_vals = union[1::2]

plt.plot(x_vals, y_vals)
plt.show()
