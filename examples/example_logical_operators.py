
is_magician = True
is_expert = True

# Method - 1
if is_magician:
    # print("You are a Magician.")
    if is_expert:
        print("You are a master magician.")
    else:
        print("You are not a master magician, but at least you are getting there.")
else:
    print("You need magical powers.")

# Method - 2

if is_magician and is_expert:
    print('You are a master magician.')
elif is_magician and not is_expert:
    print('You are not a master magician. But, at least you are getting there')
elif not is_magician:
    print("You need magical powers.")
