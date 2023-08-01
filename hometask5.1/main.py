dict1 = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5
}

dict2 = {
    'a': 1,
    'b': 2,
    'g': 33,
    'h': 44,
    'e': 55
}

output = ""

for key1 in dict1.keys():
    for key2 in dict2.keys():
        if key2 == key1:
            output += key1 + " "

print(output.rstrip())
