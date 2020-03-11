# Scope - what variables I have access to?

# global scope
a = 1

def some_func():
    # function scope, local scope
    a = 5
    return a

print(some_func())
print(a)

# 1 - check for varaible in local scope
# 2 - check for variable in parent scope
# 3 - check for variable in Global scope
# 4 - built-in python functions

def func1():
    # func1 scope, local scope
    a = 3
    def func2():
        # func2 scope, local scope
        return a
    return func2()

print(func1())
print(a)

def func3(b):
    # function scope, local scope
    # parameter b comes into local scope
    print(b)

func3(300)

total = 0

def count(total):
    total += 1
    return total

print(count(count(total)))


def outer():
    x = 'local'
    def inner():
        nonlocal x
        x = 'non-local'
        print('inner x: ', x)
    
    inner()
    print('outer x:', x)

outer()