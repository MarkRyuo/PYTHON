
# TODO Scope


variable = "This is Global Variable"


def Variable() :

    variable = "This is a Local Variable"

    def InnerVariable() :

        variable = "Local varible in a Nested function"

    InnerVariable()
    

Variable()