



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



global_variable = "Hello World Global Variable" # * Global variable 

def Outer() :

    global_variable = "Hello local variable"
    print(global_variable)
    def Inner() :

        global_variable = "Hello Inner variable in Nested Function"
        print(global_variable)
    Inner()

Outer()

print(global_variable)