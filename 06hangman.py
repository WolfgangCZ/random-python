import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''', '''
  +---+
      |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

def PrintListInLine(word_list: list):
    for letter in word_list:
        print(letter, end="")
    print("\n")

print(len(stages))

random_words = ["vlak","pes","stanice","slepice","hovnocuc","sloveso","mrakodrap","abrakadabra","letadlo"]
chosen_word = random_words[random.randrange(len(random_words))]
chosen_word = list(chosen_word)
empty_word = ""
for i in chosen_word:
    empty_word = empty_word + '_'

empty_word = list(empty_word)
lifes = len(stages) - 1

while(True):
    print(logo)
    print("Mysterious word: ", end="")
    PrintListInLine(empty_word)
    guessed_letter = input("guess a letter: ")
    IsGuessRight = False
    for i in range(len(chosen_word)):
        if guessed_letter == chosen_word[i]:
            empty_word[i] = guessed_letter
            IsGuessRight = True
    if not IsGuessRight:
        lifes -= 1
    if lifes == 0:
        PrintListInLine(empty_word)
        print("GAME OVER, YOU LOST")
        exit()
    if empty_word.count('_') == 0:
        print("Nice, it was:")
        PrintListInLine(empty_word)
        restart = input("GG YOU WON, WANNA PLAY AGAIN? (y)")
        if restart == "y":
            chosen_word = random_words[random.randrange(len(random_words))]
            chosen_word = list(chosen_word)
            empty_word = ""
            for i in chosen_word:
                empty_word = empty_word + '_'
            empty_word = list(empty_word)
            lifes = len(stages) - 1
        else:
            exit()
