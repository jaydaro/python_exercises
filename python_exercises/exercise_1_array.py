__author__ = 'jay'
'''
This is a little program that will ask the user for some
numbers, then manipulate them and print the result.
'''
# this function creates an array of the users numbers,
def numbers_for_fun():
    # declare vars here
    number_array = []
    i = 0
    t = 1
    sum_int = 0
    product_int = 1

    #start the program and input the #ammount of numbers to play with
    print "*" * 50
    print "         Fun With Numbers!"
    print ""
    array_length = int(raw_input("How many numbers do you want to play with? "))
    #check the number and prompt to choose a number between 2 and 5
    while array_length < 2 or array_length > 5:
        print "*" * 50
        print "Hmmmm ... let's just play with 2 to 5 numbers."
        array_length = int(raw_input('So, how many numbers? '))

    #this is where the ints get put in the array
    while i < array_length:

        number_array += raw_input("Enter your integer #%i : " % t)
        # check if the input is a number
        while number_array[i].isdigit() == False:
            number_array[i] = raw_input("This input needs to be an integer. Enter your integer #%i : " % t)
        # check if the input is a zero
        while int(number_array[i]) == 0 and i == 1:
            number_array[i] = raw_input("You can't divide by 0, Enter another integer that is not 0: ")
        i += 1
        t += 1
    #Ask what the user wants to do with the numbers
    print "*" * 50
    print ""
    print "Great! Now, what should we do with the numbers?"
    print "To get the sum enter 1"
    print "To get the product enter 2"
    print "To get the average enter 3"
    print "*" * 50
    print ""
    number_choice = int(raw_input("So, what will it be? "))

    #Print out the sum
    if number_choice == 1:
        for x in number_array:
            sum_int += int(x)
        print "The sum of your numbers is %i " % sum_int

    #print out the product
    elif number_choice == 2:
        for x in number_array:
            product_int *= int(x)
        print "The product of your numbers is %i " % product_int

    #print out the average
    elif number_choice == 3:
        for x in number_array:
            sum_int += int(x)
        average_int = sum_int / array_length
        print "The average of your numbers is %i " % average_int

    #exit with out doing anything
    else:
        print "I guess you don't want to play."


numbers_for_fun()