


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
print(carbon)

# * Output : 37 

# * Explanation : 37 because the first is i is 1, 31 + 1 = 32 then the next is 32 + 2 = 34, next is 34 + 3 = 37 

