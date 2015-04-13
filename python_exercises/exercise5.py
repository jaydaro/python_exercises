import string
import random


def random_string_generator():
    # This will create a random string, of random size, within a range on #'s
    # The string is made up of numbers, upper and lowercase characters
    size = random.randint(500, 5000)
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))


def how_many(text):
    # First initialize a dictionary of letters and numbers = 0
    chars2 = string.ascii_uppercase + string.ascii_lowercase + string.digits
    chars_dict = {}
    for i in range(0, len(chars2)):
        chars_dict[chars2[i]] = 0

    for character in text:
        # Populate the dictionary with number of
        # each character in the random string
        # return dictionary
        chars_dict[character] += 1
    dict_list = []
    for key, value in chars_dict.items():
        if value is not 0:
            temp = str(key) + " ==> " + str(value)
            dict_list.append(temp)
    dict_list = sorted(dict_list)
    return dict_list


def exercise5():
    i = 0
    while i < 10:
        # Write 10 random strings to file.
        # Each string is on a new line
        new_random = random_string_generator()
        with open('exercise5.dat', 'a+') as f:
            f.write(new_random + '\n')
        i += 1

    with open('exercise5.dat', 'r+') as f:
        # Read file and assign contents to str variable 'text'
        text = f.readlines()

    for random_string in text:
        # Send random number to how_many().
        random_string = random_string.strip('\n')
        how_many(random_string)
        formatted_random_string = '\n'.join(random_string[x:x + 120] for x in xrange(0, len(random_string), 120))
        print '\n' + formatted_random_string
        dict_list = how_many(random_string)
        x = 0



exercise5()