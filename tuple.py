# Tuple
# Tuples are immutable lists

my_tuple = (1,2,3,4,5)
print(my_tuple)
print(my_tuple[1])
print(5 in my_tuple)
print(9 in my_tuple)

user = {
    'greetings' : "hello",
    'basket' : [1,2,3],
    'weight' : 70,
}
print(user.items())

user2 = {
    (1,2) : "hello",
    'basket' : [1,2,3],
    'weight' : 70,
}
print(user2[(1,2)])

new_tuple = my_tuple[1:2]
print(new_tuple)

x,y,z, *other = my_tuple
print(x)
print(y)
print(z)
print(other)

# Tuple methods

# count method
print(my_tuple.count(5))
my_tuple = (1,2,3,4,5,5)
print(my_tuple.count(5))            # counts of the elements having value 5

# index method
print(my_tuple.index(5))            # first index of the element

# length method
print(len(my_tuple))