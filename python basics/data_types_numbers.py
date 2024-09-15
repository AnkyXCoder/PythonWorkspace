# Fundamental Data Types: Numbers
# Data Types: int and float

print("The Data Type of 3 is ", type(3))
print("The result of 3 + 4 is ", (3 + 4), " and Data Type is ", type(3 + 4))
print("The result of 3 - 4 is ", (3 - 4), " and Data Type is ", type(3 - 4))
print("The result of 3 * 4 is ", (3 * 4), " and Data Type is ", type(3 * 4))
print("The result of 3 / 4 is ", (3 / 4), " and Data Type is ", type(3 / 4))
print("The result of 3 // 4 is ", (3 // 4), " and Data Type is ", type(3 // 4))
print(
    "The result of 33 // 4 is ",
    (33 // 4),
    " which is quotient and Data Type is ",
    type(33 // 4),
)
print(
    "The result of 33 % 4 is ",
    (33 % 4),
    " which is remainder and Data Type is ",
    type(33 % 4),
)
print(
    "The result of 3 + (11 / 4) is ",
    (3 + (11 / 4)),
    " and Data Type is ",
    type(3 + (11 / 4)),
)
print("The result of 3 ** 4 is ", (3**4), " and Data Type is ", type(3**4))
print("This Data Type of 3.14 is ", type(3.14))
print("This Data Type of 3+4j is ", type(3 + 4j))

# math functions
print(round(18.754987, 1))
print(round(18.754987, 2))
print(round(18.754987, 3))
print(abs(3.9))
print(abs(-3.9))

# operator precedence

# () : parenthesis
# ** : square
# / : division
# * : multiplication
# + : addition
# - : subtraction

# Test with following examples
print((5 + 4) * 10 / 2)
print(((5 + 4) * 10) / 2)
print((5 + 4) * (10 / 2))
print(5 + (4 * 10) / 2)
print(5 + 4 * 10 // 2)

# decimal to binary
print(bin(10))
print(bin(80))
print(bin(8))
print(bin(5))

# binary to decimal
print(int("0b101", 2))
print(int("0x01", 16))
print(int("0x10", 16))
print(int("0x101", 16))
print(int("0x1010", 16))

# assignment
a, b, c = 1, 2, 3
print(a, b, c)
print(a)
print(b)
print(c)
