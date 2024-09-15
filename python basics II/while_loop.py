# while loop

i = 0
while i < 5:
    print(i)
    i += 1
    if i > 3:
        break

i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("all the work is done")


my_list = [1, 2, 3]

for element in my_list:
    print(element)
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

while True:
    input("say something: ")
    break

while True:
    response = input("say something: ")
    if response == "bye":
        break
