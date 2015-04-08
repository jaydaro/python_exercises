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


def gasoline_info():
    gallons = raw_input("Please enter the number of gallons of gasoline: ")

    while validate_float(gallons) is False or validate_for_zero(gallons):
        gallons = raw_input("There is no point in checking 0 or less gallons, please enter a positive number: ")

    gallons = float(gallons)
    liters = float(gallons * 3.7854)
    barrels = gallons / 19.5
    co2_produced = gallons * 20.0
    ethanol = (gallons * 115000.0) / 75700.0
    price = gallons * 4.0

    print "=" * 40
    print "Original number of gallons %.2f" % gallons
    print "=" * 40
    print "%.2f gallons is the equivalent of %.2f liters" % (gallons, liters)
    print "%.2f gallons gallons of gasoline requires %.2f barrels of oil" % (gallons, barrels)
    print "%.2f gallons produces %.2f pounds of co2" % (gallons, co2_produced)
    print "%.2f gallons of gasoline is the energy equivalent to %.2f gallons of ethanol" % (gallons, ethanol)
    print "%.2f gallons of gasoline requires %.2f of US dollars" % (gallons, price)


gasoline_info()