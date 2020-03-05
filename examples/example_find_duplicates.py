# Finding Duplicates in the list

given_list = ['a', 'b', 'c', 'd', 'a', 'e', 'b', 'h', 'm', 'm', 'p']

duplicates = []

for value in given_list:
    if given_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print ("duplicate values are:", duplicates)