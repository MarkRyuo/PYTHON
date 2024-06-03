# Understanding about in Scope 


variable_age = 21 # * Global Variable 

def Age() :

    variable_age = 19 # * Local Variable  
    
    QUESTION1 = input("What is your age?: ")
    QUESTION1 = int(QUESTION1)

    if QUESTION1 == variable_age :
        print("Your age is not bad!")
    else :
        print(f"{QUESTION1} is bad {QUESTION1} is good")
        

Age()