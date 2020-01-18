# Birth Year Calculating Exercise

birth_year = input("What year were you born?")
print(type(birth_year))
present_year = 2020
print(type(present_year))
print("Both data types are different. That's why, You have to typecast the entered data to int.")
age = present_year - int(birth_year)
print(f'You are {age} years old.')