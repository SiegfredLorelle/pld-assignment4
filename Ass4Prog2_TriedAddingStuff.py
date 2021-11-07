"""ASS4 PROG 2: 
Create a program that will ask how many apples and oranges you want
to buy. Display the total amount you need to pay if apple price is 
20 pesos and orange is 25. Display the output in the following format.
The total amount is ______."""

#Ass4 Prog2, 1st try
#            2nd try, avoided negatives 

def AskNumFruits():
    print()
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
print("An APPLE cost 20php and an ORANGE cost 25php.")
FinalNumApple, FinalNumOrange = AskNumFruits()

#Step 2 - check if apple n orange r not negative
while FinalNumApple < 0 or FinalNumOrange < 0:
    print()
    if FinalNumOrange < 0 and FinalNumApple >= 0:
        print("You cannot buy NEGATIVE oranges!!")

    elif FinalNumApple < 0 and FinalNumOrange >= 0:
        print("You cannot buy NEGATIVE apples!!")

    elif FinalNumOrange < 0 and FinalNumApple < 0:
        print("You cannot buy NEGATIVE fruits!!")
        
    print("Try again!")
    FinalNumApple, FinalNumOrange = AskNumFruits()

#Step 3 - solve apple price, orange price, n total price 
FinalPriceApple, FinalPriceOrange, FinalPriceTotal = SolvingPrice(FinalNumApple, FinalNumOrange) 

#Step 4 - Display apple, orange n total price
Display (FinalPriceApple, FinalPriceOrange, FinalPriceTotal)