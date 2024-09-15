# Dictionary
# data structure that stores data in terms of keys and values as pairs

# list is a sorted data structure, list of people in queue
# dictionary has no order, list of a persons belongings in wardrobe

user2 = dict(name="Johny")
print(user2)

#  another way of creating dictionary

dictionary = {
    # immutable keys types
    "a": 45,
    "b": 99,
    "c": True,
    "d": [1, 2, 3],
    "e": "here is your string",
    123: "hi user",
    True: "hello",
    # [100] : True               can not be used as lists are mutable, can be manipulated
}

# Getting values from keys

print("dictionary contains:", dictionary)
print(dictionary["a"])
print(dictionary["b"])
print(dictionary["c"])
print(dictionary["d"])
print(dictionary["e"])
print(dictionary[123])
print(dictionary[True])


dictionary[123] = "hi admin"  # replaces the previous value
print(dictionary[123])

my_list = [
    {"a": [1, 2, 3], "b": "hello", "c": True},
    {"a": [4, 5, 6], "b": "there", "c": False},
]

# Getting values from keys
print(my_list[0]["a"][2])
print(my_list[1]["a"][1])

# Dictionary methods

user = {
    "greetings": "hello",
    "basket": [1, 2, 3],
    "weight": 70,
}

print(user["basket"])

# get method
# to check whether key 'age' is available in user or not
print(user.get("age"))
# get age from user, if age is not available in user, then displays 55
print(user.get("age", 55))
# get weight from user, if weight is not available in user, then display 60
print(user.get("weight", 60))

# search for keys in dictionaries
print("does basket available in user?", "basket" in user)
print("does size available in user?", "size" in user)
print("does hello available in user?", "hello" in user)

# searching in keys method
print("does basket available in user keys?", "basket" in user.keys())
print("does hello available in user keys?", "hello" in user.keys())

# searching in values method
print("does basket available in user values?", "basket" in user.values())
print("does hello available in user values?", "hello" in user.values())

# searching in items method
print("items in user: ", user.items())
print("does hello available in user items?", "hello" in user.items())

# copying the dictionary method
user3 = user.copy()
print("user3 now contains: ", user3)

# clearing a dictionary
user.clear()  # clears dictionary
print("user is now: ", user)
print("user3 still contains: ", user3)

# pop method
print(user3.pop("weight"))  # pops the item with key "weight"
print(user3)

# popitem method
print(user3.popitem())  # randomly pops any item
print(user3)

# update method
user3.update({"weight": 45})  # updates key to provided value
print(user3)
# updates dictionary with new item if key is not available
user3.update({"age": 15})
print(user3)
