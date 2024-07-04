"""
python code to print the current date in the format dd--mm--yyyy such as '15 February 2023'
You can use the datetime module to get the current date and format it as a string in the desired format. Here's an example code:
"""

import datetime

def getCurrentDate():
    # Get the current date
    today = datetime.date.today()

    # Format the date as a string in the format dd Month yyyy
    date_str = today.strftime("%d %B %Y")

    # Print the date string
    print(date_str)
    return date_str #will return the date in the format (15 February 2023.) | when 'getCurrentDate()' method/function is called


"""
In this code, we first use the datetime.date.today() function to get the current date. 
We then use the strftime() method to format the date as a string in the format "dd Month yyyy". 
The %d format code is used to display the day of the month as a zero-padded two-digit number, %B is used to display the full name of the month, and %Y is used to display the year with century.

Finally, we print the formatted date string to the console. 
This would output something like 15 February 2023.

"""