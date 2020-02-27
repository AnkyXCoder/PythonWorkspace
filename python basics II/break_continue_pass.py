# break

my_list = [1,2,3,4,5,6,7]

for element in my_list:
    print(element)
    if (element == 3):
        break

i = 0
while(i < len(my_list)):
    print(my_list[i])
    if (my_list[i] == 5):
        break
    i += 1

# continue

my_list = [1,2,3,4,5,6,7]

for element in my_list:
    print(element)
    if (element == 3):
        continue


# pass
i = 0
while(i < len(my_list)):
    print(my_list[i])
    if (my_list[i] == 5):
        # still thinking about it
        pass
    i += 1
