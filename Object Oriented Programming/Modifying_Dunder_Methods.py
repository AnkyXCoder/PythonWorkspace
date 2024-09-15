# Whenever an Object is created and instantiated, it gest access to all the basic Dunder Methods available to it as per Python
# Programming Language.
# By defining the Dunder Method in the Class Encapsulation, the access to Dunder Methods are modified.


class SuperList(list):  # Defining SuperList as the Subclass of the List Class
    def __len__(
        self,
    ):  # This __len__() Dunder Method will be used and the __len__() Dunder Method provided by Python will not be used.
        return 1000


superlist1 = SuperList()

print(len(superlist1))

# Appending Number to the Superlist
superlist1.append(5)
print(superlist1)

# Appending Number to the Superlist
superlist1.append(10)
print(superlist1)

# Getting Number from the Superlist
print(f"superlist1[0]:{superlist1[0]}")
print(f"superlist1[1]:{superlist1[1]}")

# Check if SuperList is a subclass of List
print(f"SuperList is a subclass of List: {issubclass(SuperList, list)}")

# Check if SuperList is a subclass of Tuple
print(f"SuperList is a subclass of Tuple: {issubclass(SuperList, tuple)}")

# Check if SuperList is a subclass of Object
print(f"SuperList is a subclass of Object: {issubclass(SuperList, object)}")
