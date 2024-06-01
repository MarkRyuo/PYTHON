



# * Scope (global, local)
# * Function(def) - Nested Function 


# global_variable = "Hello World Global Variable" # * Global variable 

def Outer() :

    global_variable = "Hello local variable"
    print(global_variable)
    def Inner() :

        global_variable = "Hello Inner variable in Nested Function"
        print(global_variable)
    Inner()

Outer()

# print(global_variable)



global_variable = 21 # * Global variable 

def Outer() :

    global_variable = 20
 
    def Inner() :

        global_variable = 19 # * Variable in Inner is age 19
    return global_variable

    Inner()

Outer()



print(f"In Global variable my age is: {global_variable}")