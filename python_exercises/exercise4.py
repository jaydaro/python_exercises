__author__ = 'jay'


def validate_float(user_float):
    # return True if the input is a float
    try:
        float(user_float)
        return True
    except ValueError:
        return False


def validate_for_zero(user_float):
    if float(user_float) <= 0.0:
        # return True if the int is <= 0
        return True
    else:
        return False

def menu():
    user_choice = 0

    print "*!" * 20
    print ""
    print "     Welcome To The Exercise 4 Menu"
    print ""
    print "*!" * 20
    # print ""
    print "     What would you like to do?"
    #print ""
    print "     1. Write input to file"
    # print ""
    print "     2. Write input to screen"
    #print ""
    print "     3. Quit"
    # print ""
    print "*!" * 20
    print ""

    while user_choice is not 3:
        user_choice = raw_input("     Enter your choice [1-3] : ")
        if user_choice is "1":
            write_to_file = raw_input("Enter a phrase: ")
            with open('exercise4.txt', 'w+') as f:
                new_file = f.write(write_to_file)
        elif user_choice is "2":
            write_to_screen = raw_input("     Enter something to print out to the screen: ")
            print write_to_screen
        else:
            print "Ok, see ya!"
            break



menu()