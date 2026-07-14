import random 
words=["camel","star","dog","true","game","baloon","apple"] 

# Take random word from list 
chosen_word=random.choice(words)
# print(chosen_word)

# To make space bar for word
placeholder =""
word_length = len(chosen_word)
for letter in range(word_length):
    placeholder +="-"
print(placeholder)

# Take input from user 
guess =input("Guess a letter. ").lower()


display =" "
for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display +="_"
print(display)