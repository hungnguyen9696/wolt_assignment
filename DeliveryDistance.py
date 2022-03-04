def delivery_distance(distance):
    if distance <=1000:
        deli_fee=200
    else:
        extra_fee=0
        while (distance > 1000):
            distance -= 500
            extra_fee += 100
        deli_fee=extra_fee+200
    return deli_fee