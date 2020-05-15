import pickle
import requests

link = 'http://www.pythonchallenge.com/pc/def/banner.p'
f = requests.get(link)
decoding = pickle.loads(bytearray(f.text, 'utf-8'))
print(decoding)
for element in decoding:
    for subelement in element:
        char, repeat = subelement
        for _ in range(repeat):
            print(char, end='')
    print("\n", end='')

