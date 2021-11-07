"""ASS4 PROG 3: 
Create a program which you will enter the amount of money you have,
it will also ask for the price of an apple. Display the maximum number
of apples that you can buy and the remaining money that you will have.
Display the output in the following format.
You can buy ___ apples and your change is ___ pesos."""

#Ass4 Prog3, 1st try
#            2nd try, avoided negative, added centavo

import math

def AskInputs():
    MoneyStart = float(input("How much MONEY do you have?  "))
    PriceApple = float(input("How much does an APPLE cost?  "))
    MoneyStart = round(MoneyStart,2)
    PriceApple = round(PriceApple,2)
    return MoneyStart, PriceApple

def Solving(MoneyStartF, PriceAppleF):
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

#Step 2 - check negatives n zeros
while FinalMoneyStart < FinalPriceApple or FinalMoneyStart <= 0 or FinalPriceApple <= 0:
    print()
    if FinalMoneyStart <= 0 and FinalPriceApple > 0:
        if FinalMoneyStart == 0:
            print("You cannot buy anything with ZERO money!!") 
        else:
            print("You cannot have NEGATIVE money!!")

    elif FinalPriceApple <= 0 and FinalMoneyStart > 0:
        if FinalPriceApple == 0:
            print("Apples are not sold for free!!")
        else:
            print("Apple price cannot be NEGATIVE!!")

    elif FinalMoneyStart <= 0 and FinalPriceApple <= 0:
        if FinalMoneyStart == 0 and FinalPriceApple == 0:
            print("ZEROS are not acceptable!!")
        elif FinalMoneyStart < 0 and FinalPriceApple < 0:
            print("NEGATIVES are not acceptable currency!!")
        else:
            print("NEGATIVE and ZERO are not acceptable!!")

    elif FinalMoneyStart < FinalPriceApple:
        print("Sorry you cannot afford an apple.")
   
    print()
    print("Try Again!")
    FinalMoneyStart, FinalPriceApple = AskInputs()

#Step 3 - Solve max apple bought, money left in pesos, money left in centavos
FinalBoughtApple, FinalMoneyLeftPesos, FinalMoneyLeftCentavo = Solving(FinalMoneyStart, FinalPriceApple)

#Step 4 - Display apple max apple bought and money left
Display(FinalBoughtApple, FinalMoneyLeftPesos, FinalMoneyLeftCentavo)