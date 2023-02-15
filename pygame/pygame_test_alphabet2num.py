#  Alphabet position in a string
#  Python program that takes a string and replaces all the characters with their respective numbers.

def test(text):
    return ' '.join(str(ord(i)-96) for i in text.lower() if i.isalpha())    

    
word = "Python"
print("Original Word:", word)
print("Alphabet position in the said string:")
print(test(word))
word = "Java"
print("\nOriginal Word:", word)
print("Alphabet position in the said string:")
print(test(word))
word = "Python Tutorial"
print("\nOriginal Word:", word)
print("Alphabet position in the said string:")
print(test(word)) 
