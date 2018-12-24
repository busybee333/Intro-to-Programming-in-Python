# -*- coding: utf-8 -*-
    #####################################################################
    #  Hangman
    #  Prompts user to enter word or phrase
    #  User gets 6 guesses and can guess letters, words, and phrases
    #  If user guesses word correctly, user wins
    #  If user does not guess word correctly within 6 turns, user loses
    #####################################################################

#this function finds and replaces dashes with the correct letter(s) guessed and prints it
def find(string, result, char):
    for i in range(len(string)):
        if string[i].lower() in right_letters:
            result = result[:i] + phrase[i] + result[i+1:]
    for guess in result: 
        print(guess, end="")
            
num_guesses = 0
position = 0
used_letters = " "
right_letters = ""
gameOver = False

print("Hangman: guess letters until you can guess the whole word or phrase.")
print("In this game you will get six tries.")
print("")
phrase = str(input("Enter a word or phrase: "))
for i in range(len(phrase)): #prompts user again if phrase contains digit(s) and soaces
        if phrase[i].isdigit():
            print("Error: only letters are allowed as input.")
            print("")
            phrase = str(input("Enter a word or phrase: "))
if phrase.isalpha() == False and " " not in phrase: #prompts user again if phrase contains digit(s) and no spaces
    print("Error: only letters are allowed as input.")
    print("")
    phrase = str(input("Enter a word or phrase: "))
current = len(phrase) * "-"
print("phrase: " + phrase)
for i in range(len(phrase)):
    if phrase[i].isalpha():
        current = current[:i] + "-" + current[i+1:]
    else:
        current = current[:i] + " " + current[i+1:]
print("current: " + current)
print("0 guesses so far out of 6: ")
print("")

for i in range(6):
    guess = (input("Guess a letter or whole word/phrase: ")).lower()
    if guess.isalpha() == False and " " not in phrase: #If user guesses a number
        print("Error: only letters and spaces are allowed as input.")
        print(str(num_guesses) + " guesses so far out of 6:" + used_letters)
        print("")
    elif guess.lower() in phrase and guess.lower() not in used_letters: #If user guesses correctly
        right_letters += guess
        print("current: ",end="")
        find(phrase, current, guess)
        print(" ")
        num_guesses += 1
        used_letters += guess
        allLettersGuessed = True
        for i in range(len(phrase)):
            if phrase[i] not in right_letters:
                allLettersGuessed = False
                break
        if allLettersGuessed:
            print("You won.")
            gameOver = True
        else:
            print(str(num_guesses) + " guesses so far out of 6:" + used_letters)
        if gameOver == True:
            break
        if num_guesses == 6 and allLettersGuessed == False:
            print("You lost.")
            print("The word/phrase was: " + phrase)
        print("")
    elif guess.lower() == phrase.lower(): #If user guesses phrase completely
        print("You won.")
        break
    elif guess.lower() in used_letters: #If guess has been guessed already
        print("You already used this letter.")
        print("current: ",end="")
        find(phrase, current, guess)
        print("")
        if num_guesses < 6:
            print(str(num_guesses) + " guesses so far out of 6:" + used_letters)
        print("")
    else: #If user doesn't guess correctly
        if len(guess) > 1:
            print("Wrong guess of whole word or phrase.")
        else:
            print("Letter not in phrase.")
        num_guesses += 1
        used_letters += guess
        if num_guesses < 6:
            print("current: ",end="")
            find(phrase, current, guess)
            print("")
            print(str(num_guesses) + " guesses so far out of 6:" + used_letters)
            print("")
        if num_guesses == 6:
            print("You lost.")
            print("The word/phrase was: " + phrase)