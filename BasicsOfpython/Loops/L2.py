import random 
# Todo Loop 

# * [] This is List 
# * () This is Tuple 
# * {} This is Set 
# * {} This is Dict 


list_of_name = [ 
    "Riyuo",
    "Niyari",
    "Sopheya",
    "Jian",
    "Arkjo"
]


_names = random.choice(list_of_name) 
empty_list = []

for letter in _names : # * Ang laman ng letter ay ang random letter sa list_of_name
    empty_list += letter # * Ang empty ay increamented sa letter magkakaroon ng laman ang empty list  
# print(empty_list) 

this_is_dict = {
    "name" : "Riyuo",
    "age" : 20
}
