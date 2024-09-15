# functions
def say_hello():
    print("Hello")


def say_hello_name(name, country):  # parameters: when defining functions
    print(f"Hello, {name}.Are you from {country}?")


# positional arguments
user_name = "Danny"
user_country = "USA"
say_hello_name(user_name, user_country)  # arguments: when calling/invoking functions
say_hello_name("Johnny", "Canada")
say_hello_name("Australia", "Rufus")  # inappropriate print

# keyword arguments
say_hello_name(country="Europe", name="Luis")


# default parameters
def say_hello_self(name, country, self="Unknown"):  # parameters: when defining functions
    print(f"Hello,{name}. Are you from{country}? I am {self}.")


say_hello_self("Roger", "Canada", "Maximus")
say_hello_self("Roger", "Canada")


def sum_numbers(num1, num2):
    return num1 + num2


total = sum_numbers(50, 20)
print(total)
print(sum_numbers(20, total))
print(sum_numbers(20, sum_numbers(30, 10)))

tree_pattern = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

x_pattern = [
    [1, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 1],
]

y_pattern = [
    [1, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]


# function to display pixel image
def display_pixel_image(pattern):
    # docstring : hovering on the function will give you information about the function that is entered here
    """Info: This function prints the pixel image pattern given as an argument.
    The input argument must be an array of any size.
    """
    # docstring end
    for row in pattern:
        for element in row:
            if element:
                print("*", end="")
            else:
                print(" ", end="")
        print("")


display_pixel_image(tree_pattern)
display_pixel_image(x_pattern)
display_pixel_image(y_pattern)

# display function info
print(display_pixel_image.__doc__)


# *args and **kwargs
# *args is used when function is to be used for more than one arguments
def super_func(*args, **kwargs):
    print("printed as arguments", *args)
    print("printed as sets", args)
    print("printed as arguments", kwargs)
    addition = sum(args)
    total = 0
    for items in kwargs.values():
        total += items
    return addition, total


print(super_func(10, 20, 30, 40, 60, 90, num1=5, num2=7))

# Rule of order: parameters, *args, default parameters, **kwargs


def another_super_func(name, *args, greet="hi", **kwargs):
    print("name is:", name)
    print("greetings: ", greet)
    print("printed as arguments", *args)
    print("printed as sets", args)
    print("printed as arguments", kwargs)
    addition = sum(args)
    total = 0
    for items in kwargs.values():
        total += items
    return addition, total


print(another_super_func("john", 10, 20, 30, 40, 60, 90, num1=5, num2=7))
