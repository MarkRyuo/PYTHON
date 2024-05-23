import random
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


# def greetings() :

#     print("Welcome to hangman")

#     while True :
#         question_1 = input("Are you playing (y/n): ").lower()
#         if question_1 == "y" :
#             break 
#         elif question_1 == "n":
#             question_2 = input("Are you sure (y/n): ")
#             if question_2 == "y":
#                 print("Okay thank you for coming")
#                 break
#             elif question_2 == "n":
#                 continue
#             else:
#                 print(f"{question_1} not in choice")
#         else :
#             print("Please enter y or n")
        
    
#     return question_1


# def List_Of():

#     list_of_word = [
#         "Hacker",
#         "User",
#         "Admin"
#     ]
#     return list_of_word



# def main() :

#     decision = greetings() 
#     if decision :
#         words = List_Of()
#         question_3 = input("Guess the word (This is a users of the Internet): ")
#         if question_3 in words :
#             print("You Win")
#             print(f"The {question_3} in here in the list: {words }")
#         else :
#             print("You Lose")

# main()




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
            elif question_2 == "n":
                continue
            else:
                print(f"{question_1} not in choice")
        else :
            print("Please enter y or n")
        
    
    return question_1


def List_Of():

    list_of_word = [
        "hacker",
        "user",
        "admin"
    ]
    return list_of_word



def main() :

    greet = greetings()
    wordss = List_Of()
    wordOf = random.choice(wordss)
    display_word = []
    
    if greet :

        for letter in wordOf :
            display_word += "_"
        print(display_word)

    guess = input("Enter a Letter: ").lower()

    for letter in wordOf :
        if letter == guess:
            print("Right")
        else :
            print("Wrong")

main()




# Loop through each of the letters in the chosen word 
# if the letter is in the word replace the "_" with the letter 
# it should look like this "_", "d", "_", "i", "_"