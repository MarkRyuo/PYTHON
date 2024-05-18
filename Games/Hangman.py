# create a greeting 
# create a word list 
# randomly choose a word in the list 
# ask the user to guess a letter 
# bonus make the program take the input from the user and make it lowercase 
# check if the letter is in the word 


# list_of_word = [
#         "Spaces",
#         "Python",
#         "Golive",
#         "Prettier"
#     ]

# greet = input("Enter your name: ") 

# def Greeting(greet) :
    
#     print(f"Konichiwa {greet}")

# def _List(list_of_word) :

#     for i in list_of_word :
#         print(i) 

# def main() :

#     Greeting(greet)
#     print("This is the list of words: ")
#     _List(list_of_word)
    

# main()    


# create a greeting 
# create a word list 
# randomly choose a word in the list 
# ask the user to guess a letter 
# bonus make the program take the input from the user and make it lowercase 
# check if the letter is in the word 


def greetings() :

    print("Welcome to hangman")

    while True :
        question_1 = input("Are you playing (y/n): ").lower()
            if question_1 == "y" :
                break 
            elif question_1 == "n":
                question_2 = input("Are you sure (y/n): ")
                if question_2 == "y":
                    print("Okay thank you for coming")
                    break
                else:
                    print(f"{question_1} not in choice")
        else :
            print("Please enter")
        
    
    return question_1

def main() :

    greetings()


main()