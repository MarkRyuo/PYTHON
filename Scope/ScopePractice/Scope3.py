
# TODO Scope


variable = "This is Global Variable"


def Variable() :

    variable = "This is a Local Variable"
    print(variable)

    def InnerVariable() :

        variable = "Local varible in a Nested function"
        print(variable)

    InnerVariable()
    

Variable()

print(variable)

