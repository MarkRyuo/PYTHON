
# * Varible or Literal
# * Loop


ages = [ # * Global Variable
    21,
    20,
    19,
    18,
    17
]  
# ages = str(ages) # ! Fix this 

def Age() :

    
    for i in ages :
        print(i)

    def Enter_age() :

        AGE = input("Enter your age: ")

        if int(AGE) in i :
            print("Good Job")
        else :
            print("Fair")
    
    enter_age = Enter_age()

    print(f"Your input is {enter_age}")
    

Age()


        