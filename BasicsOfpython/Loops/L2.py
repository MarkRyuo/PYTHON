import random 
# Todo Loop 

# * [] This is List 
# * () This is Tuple 
# * {} This is Set 
# * {} This is Dict 

# * List 
list_of_name = [ 
    "Riyuo",
    "Niyari",
    "Sopheya",
    "Jian",
    "Arkjo"
]
# * Dict 


_names = random.choice(list_of_name) 
empty_list = []

def print_list() :

    for letter in _names : # * Ang laman ng letter ay ang random letter sa list_of_name
        empty_list += letter # * Ang empty ay increamented sa letter magkakaroon ng laman ang empty list  
    print(empty_list) 

# print_list()

name_ = this_is_dict["name"] # * Sa dict kailagan mo i declare para makuha mo 

def print_dict() :
    for dict_ in name_ : 
        empty_list += dict_ 
    print(empty_list)


print_dict()

