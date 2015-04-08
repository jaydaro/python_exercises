__author__ = 'jay'

def numbers_for_fun():

    first_int = raw_input("Enter your first integer: ")
    while first_int.isdigit() == False:
        first_int = raw_input("This input needs to be an integer. Enter your first integer: ")

    second_int = raw_input("Enter your second integer(cannot be 0): ")

    while second_int.isdigit() == False:
        second_int = raw_input("Your input needs to be an integer. Enter a second integer: ")

    while int(second_int) == 0:
        second_int = raw_input("Your second integer cannot be 0, Enter a second integer that is not 0: ")

    first_int = int(first_int)
    second_int = int(second_int)

    sum_int = first_int + second_int
    difference_int = first_int - second_int
    product_int = first_int * second_int
    quotient_int = first_int / second_int
    remainder_int = first_int % second_int

    print "The sum of %s and %s is %s " % (first_int, second_int, sum_int)
    print "The difference of %s and %s is %s " % (first_int, second_int, difference_int)
    print "The product of %s and %s is %s " % (first_int, second_int, product_int)
    print "The quotient of  %s and %s is %s with remainder %s" % (first_int, second_int, quotient_int, remainder_int)


numbers_for_fun()


