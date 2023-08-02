import re

num = int(input("How many strings would you enter (from 1 to 9): "))

if 1 > num:
    exit(["Not enough"])
elif num > 9:
    exit(["Too many strings"])

txt = ""

for i in range(0, num):
    txt += str(input()) + " "

raw = re.split(r'\W+', txt)
raw.remove("")
thedict = {
}

for el in raw:
    x = raw.count(el)
    thedict[el] = 0 + x

words = [(v, k) for k, v in thedict.items()]
words1 = sorted(words, reverse=True)

for tup in words1:
    print(f'{tup[1]} {tup[0]}')
