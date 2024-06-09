


# * Loop 


# * Loop 


# * Iterating Over a Dictionary

# * When iterating over a dictionary, you can use methods such as .keys(), .values(), or .items() to get the keys, values, or key-value pairs respectively.

# * DICT 

# person = {'name': 'Alice', 'age': 25}
# for items in person:
#     print(items, person[items])



person = {
    "name": "Niyari", 
    "age": 19
}

def Loopofperson() :
    
    for items in person :
        print(items, person[items])


# Loopofperson()


carbon = 31

for i in range(1, 4) :
    carbon += i
    pass  
# print(carbon)

# * Output : 37 

# * Explanation : 37 because the first is i is 1, 31 + 1 = 32 then the next is 32 + 2 = 34, next is 34 + 3 = 37 


# * protect the data 


data = {
    "name" : "Niyari",
    "age" : 19
}


def Log_in() :

    username = input("Enter your name: ") # * Enter username

    def Items() : # * Create Nested Function name Items 

        for items in data : # * loop the 'data' 
            data[items]  # * This is called indexing 
    
    items = Items() 

    if items == username :
        print("Hello")
    else :
        print("bye")


# Log_in()


list_of_names = [
    "Riyuo",
    "Niyari",
    "Jian",
    "Sopheya",
    "Samantha"
]

emptylist = []

for keys in list_of_names :
    keys.append(emptylist)
print(emptylist)
        



