
# TODO Scope


variable = "This is Global Variable"


def Variable() :

    variable = "This is a Local Variable" # * This is a local variable, sa loob lamang ito ng function magagamit 
    print(variable)

    def InnerVariable() :

        variable = "Local varible in a Nested function"
        print(variable)

    InnerVariable()
    

Variable()

print(variable)

