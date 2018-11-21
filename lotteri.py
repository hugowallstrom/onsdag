import random # aktiverar random

bag = [] # listan är tom nu, men är "full" vid programmets slut.

for x in range(6):
    ball = (random.randint(1, 9)) #slumpar en siffra mellan 1 och 9
    if ball == 1:
        bag.append("1")
    elif ball == 2:
        bag.append("2")
    elif ball == 3:
        bag.append("3")
    elif ball == 4:
        bag.append("4")
    elif ball == 5:
        bag.append("5")
    elif ball == 6:
        bag.append("6")
    elif ball == 7:
        bag.append("7")
    elif ball == 8:
        bag.append("8")
    else:
        bag.append("9") # alla olika siffor i en if, elif och else sats (jag vet det finns mer i vanligt lotteri, men det skulle ta allt för lång tid)

print("Your lottery number is: ")
print(bag) # skriver ut listan