temps = {
    "Boston": "0 C",
    "Boise": "48 F",
    "Phoenix": "85 F",
    "Miami": "40 C",
    "Riverside": "30 C",
    "Baltimore": "32 F",
}

# print temps
for key, value in temps.items():
    original_type = ""
    converted_type = ""
    opposite = 0

    c_or_f = value[-1]
    temperature = int(value[:2])

    if c_or_f is "C":
        opposite = temperature * (9/5) + 32
        original_type = "Celsius"
        converted_type = "Fahrenheit"

    else:
        opposite = (temperature - 32) * (9/5)
        original_type = "Fahrenheit"
        converted_type = "Celsius"

    print "In {} it is {} degrees {}, which is the equivalent to {} degrees {}".format(key, temperature, original_type,
                                                                                       opposite, converted_type)
