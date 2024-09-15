# using this list

# Example 1
basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# 1. Remove the Banana from the list
basket.remove("Banana")

# 2. Remove "Blueberries" from the list.
basket.remove("Blueberries")

# 3. Put "Kiwi" at the end of the list.
basket.append("Kiwi")

# 4. Add "Apples" at the beginning of the list
basket.insert(0, "Apples")

# 5. Count how many apples in the basket
basket.count("Apples")

# 6. empty the basket
basket.clear()

print(basket)

# Example 2
new_list = ["a", "b", "c"]
print(new_list[1])
print(new_list[-2])
print(new_list[1:3])
new_list[0] = "z"
print(new_list)

my_list = [1, 2, 3]
bonus = my_list + [5]  # created a  new list by copying the contents of my_list
my_list[0] = "z"  # updates my_list only not bonus
print(my_list)
print(bonus)

# Example 3
# method 1
friends = ["Simon", "Patty", "Joy", "Carrie", "Amira", "Chu"]
print(friends)
new_friend = ["Stanley"]
friends.sort()
print(friends + new_friend)

# method 2
friends_list = ["Simon", "Patty", "Joy", "Carrie", "Amira", "Chu"]
print(friends_list)
new_friend = ["Stanley"]
friends.extend(new_friend)
print(friends)

# Example 4
# using this list:                          # matrix interpretation
basket = [  #          column1,   column2,   column3
    "Banana",  # row1     Banana,           ,
    [
        "Apples",
        ["Oranges"],
        "Blueberries",
    ],  # row2     Apples,    Oranges, Blueberries
]
# access "Oranges" and print it:
print(basket[1][1][0])
