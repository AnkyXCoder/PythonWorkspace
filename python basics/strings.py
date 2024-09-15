# Strings

first_name = "Ankit"
last_name = "Modi"

print(first_name)
print(last_name)

full_name = first_name + last_name
print(full_name)

# printing name with spaces

full_name = first_name + " " + last_name
print(full_name)

# OR you can print it like this also
# with no difference
print(first_name + " " + last_name)

# when you want to write long strings, you can use ''' or """

long_string = """What do you want to do today evening??
let's go to theatre to watch a fun movie....
okay, let's go"""

print(long_string)

long_string1 = """What do you want to do today evening??
let's go to theatre to watch a fun movie....
okay, let's go"""

print(long_string1)

# below are the examples of string concatenation
# use type() to get the type of variable
print("Printing,", "C", " and its type is ", type("C"))

print("Printing,", "Hello", " and its type is ", type("Hello!"))

print("Printing,", 100, " and its type is ", type(100))


# type conversion

# printing integer and it's type
a = 100
b = str(a)
c = int(b)
print(a, type(a))

# converting integer to string and printing it's type
print(b, type(b))

# converting integer to string and and back to integer printing it's type
print(c, type(c))


# Escape Sequences
weather = "it's sunny"
print(weather)

# note the inverted commas
weather = "it's sunny"  # here \' is used to print the '
print(weather)

weather = 'it\'s "kind of" sunny'  # here \" is used to print "
# whenever \ is used whatever comes after \ is used as string
print(weather)

# \t means tab
# \v means vertical tab
# \n means a new line
# \

weather = 'it\'s \t"kind\nof"\vsunny'
print(weather)


# formatted strings

name = "John"
age = 52
# note that printing automatically adds space between two different types
# method - 1
print("\nPrinting using method 1:")
print(f"Hi {name}. You are {age} years old.", "Have a nice day ahead.")

# method - 2
# note the behaviour
# the following also does the same job
print("\nPrinting using method 2:")
print("Hi {}. You are {} years old. Have a nice day ahead.".format(name, age))
# checking numbering of the data being printed
print("Hi {1}. You are {0} years old. Have a nice day ahead.".format(name, age))
print("\nCorrection in printing using method 2:")
print("Hi {0}. You are {1} years old. Have a nice day ahead.".format(name, age))

# you can change the data to be printed in line
# method - 3
print("\nPrinting using method 3:")
print("Hi {new_name}. You are {new_age} years old. Have a nice day ahead.".format(new_name="Hemangi", new_age=24))

# Some more examples
print("Hello {}, your balance is {}.".format("Cindy", 50))
print("Hello {0}, your balance is {1}.".format("Cindy", 50))
print("Hello {name}, your balance is {amount}.".format(name="Cindy", amount=50))
print("Hello {0}, your balance is {amount}.".format("Cindy", amount=50))

# String Indexes

print("\nString Indexes Example\n")

greeting = "Morning, Andy!"
print("Printing every element of the string:", greeting)
length_str = len(greeting)
print(f"length of string '{greeting}' is : {length_str}")
for i in range(14):
    print(f"greeting[{i}] {greeting[i]}")


# String Slicing
# [start:stop]
# printing start to 3th characters only
print(greeting[0:3])
print(greeting[0:5])
print(greeting[0:7])

# [start:stop:stepover]
print(greeting[::1])
print(greeting[::2])
print(greeting[::3])

# checking with negative number
print(greeting[-1])
print(greeting[-4])

# printing string in reverse
print(greeting[::-1])
print(greeting[::-2])

# Some more examples
python = "I am PYTHON"

print(python[1:4])
print(python[1:])
print(python[:])
print(python[1:100])
print(python[-1])
print(python[-4])
print(python[:-3])
print(python[-3:])
print(python[::-1])

# Strings in Python are Immutable
# Uncomment the below expression and running the script will generate a compiler error
# greeting[0] = "X"
# you must completely reassign the new value

print("\nUsing Striong Methods\n")

print(greeting[0 : len(greeting)])

quote = "to be or not to be"
# to capitalize the string
print(quote.capitalize())
# to convert all the characters in Upper case
print(quote.upper())
# to convert all the characters in Lower case
print(quote.lower())
# to find first occurrence of "be" in the given string
print(quote.find("be"))
# to find first occurrence of "to" in the given string
print(quote.find("to"))
# to replace "be" with "me"
print(quote.replace("be", "me"))
# as strings are immutable
print("quote: ", quote)

quote2 = quote.replace("be", "me")
print("quote2: ", quote2)
