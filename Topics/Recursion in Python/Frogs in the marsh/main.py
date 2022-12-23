def number_of_frogs(year):
    frogs = 120
    if year == 1:
        return frogs
    else:
        return 2 * (number_of_frogs(year - 1) - 50)