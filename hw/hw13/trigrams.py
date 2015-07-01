import random

try:
    f = open('sherlock-small.txt', 'r')
    lines = f.readlines()
    f.close()
except FileNotFoundError as e:
    print(str(e))

d = {}

for i in range(len(lines)):
    words = lines[i-1].split()

    for (i, word) in enumerate(words):
        if i < (len(words)-2):
            tup = (words[i], words[i+1])
            if tup in d:
                d[tup].append(words[i+2])
            else:
                d[tup] = [words[i+2]]

start = [words[0], words[1]]
si = 0
going = True
while going:
    if si == (len(words)-3):
        going = False
    tup = (start[si], start[si+1])
    print(tup)
    print(d[tup])
    ri = random.randrange(0, len(d[tup]))
    print(ri)
    next_word = d[tup][ri]
    si = si + 1
    start.append(next_word)

sentence = " ".join(start)
print(sentence)
