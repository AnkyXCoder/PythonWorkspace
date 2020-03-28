#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name = 'Unknown', age = 0):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat("Cindy", 2)
cat2 = Cat("Lily", 1)
cat3 = Cat("Tommy", 3)

# 2 Create a function that finds the oldest cat
def oldest_cat(*args):
    return max(args)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f'The oldest cat is {oldest_cat(cat1.age, cat2.age, cat3.age)} years old.')