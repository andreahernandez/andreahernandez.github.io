# Simple hangman
import random

# Creates a tuple with words in
Words = ("secret","summer","ice","pizza","icecream","beach")

# pick a word randomly
word = random.choice(Words)
print("The word is", len(word), "letters long.")

for i in range(6):
    letter = input("Guess a letter:")
    if letter in word:
        print("Yes, the word contains:", letter)
    else:
        print("No, it doesn't contain:", letter)
print("That's all your letter guesses used up.")
guess = input("Now guess the word:")
if guess == word:
    print("Well done, you got it.")
else:
    print("Sorry, wrong.")
