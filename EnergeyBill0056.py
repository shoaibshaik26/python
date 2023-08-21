# Write a programe to calculate the Eletricity Bill

EnergeyBill = float(input(" Pleasde enter the energy consumed"))
if EnergeyBill < 50:
    print(" the bill for the consumed energy is",EnergeyBill*0.50)
    print("flag4")
else:    
    if EnergeyBill >= 50 and EnergeyBill <= 150 :
        totalamount = 25 + (EnergeyBill-50)*0.75
        amount= totalamount + totalamount*0.20
        print(" the bill for the consumed energy is",amount)
        print("flag1")
    else:
        if EnergeyBill >= 150 and EnergeyBill <= 250 :
            totalamount = 100 + ((EnergeyBill-150)*1.25)
            amount= totalamount + totalamount*0.20
            print(" the bill for the consumed energy is",amount)
            print("flag2")
        else:
            EnergeyBill >= 251
            totalamount = 220 + ((EnergeyBill-250)*1.50)
            amount= totalamount + totalamount*0.20
            print(" the bill for the consumed energy is",amount)
            print("flag3")