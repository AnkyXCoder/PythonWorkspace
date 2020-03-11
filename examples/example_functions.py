# find highest even number

def highest_even(*args):
    even_num = 0
    evens = []
    for num in args:
        if (num%2 == 0):
            evens.append(num)
    even_num = max(evens)
    return even_num, evens


print(highest_even(1,2,3,4,5,8,15,18))