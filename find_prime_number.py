def check_for_prime_number(z):
    j = 0
    for i in range(2, (z + 1)):
        if (z % i) is 0:
            j = j + 1
            print ("Given number is divisible by ",i)
    if (j is 1):
        print ("Given number is a Prime Number.\n")
    else :
        print ("Given number is not a Prime Number.\n")

a = int (input ("Enter a number to check whether it is Prime Number or not:"))

check_for_prime_number(a)