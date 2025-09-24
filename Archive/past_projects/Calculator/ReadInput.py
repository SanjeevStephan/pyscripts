from ShowInfo import show

pyFileName = "ReadInput"
show(pyFileName,"Reading User Input ")

def getInput():
    userinput = input("Enter Any Number (0-9) : ")
    show(pyFileName,"You Have Entered : {} " .format(userinput))

# getInput()