# counter
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum = 0
for number in my_list:
    sum = sum + number
    print(sum)


print("Final answer is:", sum)


# range

print(range(100))
print(range(0, 100))

for number in range(0, 10):
    print(number)
    print("counter is:", number)

for _ in range(0, 10):
    print(_)

for num in range(0, 10, 2):
    print(num)

for num in range(10, 0, -1):
    print(num)

for _ in range(2):
    print(list(range(5)))
