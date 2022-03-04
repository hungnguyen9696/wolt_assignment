from datetime import datetime
from CartValue import cart_value
from DeliveryDistance import delivery_distance
from NumberOfItems import number_of_items

def calculating(fee):
    #calculate cart value_fee
    surcharge=cart_value(fee.cart_value)

    #calculate delivery distance_fee
    deli_fee=delivery_distance(fee.delivery_distance)

    #calculatenumber of item_fee
    item_charge=number_of_items(fee.number_of_items)

    #total fee
    delivery_fee= surcharge+ deli_fee+ item_charge

    #iso datestring to datetime obj
    order_time= datetime.strptime(fee.time, "%Y-%m-%dT%H:%M:%SZ")

    #check if time is 3-7pm on friday
    if order_time.strftime("%w")== "5" and int(order_time.strftime("%H"))> 14 and int(order_time.strftime("%H"))< 19:
        delivery_fee *= 1.1

    #other conditions
    if delivery_fee > 1500:
        delivery_fee = 1500
    if fee.cart_value > 10000:
        delivery_fee = 0

    return delivery_fee