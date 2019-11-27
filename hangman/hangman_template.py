# Name:
# Section: 
# 6.189 Project 1: Hangman template
# hangman_template.py

# Import statements: DO NOT delete these! DO NOT write code above this!
from random import randrange
from string import *
from hangman_lib import *

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
# Import hangman words

WORDLIST_FILENAME = "words.txt"

def load_words(): # load word from words.txt
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    print('Enter play_hangman() to play a game of hangman!')
    return wordlist

# actually load the dictionary of words and point to it with 
# the words_dict variable so that it can be accessed from anywhere
# in the program
words_dict = load_words()


# Run get_word() within your program to generate a random secret word
# by using a line like this within your program:
# secret_word = get_word()

def get_word():
    """
    Returns a random word from the word list
    """
    word=words_dict[randrange(0,len(words_dict))]
    return word

# end of helper code
# -----------------------------------


# CONSTANTS
MAX_GUESSES = 6 #should put variable that never change in CAPITAL LETTERS
ALPHABETICAL = [chr(x) for x in range(ord('a'), ord('z') + 1)]

# GLOBAL VARIABLES 
secret_word = 'claptrap' 
letters_guessed = []

# From part 3b:

def answer_letters(secret_answer):
    result = []  
    result.append(a[0])
    for i in secret_answer:
        if i in result:
            pass
        else:
            result.append(i)
    return result

def word_guessed():
    '''
    Returns True if the player has successfully guessed the word,
    and False otherwise.
    '''
    global secret_word
    global letters_guessed

    # letters_guessed = [’e’, ’l’, ’q’, ’t’, ’r’, ’p’, ’n’]
    ####### YOUR CODE HERE ######
    for letters in secret_word:
        if letters not in letters_guessed:
            return False
    return True

def print_guessed():
    '''
    Prints out the characters you have guessed in the secret word so far
    '''
    global secret_word
    global letters_guessed
    

    ####### YOUR CODE HERE ######
    l = len(secret_word)
    not_guessed = ["-"] * l
    not_guessed_left = ALPHABETICAL
    for i in range(l):
        if secret_word[i] in letters_guessed:
            not_guessed[i] = secret_word[i]
    guessed_print = "".join(not_guessed)
    for i in not_guessed_left:
        if i in letters_guessed:
            not_guessed_left.remove(i)
    return guessed_print, not_guessed_left

def play_hangman():
    # Actually play the hangman game
    global secret_word
    global letters_guessed
    # Put the mistakes_made variable here, since you'll only use it in this function
    mistakes_made = 0

    # Update secret_word. Don't uncomment this line until you get to Step 8.
    #secret_word  = get_word()
    print(print_guessed())
    ####### YOUR CODE HERE ######
    list_secret_word =[]
    for i in secret_word:
        list_secret_word.append(i)
    
    def print_num_mistakes(mistakes_made):
        if mistakes_made <= 1:
            print("You got " + str(mistakes_made) + " mistake")
        else:
            print("You got " + str(mistakes_made) + " mistakes")

    def win_soon():
        choice_list = ['Y', 'N', 'y', 'n']
        tmp_mistakes_made = 0
        start_game = input("You have a choice to win the game early, if you want, please enter 'Y' or 'y'. If not enter 'N' or 'n': ")
        if start_game in choice_list:
            if start_game == 'Y' or start_game == 'y':
                win_chance = input("Enter a letter, or the word 'guess' to try and guess the full word: ")
                if win_chance == secret_word:
                    tmp_mistakes_made += MAX_GUESSES
                    print("Nice!!!")
                elif win_chance != secret_word:
                    tmp_mistakes_made += 2
                    print("You got " + str(tmp_mistakes_made) + " mistakes.")          
        elif start_game not in choice_list:
            win_soon()
        return int(tmp_mistakes_made)    
  
    mistakes_made = int(win_soon())
    if mistakes_made == MAX_GUESSES:
        print("Congratulation!!! You won!")
    else:
        while mistakes_made < MAX_GUESSES and not word_guessed():
            print_num_mistakes(mistakes_made)
            guess = input("Let make a guess: ")
            guess = guess.lower()
            if type(guess) != int:
                if guess in letters_guessed:
                    pass
                else:
                    letters_guessed.append(guess)
                    if guess not in list_secret_word:
                        mistakes_made += 1
                        print_hangman_image(mistakes_made)
                        print_num_mistakes(mistakes_made)
                    first, second = print_guessed()
                    print(first)
                    print("the string left to guess is:")
                    print(second)
                print("The string you guessed is:")
                print(letters_guessed)
                if not word_guessed():
                    if mistakes_made == MAX_GUESSES:
                        print("You lose!!! So sorry!")
                        break
                    else:
                        print(str(MAX_GUESSES - mistakes_made) + " guesses left")
                elif word_guessed():
                    print("Congratulation!!! You won!")

play_hangman()