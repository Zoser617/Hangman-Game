#Hangman Game

# For the random, time, and sleep function
import random
from time import sleep
# Random list of 10,000 words for the game, via MIT.edu 
word_file = "wordlist.10000.txt"
word = open(word_file).read().splitlines()

#Pick a random choice from the word list
picked = random.choice(word)

print ('The word has',len(picked), 'letters')

#The letters are picked right or wrong
right = ['_'] * len(picked)
wrong = []

# This is for the right word list
def update():
   for i in right:
       print(i, end = ' ')
   print()
print("Think of a word!") # Delays the choice of word
def wait():


   for i in range(4):
       print('.', end = '')
       sleep(.4)
   print()
update()

wait()


# Lets the user guess a letter
while True:
   print('===================')

   guess = input("Enter a letter:")
   print("Lets see how you did!")
   wait()

   if guess in picked:
       index = 0
       for i in picked:
           if i == guess:
               right[index] = guess
           index += 1
       update()


# Checks if the guess is in the wrong list
   else:
       if guess not in wrong:
           wrong.append(guess)



       else:
           print("You guessed that already")
       print(wrong)

#Number of guesses before ending the program
   if len(wrong) > 4:
       print('You are a Loser')
       print("The picked was ", picked, "!!!!")
       break

#When you guess all the letters correctly
   if '_' not in right:
       print("You are a winner!!!")
       break
input('Press ENTER to exit') #Only closes program after user confirmation