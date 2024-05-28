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
empty = []

for letter in _names : # * Ang laman ng letter ay ang random letter sa list_of_name
    empty += letter # * Ang empty ay increament sa letter 
print(empty)
