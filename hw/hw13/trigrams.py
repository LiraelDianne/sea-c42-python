import random


def simplify(lines):
    # turn a list of lines into a list of words
    wordlist = []
    for i in range(len(lines)):
        wordlist.extend(lines[i].split())
    return wordlist


def make_trigram_dict(words):
    # turn a list of words into a trigram dictionary
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
    """ Pick a random pair of words from the trigram dictionary
    and return a story of length word_length """
    start = list(random.choice(list(trigrams.keys())))
    i = 0
    going = True
    while going:
        # read the last two words in the start list
        tup = (start[i], start[i+1])
        if tup in trigrams:
            # find a word that can follow the last two words
            select = random.randrange(0, len(trigrams[tup]))
            next_word = trigrams[tup][select]
            i = i + 1
            start.append(next_word)
        else:
            # stop loop if no trigram is found
            i = word_length
        if i == word_length:
            # stop loop when story is long enough
            going = False

    # join the word list with spaces and add a period if needed
    story = " ".join(start)
    if story[len(story)-1] == ".":
        return story
    story += "."
    return story


if __name__ == "__main__":
    try:
        f = open('sherlock.txt', 'r')
        for i in range(61):
            f.readline()
        lines = f.readlines()
        f.close()
    except FileNotFoundError as e:
        print(str(e))

    trigram_dict = make_trigram_dict((simplify(lines)))
    print(make_story(trigram_dict, 400))
