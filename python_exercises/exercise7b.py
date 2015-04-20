import temperature

temps = {
    "Boston": "0 C",
    "Boise": "48 F",
    "Phoenix": "85 F",
    "Miami": "40 C",
    "Riverside": "30 C",
    "Baltimore": "32 F",
}


for key, value in temps.items():
    original_type = ""
    converted_type = ""
    opposite = 0

    c_or_f = value[-1]
    temp = int(value[:2])

    if c_or_f is "C":
        opposite = temperature.c2f(temp)
        original_type = "Celsius"
        converted_type = "Fahrenheit"

    else:
        opposite = temperature.f2c(temp)
        original_type = "Fahrenheit"
        converted_type = "Celsius"

    print "In {} it is {} degrees {}, which is the equivalent to {} degrees {}".format(key, temp, original_type,
                                                                                       opposite, converted_type)