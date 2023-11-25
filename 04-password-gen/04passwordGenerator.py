import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

passwordLenght = nr_letters + nr_symbols + nr_numbers
numberSequence = []
passwordMask = []

#fill mask with emtpy strings
for i in range(passwordLenght):
    passwordMask.append("null")

#create simple number array
for i in range(passwordLenght):
    numberSequence.append(i)

#choose random numbers and create mask for password
for i in range(nr_letters):
    randIndex = random.randint(0,len(numberSequence)-1)
    chosenIndex = numberSequence[randIndex] 
    passwordMask[chosenIndex] = "letter"
    numberSequence.pop(randIndex)
for i in range(nr_symbols):
    randIndex = random.randint(0,len(numberSequence)-1)
    chosenIndex = numberSequence[randIndex] 
    passwordMask[chosenIndex] = "symbol"
    numberSequence.pop(randIndex)
for i in range(nr_numbers):
    randIndex = random.randint(0,len(numberSequence)-1)
    chosenIndex = numberSequence[randIndex] 
    passwordMask[chosenIndex] = "number"
    numberSequence.pop(randIndex)

generatedPassword = ""

for i in range(len(passwordMask)):
    if passwordMask[i] == "symbol":
        generatedPassword += symbols[random.randint(0, len(symbols)-1)]
    elif passwordMask[i] == "letter":
        generatedPassword += letters[random.randint(0, len(letters)-1)]
    elif passwordMask[i] == "number":
        generatedPassword += numbers[random.randint(0, len(numbers)-1)]
print(generatedPassword)