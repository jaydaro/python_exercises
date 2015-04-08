__author__ = 'jay'

first_int = int(raw_input("Enter your first integer: "))
second_int = int(raw_input("Enter your second integer: "))

sum_int = first_int + second_int
difference_int = first_int - second_int
product_int = first_int * second_int
quotient_int = first_int / second_int
remainder_int = first_int % second_int

print "The sum of %s and %s is %s " % (first_int, second_int, sum_int)
print "The difference of %s and %s is %s " % (first_int, second_int, difference_int)
print "The product of %s and %s is %s " % (first_int, second_int, sum_int)
print "The quotient of  %s and %s is %s with remainder %s" % (first_int, second_int, quotient_int, remainder_int)


