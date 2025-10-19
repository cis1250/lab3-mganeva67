#!/usr/bin/env python3

#need this to start any python coad^

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re
# 1. Prompt the user: Ask the user to enter a sentence.
#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

user_sentence = input("Enter a sentence: ")
# 2. Split the sentence
while (is_sentence(user_sentence) == False): # starting of while loop and will run untill the is_ste function will run F
    print("This does not meet the criteria for a sentence.")
    user_input = input("Enter a sentence: ") # prompts it is need to uptodate to check the while loop
#need to run this:
#Input: "To be or not to be, that is the question."
#Output:
#to: 2
#be: 2
#or: 1
#not: 1
#that: 1
#is: 1
#the: 1
#question: 1
    # 3. Create lists to store words and their corresponding frequencies.
    word_tokens = processed_sentence.split() # making a list 
    unique_world = []
    frequencies = []
# CreatLists^ to^ stor^ the^ words^ & ther^ num
# Word frequency exercise frequency is a list i need to creat for nad if writen be2 and if writen that1
# 4. Iterate through words and update frequencies
for word in word_tokens: # starting of anouther FOR loop 
    if word in unique_words: # checking if the correct word has already been stored
        # If YES, find its index
        index = unique_words.index(word) # its us after a word it foun and placed in the correct the position
        
        # CORRECTED: Fix the typo 'frequncies' to 'frequencies'
        # Update frequency: Increment the count at that index
        frequencies[index] = frequencies[index] + 1 
        index = unique_words.index(word) 
        frequencies[index] = frequncies[index] + 1
        # ^takes curect index in frq and add 1 to its saving the new values back to the same spot
    else: # the then in an if els statment
        frequencies.append(1) 
        unique_words.append(word) # stores box
        frequencies.append(1) #states and f cound of the new world
print("\nWorld Frequencies:")
for i in range(len(unique_words)): #loop
    word = unique_words[i] # asses the world name for printing
    frequency = frequencies[i]  #make the num avalibal for the next line to see
    print(f"{word}:{frequency}")
    
    
# Your code doesn't run -3
