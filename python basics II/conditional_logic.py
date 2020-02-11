

is_old = True
is_licensed = True

#  If loop
if (is_old):
    print('You are old enough to drive a vehicle.')

is_old = False

#  If ... else ... loop
if (is_old):
    print('You are old enough to drive a vehicle.')
else:
    print('You are not of age.')


#  If ... elif ... else ... loop
if (is_old):
    print('You are old enough to drive a vehicle.')
elif (is_licensed):
    print('You can drive a vehicle.')
else:
    print('You are not of age.')

is_old = False
is_licensed = True
#  If ... elif ... else ... loop
if is_old and is_licensed:                  # if (is_old & is_licensed):
    print('You are old enough and licensed to drive a vehicle.')
elif is_old or is_licensed:                # elif (is_old | is_licensed):
    print('You are either not of age or not licensed, but You can drive a vehicle.')
else:
    print('You can not drive.')

print('Test Complete.')



# All values are considered "truthy" except for the following, which are "falsy":

#     None
#     False
#     0
#     0.0
#     0j
#     Decimal(0)
#     Fraction(0, 1)
#     [] - an empty list
#     {} - an empty dict
#     () - an empty tuple
#     '' - an empty str
#     b'' - an empty bytes
#     set() - an empty set
#     an empty range, like range(0)
#     objects for which
#         obj.__bool__() returns False
#         obj.__len__() returns 0

