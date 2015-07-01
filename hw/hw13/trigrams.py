try:
    f = open('sherlock-small.txt', 'r')
    lines = f.readlines()
    f.close()
except FileNotFoundError as e:
    print(str(e))

words = lines[0].split()

d = {}
for (i, word) in enumerate(words):
    if i < (len(words)-2):
        d[(words[i], words[i+1])] = words[i+2]

start = [words[0], words[1]]
si = 0
going = True
while going:
    if si == (len(words)-3):
        going = False
    tup = (start[si], start[si+1])
    next_word = d[tup]
    si = si + 1
    start.append(next_word)

print(start)

'''
import random

d = {('pick', 'three'):['words', 'clocks']}
print(d[('pick', 'three')])
ri = random.randint(0, len(d['pick', 'three']))
next_word = d[('pick', 'three')][ri]
print(next_word)
'''
