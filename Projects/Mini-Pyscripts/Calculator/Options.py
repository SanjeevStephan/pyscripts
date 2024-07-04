from ShowInfo import show

show("Option","Displaying Options")

def displayOptions():

    operators = dict(
        add="Press ( A )",
        substract="Press ( S )",
        Divide="Press ( D )",
        Multiply="Press ( M )"
    )

    for key,value in operators.items():
        print("{1} to {0}" .format(key,value))


# displayOptions()