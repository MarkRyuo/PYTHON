# create a greeting 
# create a word list 
# randomly choose a word in the list 
# ask the user to guess a letter 
# bonus make the program take the input from the user and make it lowercase 
# check if the letter is in the word 



greet = input("Enter your name: ") 

def Greeting(greet) :
    
    print(f"Konichiwa {greet}")

def _List() :

    list_of_word = [
        "Spaces",
        "Python",
        "Golive",
        "Prettier"
    ]
    return list_of_word


def main() :

    Greeting(greet)
    _listOf = _List()
    print(f"This is the list: \n {_listOf} " )

main()    