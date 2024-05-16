# LOOPS 

people = [
    "Niyari",
    "Moda",
    "Sopheya",
    "Mark"
]

for i in people :
        print(i)

while True :
    
    _name = input("Who is your Favorite?: ")

    if _name in people :
        break
    else :
        print("Who is that?")
print(_name)