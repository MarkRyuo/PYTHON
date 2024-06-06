
# * Varible or Literal
# * Loop

 
# ages = str(ages) # ! Fix this 

# def Age() :

    
#     for i in ages :
#         print(i)

#     def Enter_age() :

#         AGE = input("Enter your age: ")

#         if int(AGE) in i :
#             print("Good Job")
#         else :
#             print("Fair")
    
#     enter_age = Enter_age()

#     print(f"Your input is {enter_age}")
    

# Age()


ages = [ # * Global Variable
    21,
    20,
    19,
    18,
    17
] 

age_limit = 16 

# TODO if age is

def Ages_1() :

    age = True 
    attempt = 2 

    while age :

        Q1 = input("Enter your age: ")

        for i in ages :
            if i == int(Q1) :
                print("UNLOCK🔓") 
                return Q1
        else :
            attempt -= 1
            if attempt > 0 :
                print("Try again")
            else :
                print("Attempt Block")
    
        return None # ! None Understanding 
    # Todo create a 2 attempt block 


    return Q1            

def Main() :

    ages_1 = Ages_1()
    
    if ages is not None :
        print(f"Access granted for age: {ages_1}")
    else:
        print("Access denied")



Main()
        