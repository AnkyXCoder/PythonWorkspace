# functions
def  say_hello():
    print('Hello')

def say_hello_name(name, country):                   # parameters: when defining functions
    print(f'Hello, {name}.Are you from {country}?')

# positional arguments
user_name = "Danny"
user_country = "USA"
say_hello_name(user_name, user_country)                   # arguments: when calling/invoking functions
say_hello_name('Johnny', 'Canada')
say_hello_name('Australia', 'Rufus')                      # inappropriate print

# keyword arguments
say_hello_name(country = 'Europe', name = 'Luis')

# default parameters
def say_hello_self(name, country, self = 'Unknown'):                   # parameters: when defining functions
    print(f"Hello,{name}. Are you from{country}? I am {self}.")


say_hello_self('Roger', 'Canada', 'Maximus')
say_hello_self('Roger', 'Canada')

def sum(num1, num2):
    return num1+num2

total = sum(50,20)
print(total)
print(sum(20, total))
print(sum(20, sum(30,10)))

tree_pattern = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]
# function to display pixel image
def display_pixel_image(pattern):           
    for row in pattern:
        for element in row:
            if (element):
                print ('*', end = '')
            else :
                print (' ', end = '')
        print('')

display_pixel_image(tree_pattern)