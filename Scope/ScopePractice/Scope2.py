
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


# * 1 

def Ages() :

    Q1 = input("Enter a Number: ")

    for i in ages :

        if int(Q1) == i :
            print("Unlock")
            break
        else :
            print("Lose")

# Ages()

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
                 
                

Ages_1()
        