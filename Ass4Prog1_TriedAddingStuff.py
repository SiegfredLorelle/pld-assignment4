"""ASS4 PROG1: 
Create a program that will ask for name, age and address. 
Display those details in the following format.
Hi, my name is _____. I am ____ years old and I live in _____ ."""

#Ass4 Prog1 - 1st try, only for fun
#             2nd try, added exit or try again option
            
import sys

def AskInputs():
    print()
    print("Yo!! I'll ask you some personal details.")
    Name = input("Your name?  ")
    Age = int(input("Your age in years?  "))
    Address = input("Place you live?  ")
    return Name, Age, Address

def AgeCheck(AgeF):
    if AgeF <= 0 or AgeF >= 120:   #iwas negative age at wala nmn atang 120+ na age
        print()
        if AgeF <= 0:
            print(f"{AgeF} years old is not a valid age!!")
        elif FinalAge >= 120:
            print(f"{AgeF} years old is way too old to be true!!")
        print()
        print("Type '1' to try again.")
        print("Type '2' to exit the program. ")    
        OneOrTwo = input("Reply:   ")
        return OneOrTwo

def Display(FinalNameF, FinalAgeF, FinalAddressF):
    print()
    if FinalAge == 1:   # year old (singular)
        print(f"Hi, my name is {FinalNameF}. I am {FinalAgeF} year old and I live in {FinalAddressF}.")
    else:
        print(f"Hi, my name is {FinalNameF}. I am {FinalAgeF} years old and I live in {FinalAddressF}.")
    print()

#Step 1 - ask name, age, address
FinalName, FinalAge, FinalAddress = AskInputs()

#Step 2 - check if age is valid, and exit/tryagain option
Checker = AgeCheck(FinalAge)

while Checker == "1":
    FinalName, FinalAge, FinalAddress = AskInputs()
    Checker = AgeCheck(FinalAge)
if Checker == "2":
    print()
    print("The program is closing. Thank you for trying!")
    print()
    sys.exit()
if Checker is None:  #para d mag error pag tama ung age
    print()
else:  #incase may mag input na  hindi 1 at 2
    print()
    print("Please follow the instructions. Restart the program if you want to start again.")
    print()
    sys.exit()
    
#Step 3 - display name age & address
Display(FinalName, FinalAge, FinalAddress)