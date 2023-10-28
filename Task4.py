import random
a=["s","w","g"]
count=1
print("Welcome to Rock Paper Scissors Game")
print("Press r for Rock\n")
print("Press p for Paper\n")
print("Press s for Scissors\n")
userscore=0
compscore=0
while count<=5:

    inp=input("Enter your choice: ")
    count+=1

    if (inp=="r" or inp=="p" or inp=="s"):
        comp=random.choice(a)
        print("Computer's choice: "+comp)

        if (inp=="r" and comp=="s"):
            userscore+=1
        elif(inp=="r" and comp=="p"):
            compscore+=1

        elif (inp == "p" and comp == "r"):
            userscore += 1

        elif (inp == "p" and comp == "s"):
            compscore += 1

        elif (inp == "s" and comp == "p"):
            userscore += 1

        elif (inp == "s" and comp == "r"):
            compscore += 1

        # elif (inp == "g" and comp == "g"):
        #     compscore += 1
        #     userscore+=1
        #
        # elif (inp == "w" and comp == "w"):
        #     compscore += 1
        #     userscore+=1
        #
        # elif (inp == "s" and comp == "s"):
        #     compscore += 1
        #     userscore+=1
    else:
            print("Invalid input")


if compscore>userscore:
    print("Computer wins")
elif userscore>compscore:
    print("User wins")
else:
    print("Its a tie")
print("Computer scores: ",compscore)
print("User scores: ",userscore)