global x,y
def operation(z):
    print ("You have selected \"",z,"\" operator.\n")
    if (z == "+"):
        print (x, " + ", y, " = ", x + y)
    elif (z == "-"):
        print (x, " - ", y, " = ", x - y)
    elif (z == "x"):
        print (x, " x ", y, " = ", x * y)
    elif (z == "/"):
        print (x, " / ", y, " = ", x / y)
    elif (z == "^"):
        print (x, " ^ ", y, " = ", x ** y)
    else :
        pass

print ("This program does basic mathematical manipulation between two numbers.\n")
x = int (input("Enter number 1: "))
print ("Okay, got it")
y = int (input("Enter number 2: "))
print ("Yup, that's it")

print ("Select operator from the following list:\n+ for addition\n- for subtraction\nx for multiplication\n/ for division\n^ for exponent\n")

z = input("Waiting for operator: ")
operation(z)