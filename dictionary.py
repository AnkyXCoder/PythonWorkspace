# Dictionary
# data structure that stores data in terms of keys and values as pairs

dictionary = {
    # immutable keys types
    'a' : 45,
    'b' : 99,
    'c' : True,
    'd' : [1,2,3],
    'e' : 'here is your string',
    123 : 'hi user',
    True : 'hello',
    #[100] : True               can not be used as lists are muttable, can be manipulated
}

# Getting values from keys

print ('dictionary contains:', dictionary)
print(dictionary['a'])
print(dictionary['b'])
print(dictionary['c'])
print(dictionary['d'])
print(dictionary['e'])
print(dictionary[123])
print(dictionary[True])


dictionary[123] = 'hi admin'
print(dictionary[123])

my_list = [
    {
        'a' : [1,2,3],
        'b' : 'hello',
        'c' : True
    },
    {
        'a' : [4,5,6],
        'b' : 'there',
        'c' : False
    }
]

# Getting values from keys
print(my_list[0]['a'][2])
print(my_list[1]['a'][1])

