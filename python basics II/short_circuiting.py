# Short Circuiting

is_friend = True
is_user = False

if is_user and is_friend:           # short circuit condition   False and (True) not checked
    print("can message")

if is_friend or is_user:            # short circuit condition   True and (False) not checked
    print("may message")