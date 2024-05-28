import random 
# Todo Loop 


list_of_name = [
    "Riyuo",
    "Niyari",
    "Sopheya",
    "Jian",
    "Arkjo"
]


_names = random.choice(list_of_name) 
empty = ""

for letter in _names : # * Ang laman ng letter ay ang random letter sa list_of_name
    empty += letter # * Ang empty ay increament sa letter 
print(empty)
