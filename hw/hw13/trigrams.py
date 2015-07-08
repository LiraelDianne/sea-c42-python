import random


def simplify(lines):
    wordlist = []
    for i in range(len(lines)):
        wordlist.extend(lines[i].split())
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


def make_story(trigrams, word_length):
    start = list(random.choice(list(trigrams.keys())))
    i = 0
    going = True
    while going:
        tup = (start[i], start[i+1])
        if tup in trigrams:
            select = random.randrange(0, len(trigrams[tup]))
            next_word = trigrams[tup][select]
            i = i + 1
            start.append(next_word)
        else:
            i = word_length
        if i == word_length:
            going = False

    story = " ".join(start)
    if story[len(story)-1] == ".":
        return story
    story += "."
    return story


if __name__ == "__main__":
    try:
        f = open('sherlock-small.txt', 'r')
        """for i in range(61):
            f.readline() """
        lines = f.readlines()
        f.close()
    except FileNotFoundError as e:
        print(str(e))

    trigram_dict = make_trigram_dict((simplify(lines)))
    print(make_story(trigram_dict, 100))
