
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

    while age :

        Q1 = input("Enter your age: ")

        for i in ages :
            if i == int(Q1) :
                print("UNLOCK🔓") 
                age = False
                break
        else :
            print("Try again")

    # Todo create a 2 attempt block 


    return Q1            

def Main() :

    ages_1 = Ages_1()
    




Main()
        