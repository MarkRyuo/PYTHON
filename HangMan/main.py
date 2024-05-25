import person
from Ban import list_of_ban

# Todo create a greeting 
# Todo create a word list 
# Todo randomly choose a word in the list 
# Todo ask the user to guess a letter 
# Todo bonus make the program take the input from the user and make it lowercase 
# Todo check if the letter is in the word 


# Todo Loop through each of the letters in the chosen word 
# Todo if the letter is in the word replace the "_" with the letter 
# Todo it should look like this "_", "d", "_", "i", "_"


# Todo Use a while loop so your game keeps going 
# Todo until the word has been guessed 


# GREETING = person.Greeting()


def Greeting():
    
    print("Welcome to Hangman Challange ")

    _username = True

    while _username :

        ask_Username = input("Enter your username: ").lower()
        # ! Check if ask_Username is in the ban name 

        if ask_Username in list_of_ban :
            print(f"Your ban here user {ask_Username}")
            _username = False
        elif ask_Username.isdigit :
            print()
            # pass # Todo Gumawa ng condition kapag number lang nilagay ay huwag ito papasukin 
        elif ask_Username :
            break
        else : 
            print("Unsupported Username")

        return ask_Username


def main() :

    Greeting()




main()
