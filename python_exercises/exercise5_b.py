import string
import operator


def exercise5_b():
    with open('exercise5_b.txt', 'r+') as f:
        # Read file and assign contents to str variable 'text'
        text = f.read()
        text = text.lower()
    # Remove punctuation and split into separate words
    new_text = text.translate(None, string.punctuation)
    words = new_text.split()

    words_dict = {}
    for i in words:
        # This is where the words are counted and the dict of # of words is made
        if i in words_dict.keys():
            words_dict[i] += 1
        else:
            words_dict[i] = 1

    words_sorted = sorted(words_dict.items(), key=operator.itemgetter(1), reverse=True)
    # Sort the words, from most to least frequent

    x = 0
    for i in words_sorted:
        # format the output to be more readable.
        x += 1
        if x % 10 == 0 or len(words_sorted) - x is 0:
            print str(i) + "\n"
        else:
            print i,


    # print words_sorted
    print "Total number of different words: ", len(words_sorted)


exercise5_b()