""" 
.SYNOPSIS
    python code to loop a list of item from dictionary named "pymath_files" in the format [1]-item, [2]-item 


.DESCRIPTION
    
    This Python script loop through the items in a dictionary named pymath_files and print them out in the format [1]-item, [2]-item:. 
    
.PARAMETER

    

.EXAMPLE
    
    
     
.AUTHOR
    
    -Sanjeev Stephan Murmu

.LINK

.NOTES
    

.
-------------------------------|| CODE_BELOW ||-----------------------------
"""
pymath_files = {
    "Random 3 digit multiplicaiton": "file1.py",
    "Random 2 digit multiplication": "file2.py",
    "Random 2 digit substraction from 11 to 99 ": "file3.py"
}
item_num=0

for key, value in pymath_files.items():
    item_num = item_num + 1
    print("[{}] {}".format(item_num,key))

"""
-------------------------------|| CODE_ABOVE ||-----------------------------
------------------------------|| TERMINAL LOG ||----------------------------

PS D:\terminal> python


-------------------------------|| HOW THE SCRIPT WORK ||--------------------
In this example, pymath_files is a dictionary with three key-value pairs. The keys are integers (1, 2, and 3), and the values are strings representing file names ("file1.py", "file2.py", and "file3.py").

Note that the keys can be any immutable data type (such as integers, strings, or tuples), while the values can be any data type (such as strings, integers, lists, or even other dictionaries). The format of the dictionary will depend on the specific use case and the types of data being stored.

In this code, pymath_files.items() returns a list of tuples where each tuple contains a key-value pair from the dictionary. The for loop then iterates through each tuple and unpacks the key and value into the variables key and value, respectively.

The print() function then formats the output string using the str.format() method. The {} placeholders in the format string are replaced with the values of key and value. The [] characters are included in the format string to match the desired output format.

"""
