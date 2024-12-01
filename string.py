
from operator import concat

#String can be used within single quote or double quote
greeting = "hello"
f_name = 'John'

#Single and Double quotation using in a single statement
message = "This is John's pen."
quote = 'Harry said, "The world is become destroy."'

#upper() method
print(f_name.upper()) #invoking a method
print(f_name.lower())
print(message.title())

#String Concatination
print(greeting + f_name)
print(concat(greeting,f_name)) #expect only two argument

#Blank space characters
print("hello \n world") #/n is for new line
print("hello \t world") #/t is for tab

#Length of a string
print(len(message))

#Find a character in a string
print(message.find("l"))
print(message.find("#"))
print(message.find("s"))

#count
print(message.count("i"))