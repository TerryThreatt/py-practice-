# Data Types:

# bool = True or False
# int = 1
# str = "String"
# list = [1,2,3] - ordered sequence of values
# dict = {"first_name": "terry"} - collection of key/values
# None = equal to Null/Nil

is_active = True
print(is_active)

"""
Dynamic typing - Python is highly flexibile about reassigning variables to different types:

"""

## Strings

"""
# Set the message variable equal to any string containing a new-line escape sequence
message = "Hello \n goodbye"

# Add a string to the mountains variable that when printed results in: /\/\/\
# You will need to use an escape sequence more than once!

mountains = "/\\/\\/\\"


# Set the quotation variable to any string that contains an escaped double quotation mark
quotation = "My cat said \"meow\""
"""


## Formating Strings
guess = 8
print(f"your guess of {guess} was incorrect!")
print(f"{guess + 1} is the answer!")

## Old Version - Formatting
formatted = "I've told you {} times already!".format(10)
print(formatted)

## String Indexes - can get the index of each string char
"lol"[0] #=> "l"
"low"[-1] #=> "w"

# Converting Data Types
decimal = 12.56243434
integer = int(decimal) #=> 12

my_list = [1, 2, 3]
my_list_as_a_string = str(my_list) #=> "[1, 2, 3]"
