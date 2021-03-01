# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random

# CRYPTO-LOGIC

# Open file to read
inputFile = open("C:\\Users\\tanto\\Desktop\\wordList.txt","r")
line = inputFile.readline()
lst = []

while line != "" :
    line = inputFile.readline()
    line = line.rstrip()
    lst.append(line)

inputFile.close()

# Select random word from list    
value = random.randint(0,len(lst))
secretword = lst[value]

# Split word into list of char
shufflelist = list(secretword)

# Shuffle char for secretword
random.shuffle(shufflelist)

# GAME START
counter = 0     # counter implemented for incorrect guesses
guesslist = []
i = 0               # i is created to increment through the characters of secretword
guessdisplay=''   # string created to display current guessed letters and used as sentinel

# Menu for game with secretword as sentinel boolean compared to guessdisplay
while guessdisplay != secretword :
    print("\nWelcome to CRYPTO-LOGIC!")
    print("Try to guess the scrambled word, one letter at a time!")
    print()
    print("Scrambled word: %s" % shufflelist)
    guess = input("Enter your guess ... ")      # asks for user input
    if guess == secretword[i] :
        guesslist.append(guess)
        guessdisplay =''.join(guesslist)
        i+=1
        print()         # If guessed correctly
        print("------------------------------------------")
        print()
        print("Incorrect guesses: %s" % counter)
        print("Letters already guessed: %s" % guessdisplay)
        print()
        print("------------------------------------------")
        print()
    else :
        counter+=1
        print()         # If guessed incorrectly
        print("------------------------------------------")
        print()
        print("Incorrect guesses: %s" % counter)
        print("Letters already guessed: %s" % guessdisplay)
        print()
        print("-------------------------------------------")
        print()

print("\nCongratulations! You found the word after %s incorrect guess(es)!" % counter)
