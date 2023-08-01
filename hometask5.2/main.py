source = "AaawcatawrwefWXR   X1Reshraetcva6u23bcabcdfghj"
thedict = {
}

for char in source:
    x = source.count(char)
    thedict[char] = 0 + x

thedict = sorted(thedict.items())

for tup in thedict:
    print(f'{tup[0]}, {tup[1]}')
