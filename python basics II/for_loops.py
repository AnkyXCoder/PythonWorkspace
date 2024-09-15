# For loops

print("For loop in string")
for item in "Python Learning":
    print(item)

print("For loop in list")
for item in [1, 2, 3, 4, 5]:  # list
    print(item)

print("For loop in set")
for item in {1, 2, 3, 4, 5}:  # set
    print(item)

print("For loop in tuple")
for item in (1, 2, 3, 4, 5):  # tuple
    print(item)

print("Nested Loop")
for item in (1, 2, 3, 4, 5):  # tuple
    for x in ["a", "b", "c"]:
        print(item, x)


# iterable - list, dictionary, tuple, set, string
# -> one by one check each item in collection

user = {"name": "John", "age": 56, "can_swim": False}

for item in user.items():
    print(item)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)

for item in user.items():
    key, value = item
    print(key, value)

for key, value in user.items():
    print(key, value)
