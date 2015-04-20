def first_function(new_file):
    try:
        with open(new_file, 'r') as f:
            print f.read()
    except IOError:
        print "'{}' is a file that does not exist! This is handled in the first function".format(new_file)


def second_function(new_file):
    with open(new_file, 'r') as f:
        print f.read()

file_name = ""


file_name = "BobsBurgers.txt"
try:
    first_function(file_name)
    second_function(file_name)
except IOError:
    print "The '{}' file does not seem exist! This is handled in the main script.".format(file_name)