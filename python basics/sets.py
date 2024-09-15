# Set
# unordered collections of unique objects

my_set = {1, 2, 3, 4, 5}
print(my_set)


my_set = {1, 2, 3, 4, 5, 5, 5, 3, 2}
print(my_set)

# methods

# add method
my_set.add(100)
print(my_set)
my_set.add(2)
print(my_set)

# using set in lists
my_list = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 3, 3, 4, 5]
print(set(my_list))

# accessing elements of set
print(5 in my_set)

# checking length of set
print(len(my_set))

# converting set to a list
print(list(my_set))

# copy method
new_set = my_set.copy()
my_set.clear()
print(my_set)
print(new_set)


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8, 9, 10}
print("set1: ", set1)
print("set2: ", set2)

# difference method
# difference of set1 with respect to set2: (these elements are not present in set2)
print("set1.difference(set2): ", set1.difference(set2))
# difference of set2 with respect to set1: (these elements are not present in set1
print("set2.difference(set1): ", set2.difference(set1))

# intersection method
# intersection gives elements common between set1 and set2
print("set1.intersection(set2): ", set1.intersection(set2))  # print(set1 & set2)

# isdisjoint method
# isdisjoint method gives False if the sets are overlapping
print("set1.isdisjoint(set2): ", set1.isdisjoint(set2))

# difference update method
# set1.difference_update(set2) removes set2 elements from set1
set1.difference_update(set2)
print(set1)

# discard method
# discarding 5 from set1
set1.discard(5)
print(set1)

# union method
# union creates a new set and elements of new set consists the elements of both the sets removing any duplicates
print("set1.union(set2): ", set1.union(set2))  # print(set1 | set2)


set1 = {4, 5}
set2 = {4, 5, 6, 7, 8, 9}

# issubset method
# checks if the given set is a subset of other set or not
print("set1.issubset(set2): ", set1.issubset(set2))
print("set2.issubset(set1): ", set2.issubset(set1))

# issuperset method
# checks if the given set is a superset of other set or not
print("set2.issuperset(set1): ", set2.issuperset(set1))
print("set1.issuperset(set2): ", set1.issuperset(set2))
