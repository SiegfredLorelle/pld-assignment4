"""ASS4 PROG1: 
Create a program that will ask for name, age and address. 
Display those details in the following format.
Hi, my name is _____. I am ____ years old and I live in _____ ."""

#Ass4 Prog1 - 1st try, only for fun

def AskInputs():
    print()
    print("Yo!! I'll ask you some personal details.")
    Name = input("Your name?  ")
    Age = int(input("Your age in years?  "))
    Address = input("Place you live?  ")
    return Name, Age, Address

def Display(FinalNameF, FinalAgeF, FinalAddressF):
    print()
    if FinalAge == 1:
        print(f"Hi, my name is {FinalNameF}. I am {FinalAgeF} year old and I live in {FinalAddressF}.")
    else:
        print(f"Hi, my name is {FinalNameF}. I am {FinalAgeF} years old and I live in {FinalAddressF}.")
    print()

# Step 1 - ask name, age, address
FinalName, FinalAge, FinalAddress = AskInputs()

#Step 2 - check if age is valid
while FinalAge <= 0 or FinalAge >= 120:
    print()
    if FinalAge <= 0:
        print(f"{FinalAge} years old is not a valid age!! Try again!")
    elif FinalAge >= 120:
        print(f"{FinalAge} years old is way too old to be true!! Try again!")
    FinalName, FinalAge, FinalAddress = AskInputs()
    
#Step 3 - display name age & address
Display(FinalName, FinalAge, FinalAddress)