# Python program to calculate electricity bill

unit = int(input)("please enter the number of units you consumed: ")

if(units < 50):
    amount = units*2.60
    surcharge = 25
    elif(unit <= 100):
        amount=130+((units - 50)*3.25)
        surcharge= 35
        elif(units <= 200):
            amount = 130 + 163.50 + ((units - 100)*5.24)
            surcharge = 45

            else:
                amount = 130+163.50+526+((units - 200)*8.45) 
                surcharge = 75

                total = amount + surcharge
                printf("/nElectricity Bill = %.2f" %total)