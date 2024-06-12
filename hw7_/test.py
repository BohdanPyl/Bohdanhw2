def lookup_key(d, value):
    return [k for k, v in d.items() if v == value]



dictionary = {'1': 'one', '2': 'one', '3': 'one'}
value_to_find = 'one'
keys = lookup_key(dictionary, value_to_find)
print(keys)