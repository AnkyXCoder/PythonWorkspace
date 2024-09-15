# Create a class and constructors


# Abstraction
# create an object
class PersonalCharacter:
    # global attribute
    _membership = True

    # constructor
    def __init__(self, name="anonymous", age=0, strength=100):  # dunder method
        """This is a constructor using __init__ which is called a duncder method.
        This constructor is called every time an object is created.
        It instantiates the object with the given attributes of the class.
        Able to access data and properties unique to each instance."""
        # attributes
        """Protected members are those members of the class which cannot be accessed outside the class
        but can be accessed from within the class and it’s subclasses."""
        self._name = name  # to make attribute protected
        self._age = age  # to make attribute protected
        """Private members are similar to protected members, the difference is that the class members declared private
        should neither be accessed outside the class nor by any base class."""
        self.__strength = strength  # to make attribute private


# instantiate
person1 = PersonalCharacter("Andy", 25)
person2 = PersonalCharacter("Cindy", 22)

# location of object in memory
print(person1)
print(person2)

# getting details of the objects
print(person1._name, person1._age, "membership", person1._membership)
print(person2._name, person2._age, "membership", person2._membership)
