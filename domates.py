right_water_amount = 6
water_amount = int(input("water amount for tomatos in every 60h? "))

if water_amount == right_water_amount:
    print("motoru kapat.")
elif water_amount != right_water_amount:
    if water_amount < right_water_amount:
        increase = right_water_amount - water_amount
        print(f"\nmotor çalışsın ve {int(increase)} litre daha eklesin!")
    elif water_amount > right_water_amount:
        decrease = abs(right_water_amount - water_amount)
        print(f"\nmotor çok fazla çalışmış ve {int(decrease)} litre fazla su vermiş!")