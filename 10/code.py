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
