import random 


words = [
    "Hacker",
    "User",
    "Admin"
]


wordsOf = random.choice(words) # Kukuha siya ng random word sa words list 
display_word = [] # eto ang mag sisilbing lalagyan 

for letter in wordsOf : # for loop 
    display_word += 0  # Imbis na letter ang ilagay ang inilagay ay empty 
print(display_word)