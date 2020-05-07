CODE = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb " \
       "rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "


def approach1():
    decode_keys = {'k': 'm', 'o': 'q', 'e': 'g'}

    def key_to_value(c, map_dict):
        if c in map_dict:
            return map_dict[c]
        else:
            return c

    # Possible solution using list comprehension
    dec_list = [key_to_value(c, decode_keys) for c in CODE]
    decoding = ''.join(dec_list)
    print(decoding)

    # Yet another possible solution using list comprehension
    dec_mapping = map(lambda p: key_to_value(p, decode_keys), CODE)
    decoding = ''.join(dec_mapping)
    print(decoding)


def approach2():
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


if __name__ == '__main__':
    approach2()




