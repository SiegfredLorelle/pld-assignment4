"""ASS4 PROG 3: 
Create a program which you will enter the amount of money you have,
it will also ask for the price of an apple. Display the maximum number
of apples that you can buy and the remaining money that you will have.
Display the output in the following format.
You can buy ___ apples and your change is ___ pesos."""

#Ass4 Prog3, first try

import math

def AskInputs():
    MoneyStart = int(input("How much MONEY do you have?  "))
    PriceApple = int(input("How much does an APPLE cost?  "))
    return MoneyStart, PriceApple

def Solving(MoneyStartF, PriceAppleF):
    BoughtApple = math.floor (MoneyStartF / PriceAppleF)
    MoneyLeft = MoneyStartF % PriceAppleF
    return BoughtApple, MoneyLeft

def Display(BoughtAppleF, MoneyLeftF):
    print()
    print (f"You can buy {BoughtAppleF} apple(s) and your change is {MoneyLeftF} pesos.")
    print()

#Step 1 - ask how much money, how much apple
print()
print("Yo!!")
FinalMoneyStart, FinalPriceApple = AskInputs()

#Step 2 - Solve max apple bought n money left
FinalBoughtApple, FinalMoneyLeft = Solving(FinalMoneyStart, FinalPriceApple)

#Step 3 - Display apple max apple bought and money left
Display(FinalBoughtApple, FinalMoneyLeft)