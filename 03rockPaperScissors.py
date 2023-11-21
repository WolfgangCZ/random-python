import random 

print("hello world")

results = ["rock", "paper", "scissors"]

yourChoice = input("What you do? Rock, paper, or scissors? Go: ")

if yourChoice != "rock" and yourChoice != "scissors" and yourChoice != "paper":
    print("you are dumb, im out!")
    exit()

pcChoice = results[random.randint(0,2)]

print("PC chose {}".format(pcChoice))

if yourChoice == pcChoice:
    print("its a draw!")
elif yourChoice == "rock" and pcChoice == "paper":
    print("you lost!")
elif yourChoice == "rock" and pcChoice == "scissors":
    print("you won!")
elif yourChoice == "paper" and pcChoice == "rock":
    print("you won!")
elif yourChoice == "paper" and pcChoice == "scissors":
    print("you lost!")
elif yourChoice == "scissors" and pcChoice == "paper":
    print("you won!")
elif yourChoice == "scissors" and pcChoice == "rock":
    print("you lost!")




