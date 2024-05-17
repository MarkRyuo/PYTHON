# create a greeting 
# create a word list 
# randomly choose a word in the list 
# ask the user to guess a letter 
# bonus make the program take the input from the user and make it lowercase 
# check if the letter is in the word 


list_of_word = [
        "Spaces",
        "Python",
        "Golive",
        "Prettier"
    ]


greet = input("Enter your name: ") 

def Greeting(greet) :
    
    print(f"Konichiwa {greet}")

def _List() :

    for _list in list_of_word :
        print(_list)
    return _list

def main() :

    Greeting(greet)
    _ListOf = _List()
    print(f"This is the list: \n {_ListOf}")

main()    