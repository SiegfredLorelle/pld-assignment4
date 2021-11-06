"""ASS4 PROG 2: 
Create a program that will ask how many apples and oranges you want
to buy. Display the total amount you need to pay if apple price is 
20 pesos and orange is 25. Display the output in the following format.
The total amount is ______."""

#Ass4 Prog2, first try

def AskNumFruits():
    NumApple = int(input("How many APPLES would you like to buy?  "))
    NumOrange = int(input("How many ORANGES would you like to buy?  "))
    return NumApple, NumOrange

def SolvingPrice(FinalNumAppleF, FinalNumOrangeF):
    PriceApple = (FinalNumAppleF) * 20
    PriceOrange = (FinalNumOrangeF) * 25
    PriceTotal = PriceApple + PriceOrange
    return PriceApple, PriceOrange, PriceTotal

def Display(PriceAppleF, PriceOrangeF, PriceTotalF):
    print()
    print(f"The APPLES will cost {PriceAppleF} php and the ORANGES will cost {PriceOrangeF} php.")
    print()
    print(f"The TOTAL AMOUNT is {PriceTotalF} php.")
    print()


#Step 1 - ask how many apples n oranges to buy 
print()
print("Yo!!")
FinalNumApple, FinalNumOrange = AskNumFruits()

#Step 2 - solve apple price, orange price, n total price 
FinalPriceApple, FinalPriceOrange, FinalPriceTotal = SolvingPrice(FinalNumApple, FinalNumOrange) 

#Step 3 - Display apple orange n total price
Display (FinalPriceApple, FinalPriceOrange, FinalPriceTotal)