# Understanding about in Scope 


variable_age = 21 # * Global Variable 

def Age() :

    # variable_age = 19 # * Local Variable  
    
    question1 = input("What is your age?: ")
    question1 = int(question1)

    if question1 == variable_age :
        print("Your age is not bad!")
    else :
        print(f"{question1} is bad {variable_age} is good")
        

Age()