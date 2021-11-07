"""ASS4 PROG 3: 
Create a program which you will enter the amount of money you have,
it will also ask for the price of an apple. Display the maximum number
of apples that you can buy and the remaining money that you will have.
Display the output in the following format.
You can buy ___ apples and your change is ___ pesos."""

#Ass4 Prog3, 1st try
#            2nd try, avoided negative, added centavo,
#            3rd try, added exit/tryagain option

import math, sys

def AskInputs():  #Step1
    MoneyStart = float(input("How much MONEY do you have?  "))
    PriceApple = float(input("How much does an APPLE cost?  "))
    MoneyStart = round(MoneyStart,2)
    PriceApple = round(PriceApple,2)
    return MoneyStart, PriceApple

def Checker (MoneyStartF, PriceAppleF):   #Step2
    if MoneyStartF < PriceAppleF or MoneyStartF <= 0 or PriceAppleF <= 0:
        print()
        if MoneyStartF <= 0 and PriceAppleF > 0:
            if MoneyStartF == 0:
                print("You cannot buy anything with ZERO money!!") 
            else:
                print("You cannot have NEGATIVE money!!")

        elif PriceAppleF <= 0 and MoneyStartF > 0:
            if PriceAppleF == 0:
                print("Apples are not sold for free!!")
            else:
                print("Apple price cannot be NEGATIVE!!")

        elif MoneyStartF <= 0 and PriceAppleF <= 0:
            if MoneyStartF == 0 and PriceAppleF == 0:
                print("ZEROS are not acceptable!!")
            elif MoneyStartF < 0 and PriceAppleF < 0:
                print("NEGATIVES are not acceptable currency!!")
            else:
                print("NEGATIVE and ZERO are not acceptable!!")

        elif MoneyStartF < PriceAppleF:
            print("Sorry you cannot afford an apple.")

        print()    #exit/tryagain option
        print("Type '1' to try again.")
        print("Type '2' to exit the program. ")
        OneOrTwo = input("Reply:   ")
        return OneOrTwo

def Solving(MoneyStartF, PriceAppleF):      #Step 3
    #solv muna money left with deci n without para makuha centavo
    MoneyLeftWithDeci = MoneyStartF % PriceAppleF    
    MoneyLeftWithoutDeci = math.floor (MoneyStartF % PriceAppleF)

    #FinalAns
    BoughtApple = math.floor (MoneyStartF / PriceAppleF)
    MoneyLeftPesos = MoneyLeftWithoutDeci
    MoneyLeftCentavos = (MoneyLeftWithDeci - MoneyLeftWithoutDeci) * 100
    return BoughtApple, MoneyLeftPesos, MoneyLeftCentavos

def Display(BoughtAppleF, MoneyLeftPesosF, MoneyLeftCentavoF):
    print()
    print (f"You can buy {BoughtAppleF} apple(s) and your change is {MoneyLeftPesosF} pesos and {MoneyLeftCentavoF:.0f} centavos.")
    print()


#Step 1 - ask how much money, how much apple
print()
print("Yo!!")
FinalMoneyStart, FinalPriceApple = AskInputs()

#Step 2 - check negatives n zeros tapos exit/tryagain option
OneOrTwo = Checker(FinalMoneyStart, FinalPriceApple)

while OneOrTwo == "1":
    print()
    print("Try again!")
    FinalMoneyStart, FinalPriceApple = AskInputs()
    OneOrTwo = Checker(FinalMoneyStart, FinalPriceApple)

if OneOrTwo == "2":
    print()
    print("The program is closing. Thank you for trying!")
    print()
    sys.exit()

if OneOrTwo is None:  #para d mag error pag tama inputs
    print()

else:  #incase may mag input na d 1 at 2
    print()
    print("Please follow the instructions. Restart the program if you want to start again.")
    print()
    sys.exit()   

#Step 3 - Solve max apple bought, money left in pesos, money left in centavos
FinalBoughtApple, FinalMoneyLeftPesos, FinalMoneyLeftCentavo = Solving(FinalMoneyStart, FinalPriceApple)

#Step 4 - Display apple max apple bought and money left
Display(FinalBoughtApple, FinalMoneyLeftPesos, FinalMoneyLeftCentavo)