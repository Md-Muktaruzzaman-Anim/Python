# b = "hello world" # Strings are immutable

# m[3] = "k" # You cannot do this

# a = len(b)
# print(a) # output: 4, because Anim has 4 characters

# Changing Case

# print("Changing Case:")
# print(b.upper())      # Output: "HELLO WORLD"
# print(b.lower())      # Output: "hello world"
# print(b.capitalize()) # Output: "Hello world"
# print(b.title())      # Output: "Hello World"

# Removing Whitespace

# print("Removing Whitespace:")
# text = " hello world "
# print(text.strip())  # Output: "hello world"
# print(text.lstrip()) # Output: "hello world "
# print(text.rstrip()) # Output: " hello world"

# Finding and Replacing

# text = "Python is fun, fun and fun"
# print(text.find("is")) # Output: 7 index of first occurence.
# print(text.replace("fun", "awesome")) # Output: Python is awesome, awesome and awesome
# Anim = "He is a bad, bad and bad player"
# print(Anim.replace("bad", "good")) # Output: He is a good, good and good player

# sentence = "I sing in Bengali"
# words = sentence.split(" ") # Divide by space
# print(words)

# a = "a=b=c"
# print(a.split("="))

text = "Apples,Bananas,Pineapples"
print(text.split(","))
print(",".join(['Apples', 'Bananas', 'Pineapples']))

# Checking String Properties

text = "Python123"

print(text.isalpha()) # Whether there are only letters (A-Z, a-z) # Output: False
print(text.isdigit()) # Whether there are only numbers (0-9) # Output: False
print(text.isalnum()) # Whether there are letters + numbers (no spaces/special characters) # Output: True
print(text.isspace()) # Whether there are only spaces/whitespace # Output: False