import random 


words = [
    "Hacker",
    "User",
    "Admin"
]


wordsOf = random.choice(words) # Kukuha siya ng random word sa words list
display_word = [] 

for letter in wordsOf :
    display_word += "_" 
print(display_word)