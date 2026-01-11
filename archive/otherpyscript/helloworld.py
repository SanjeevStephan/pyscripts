from personal import Greetings as greet

fname = "sanjeev stephan"
lname = "murmu"
site = "https://www.google.com"
lang = 'python '
lang2 = ' java'


full_name  = f'{fname} {lname}'
greet.Hello(full_name.upper())
greet.Hello(full_name.lower())
greet.Hello(fname.title())
## print("Hello world")


print(lang.rstrip())
print(lang2.lstrip())
print(site.removeprefix('https://'))
