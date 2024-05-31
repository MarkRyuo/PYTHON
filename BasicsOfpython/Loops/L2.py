import random 
# Todo Loop 

# * [] This is List 
# * () This is Tuple 
# * {} This is Set 
# * {} This is Dict 


LIST_OF_NAME = [ # * List 
    "Riyuo",
    "Niyari",
    "Sopheya",
    "Jian",
    "Arkjo"
]

this_is_dict = { # * Dict 
    "name" : "Riyuo",
    "age" : 20
}



def print_list() :

    _names = random.choice(LIST_OF_NAME) 
    empty_list = []

    for letter in _names : # * Ang laman ng letter ay ang random letter sa list_of_name
        empty_list += letter # * Ang empty ay increamented sa letter magkakaroon ng laman ang empty list  
    print(empty_list) 

# print_list()


def print_dict() :

    name_ = this_is_dict["name"] # * Sa dict kailagan mo i declare para makuha mo 
    empty_list = []

    for dict_ in name_ : 
        empty_list += dict_ 
    print(empty_list)


# print_dict()

def List_():
    LIST_OF_NAME = ["Niyari", "Alice", "Bob", "John"]  # Example list of names
    
    def loop1(name):
        emptylist = []
        for char in name:
            emptylist.append(char)
        return emptylist

    while True:
        name_ = random.choice(LIST_OF_NAME)
        emptylist = loop1(name_)
        
        if ''.join(emptylist) == "Niyari":
            break

    return emptylist

print(List_()))




