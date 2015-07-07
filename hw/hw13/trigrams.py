import random

try:
    f = open('sherlock-small.txt', 'r')
    for i in range(61):
        f.readline()
    lines = f.readlines()
    f.close()
except FileNotFoundError as e:
    print(str(e))


def simplify(lines):
    wordlist = []
    for i in range(len(lines)):
        wordlist.append(lines[i-1].split())
    return wordlist


def make_trigram_dict(words):
    d = {}
    for (i, word) in enumerate(words):
        if i < (len(words)-2):
            tup = (words[i], words[i+1])
            if tup in d:
                d[tup].append(words[i+2])
            else:
                d[tup] = [words[i+2]]
    return d


def make_story(trigrams, story_length):
    start = list(random.choice(list(trigrams.keys())))
    si = 0
    going = True
    while going:
        if si == story_length:
            going = False
        tup = (start[si], start[si+1])
        select = random.randrange(0, len(trigrams[tup]))
        next_word = trigrams[tup][select]
        si = si + 1
        start.append(next_word)

    story = " ".join(start)
    return story
