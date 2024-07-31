# electricity bill checking using if else

meter_no=int(input("enter  meter number: "))
previous_reading=int(input("enter  previous reading: "))
current_reading=int(input("enter current_reading: "))
units=int(input("enter units: "))

if units <=100:
    unit_charge=2.50
    units=current_reading-previous_reading
    print("the total units are: ",units)
    total_amount=units*unit_charge
    print("the total amount is:",total_amount)

elif units > 100 and units <= 150:
    unit_charge=3.50
    units=current_reading-previous_reading
    print("the total units are: ",units)
    total_amount=units*unit_charge
    print("the total amount is: ",total_amount)

elif units <=150 and units <=200:
    unit_charge=2.50
    units=current_reading-previous_reading
    print("the total units are: ",units)
    total_amount=units*unit_charge
    print("the total amount is: ",total_amount)

elif units <=200 and units <=300:
    unit_charge=2.50
    units=current_reading-previous_reading
    print("the total units are: ",units)
    total_amount=units*unit_charge
    print("the total amount is: ",total_amount)

elif units <=300:
    unit_charge=2.50
    units=current_reading-previous_reading
    print("the total units are: ",units)
    total_amount=units*unit_charge
    print("the total amount is:",total_amount) 

else:
    print("invalid")
