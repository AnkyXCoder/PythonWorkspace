# 1. Write a code that check whether age is (< 18), (= 18), or (> 18).
# 2. If age is < 18: display "Sorry, you are too young to drive this car. Powering off"
# 3. If age is = 18: "Congratulations on your first year of driving. Enjoy the ride!"
# 4. If age is > 18: "Powering On. Enjoy the ride!"
# 5. Wrap this code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age.
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function every time?

# 6. Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age.
# also make this function such that the default age is set to 0 if no argument is given.


def checkDriverAge(age=0):
    print(age)
    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!")
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")


checkDriverAge()
checkDriverAge(17)
checkDriverAge(92)
