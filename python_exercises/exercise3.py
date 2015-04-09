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


def miles_per_hour():
    mph_float = raw_input("Please enter any positive number for the Miles Per Hour: ")

    while validate_float(mph_float) is False or validate_for_zero(mph_float):
        mph_float = raw_input("There is no point in checking 0 or less MPH, please enter a positive number: ")

    mph_float = float(mph_float)
    meters_per_hour = float(mph_float * 1609.34)
    meters_per_second = float(meters_per_hour / 3600)
    yards_per_hour = float(mph_float * 1760)
    # barleycorn = 117.647 meters
    barleycorn_day = float((meters_per_hour * 117.648) * 24)
    # furlong = 220 yards, fortnight is 14 days
    furlongs_fortnight = float((yards_per_hour * 220) * 336)
    feet_a_second = float((mph_float * 5280) / 3600)
    # mach is = 1230 feet/second
    mach_number = float(feet_a_second / 1230)
    # speed_of light = 299792458 meters/second
    speed_of_light_percentage = float((meters_per_second / 299792458) * .1)

    print "Original speed in miles/hour is: %.2f" % (mph_float)
    print "Converted to barleycorn/day is: %.2f" % (barleycorn_day)
    print "Converted to furlongs/fortnight is: %.2f" % (furlongs_fortnight)
    print "Converted to Mach number is: %f" % (mach_number)
    print "Converted to the percentage of the speed of light is: ", speed_of_light_percentage


miles_per_hour()