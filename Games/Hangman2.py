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
        "Sopheya"
    ]

class Greeting() :

    def __init__(self, username, greet) :
        self.username = username
        self.greet = greet 
    
    def greetings(self):

        print(
            f"Hello! \n Welcome to Hangman {self.username}"
            )

def add_username() :

    while True:

        username = input("Enter your username").lower

        if username in list_ban :
            print("This user is ban!")
        






def main() :
