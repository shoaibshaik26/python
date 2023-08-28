#Design a program that takes input amount of currency and returns the number of currency NOTES by the denomination that cab be returns to the customer

#Formating of the statement need to done as well


number = float(input(" Please enter the change you required for"))
Cuurencey500= currency200 = currency100 = currency50 = currency20 = currency10 = currency5 = currency1 =0 #cascading of the data

if (number>=500):
    Cuurencey500 = int(number/500)
    number = number-(Cuurencey500*500)
    print("the number of 500 notes you will get is: ", Cuurencey500)
if (number>=200):
    currency200 = int(number/200)
    number = number-(Cuurencey500*200)
    print("the number of 200 notes you will get is: ", currency200)
if (number>=100):
    currency100 = int(number/100)
    number = number-(currency100*100*100)
    print("the number of 100 notes you will get is: ", currency100)
if (number>=50):
    currency50 = int(number/50)
    number = number-(currency50*50)
    print("the number of 50 notes you will get is: ", currency50)
if (number>=20):
    currency20 = int(number/20)
    number = number-(currency20*20)
    print("the number of 20 notes you will get is: ", currency20)
if (number>=10):
    currency10 = int(number/10)
    number = number-(currency10*10)
    print("the number of 10 notes you will get is: ", currency10)
if (number>=5):
    currency5 = int(number/5)
    number = number-(currency5*5)
    print("the number of 50 notes you will get is: ", currency5)
if (number>=1):
    currency1 = int(number/1)
    number = number-(currency1*1)
    print("the number of 1 notes you will get is: %d" %(currency1))