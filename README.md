# CRYPTO-LOGIC
CRYPTO-LOGIC is a word guessing game.

#  This game is designed to challenge the user to guess a word from the list of words in the wordList.txt file used in the program. The random class is imported to make use of its shuffle method to randomize the words for the game and to choose a random word. I have provided comments to make the program easier to understand and will also talk about them in greater detail in this README.md file.
  
#  The first step that the program takes is to read all the words into a list named "lst" variable from the wordList.txt provided in the repository. After the .txt file is read it is closed to prevent any issues. 
  
  inputFile = open("C:\\Users\\tanto\\Desktop\\wordList.txt","r")
line = inputFile.readline()
lst = []

while line != "" :
    line = inputFile.readline()
    line = line.rstrip()
    lst.append(line)

inputFile.close()

# Afterwards a random word is chosen from "lst" to be used in the guessing game.

value = random.randint(0,len(lst))
secretword = lst[value]

# The chosen word is then split into a list of characters to be shuffled
shufflelist = list(secretword)

# The word is shuffled using the shuffle method from the random class

random.shuffle(shufflelist)

# The game now starts and displays to the screen the welcome message and instructions for the user. A counter variable is initialized to keep track of the number of incorrect guesses. A variable named 'i' is created to increment through the characters of "secretword" when comparing the input from the user. A new string is initialized to display the user's current guesses and to act as a sentinel when compared to "secretword". The user is now prompted to enter a character to guess for the scrambled word.

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
    
# The game will use an "if" statement to check the player's guess and will execute the code based on the guess. This will loop until secretword is = guessdisplay.

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
        
# After all the letters have been guessed, the game will display the number of guesses it took to win the game and a congratulations message.

print("\nCongratulations! You found the word after %s incorrect guess(es)!" % counter)

