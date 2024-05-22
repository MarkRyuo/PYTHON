import random


# create a greeting 
# create a word list 
# randomly choose a word in the list 
# ask the user to guess a letter 
# bonus make the program take the input from the user and make it lowercase 
# check if the letter is in the word 

# List of name of ban for playing hangman

list_ban = [
        "niyari",
        "ryuo",
        "samantya",
        "mark",
        "sopheya"
    ]

class Greeting() :

    def __init__(self, username) :
        self.username = username
        
    
    def greet(self):

        print(
            f"Hello! \nWelcome to Hangman {self.username}"
            )

def add_username() :

    while True:

        username = input("Enter your username: ").lower()

        if username in list_ban :
            print("This user is ban!")
            exit() 
        else :
            break
        
    return username




def main() :

    username = add_username()
    User = Greeting(username)
    User.greet()

    word_random = random.choice(list_ban)
    empty_word = []

    if User :

        for leter in range(word_random) :
            empty_word += "_"
        


main()

