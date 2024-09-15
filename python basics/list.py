# List

list1 = [1, 2, 3, 4, 5]
list2 = ["a", "b", "c"]
list3 = ["Hello", "Good", "Morning"]
list4 = [True, False, True, True]
list5 = [1, 2, 3, "a", "b", "Hello", True]

print(list1)
print(list2)
print(list3)
print(list4)
print(list5)


my_inventory = ["sunglasses", "shirts", "t-shirts", "jeans", "watches"]
print(my_inventory)
print(my_inventory[0])
print(my_inventory[1])
print(my_inventory[2])
print(my_inventory[3])
print(my_inventory[4])
# print(my_inventory[5])

# List Slicing

print(my_inventory[1:3])
print(my_inventory[:])
print(my_inventory[1::2])

# Lists can be changed
# strings are immutable, Lists aren't

my_inventory[0] = "laptop"
print(my_inventory)
new_inventory = my_inventory
new_inventory[0] = "mobile"
print("new_inventory: ", new_inventory)
# here changing the new_inventory list have changed the my_inventory list
# which means that when we defined new_inventory = my_inventory we defined that new_inventory is my_inventory
# we are not copying the contents of my_inventory in new_inventory
print("my_inventory: ", my_inventory)

# to copy the contents of my_inventory into new_inventory1
new_inventory1 = my_inventory[:]
new_inventory1[0] = "charger"
print("new_inventory1: ", new_inventory1)
print("my_inventory: ", my_inventory)

print("Length/Elements of new_inventory: ", len(new_inventory))

# Matrix
# list is one dimensional array
# matrix is a (two or more than two dimensional) multidimensional array
matrix = [[1, 4, 3], [2, 5, 6], [7, 8, 9]]

print("matrix is: ", matrix)
print("matrix[0]: ", matrix[0])  # prints first row
print("matrix[1]: ", matrix[1])  # prints second row
print("matrix[2]: ", matrix[2])  # prints third row
print("matrix[0]][0]: ", matrix[0][0])

for i in range(0, 3):
    for j in range(0, 3):
        print("matrix[", i, "]", "[", j, "]: ", matrix[i][j])

# Methods on Lists

basket = ["mango", "apple", "banana"]
# append updates the actual list, doesn't produce a new list, here new_basket
new_basket = basket.append("guava")
print("basket: ", basket)
print("new_basket: ", new_basket)

# insert enters a new element at a specified index in the array
basket.insert(2, "pomogranade")
print("updated basket: ", basket)

# extend list by appending elements given
basket.extend(["grapes", "kiwi"])
print("extended basket: ", basket)

# pop removes last element of the list
basket.pop()
print("pop basket: ", basket)
basket.pop()
print("pop basket: ", basket)
basket.pop(2)  # pop element at the given index of the list
print("pop basket: ", basket)
new_item = basket.pop(3)  # pop method removes element from list and moves into new_item
print("new_item: ", new_item)

# remove the given element value from the list
basket.remove("apple")
print("updated basket: ", basket)

# clear the list
basket.clear()
print("basket: ", basket)

basket = ["mango", "apple", "banana", "guava"]
print("basket: ", basket)
# index gives the position of element
print("banana is at position :", basket.index("banana"))
# searching in the specified range
# print("banana is at position :",basket.index("guava", 0,2))
# if the search item is not available in the given range, compiler gives an error
print("is banana in basket? ", "banana" in basket)
print("is mango in basket? ", "mango" in basket)
print("is pomogranade in basket? ", "pomogranade" in basket)

print(basket.count("banana"))
print(basket.count("a"))

num_list = [1, 2, 3, 4, 5, 1, 5, 6, 7, 8, 4, 4]
print("num_list: ", num_list)
print("Count of 4 in num_list: ", num_list.count(4))

# sorting the list elements in ascending order
print("basket: ", basket)
print("sorted basket: ", sorted(basket))  # doesn't update the actual list
print("basket: ", basket)

new_basket = basket.copy()
new_basket.sort()
print("new_basket: ", new_basket)
print("basket: ", basket)

basket.sort()  # updates the actual list
print("basket: ", basket)
num_list.sort()  # updates the actual list
print("num_list: ", num_list)

# reversing the list, just changes the index of each elements
basket.reverse()  # using methods
print("reversed basket: ", basket)
print(
    "reversed basket: ", basket[::-1]
)  # using list slicing, but this creates a new list, doesn't update the actual list

# create a list of number
print(list(range(1, 20)))
print(list(range(20)))

# join method   # can be used to combine list into a string
sentence = "~"  # try this with '', ' ','@', '#', '~' etc
new_sentence = sentence.join(["hi", "my", "friend"])  # create a new sentence
print("sentence is: ", sentence)
print("new_sentence is: ", new_sentence)

# list unpacking
numbers = [1, 2, 3]
print(numbers)
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)

a, b, c, *other = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(a)
print(b)
print(c)
print(other)


a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(a)
print(b)
print(c)
print(other)
print(d)

# use of None

attributes = None
print(attributes)
