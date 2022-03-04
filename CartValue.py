def cart_value(value):
    if value < 1000:
        surcharge = 1000 - value
    else:
        surcharge = 0
    return surcharge