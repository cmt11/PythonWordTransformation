"""
This program uses recursion to solve a "changeling" puzzle, in which one English word must be transformed into another English word of the same length in a given number of steps.
Only one letter at a time may be changed, and all of the "transition" words must be legal English words themselves.

Author: Chris Thomas
"""


"""
Imports WordLookup function and list of English words
"""
from WordLookup import *


"""
This function takes an English word (the current word), another different English word (the target word) and the number of steps we are allowed to get from the current word to the target word as paremeters.
It returns a list of steps to get from the current word to the target word if there is a solution, and None if there is not.
"""
def changeling(current, target, numberSteps):
    words = [] # the list of words getting us from the current word to the target word
    if current == target and numberSteps >= 0: # if the two words are the same, return that word
        return [target]
    elif numberSteps <= 0: # if we are not allowed any more steps, return None
        return None
    elif len(current) != len(target): # if the two words are different lengths, return None
        return None
    elif lookup(current) == False or lookup(target) == False: # if either of the two words are not legal English words, return None
        return None
    else:
        tempOneDifferent = oneLetterDiff(current) # a list of words which differ from the current word by only one letter
        if target in tempOneDifferent: # if the target word is in tempOneDifferent, we have found a solution; insert the target and current words into the list
            words.insert(0, target)
            words.insert(0, current)
            return words # return the list of words
        else:
            for word in tempOneDifferent: # loop through every word in tempOneDifferent
                temp = changeling(word, target, numberSteps-1) # recursive call to changeling assigned to a "temp" variable
                if temp != None:  # if temp is not None, the recursive call found a solution; update the list of words with what we already have plus the current word
                    words = temp
                    words.insert(0, current)
                    return words  # return the list of words

        

"""
This function takes an English word as a parameter, and returns a list of all English words which differ from the given word by only one letter.
"""
def oneLetterDiff(word):
    related = [] # the (currently empty) list of "related" words
    temp = word  # stores a copy of the original word
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    i = 0
    while i < len(word): # loop through every letter of the word
        word = temp
        for x in alphabet: # loop through every letter of the alphabet
            word = changeLetter(word, i, x) # change the current letter of the word to the current letter of the alphabet
            if lookup(word) == True and word != temp: # if this change gives a legal English word, add it to the list
                related.append(word)
        i+=1
    return related # return the list of "related" words



"""
This function takes an English word to be changed, the index of the letter to be changed, and the letter it is to be changed to as parameters, and returns the changed word.
"""
def changeLetter(word, i, x):
    letters = [] # the (currently empty) list of letters in the word
    newWord = "" # the new word to be created
    n = 0
    for n in word: # loop through all letters in the word and add them to the list
        letters += n
    letters[i] = x # change the specified letter
    for a in letters: # loop through all letters in the list and add them to the new word
        newWord += a
    return newWord # return the new "one-letter-different" word
