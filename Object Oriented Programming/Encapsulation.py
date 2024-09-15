# Create a class and constructors


# Abstraction
# create an object
class PersonalCharacter:
    # global attribute
    _membership = True

    # constructor
    def __init__(self, name="anonymous", age=0):  # dunder method
        """This is a constructor using __init__ which is called a duncder method.
        This constructor is called every time an object is created.
        It instantiates the object with the given attributes of the class.
        Able to access data and properties unique to each instance."""
        # attributes
        self._name = name  # to make attribute protected
        self._age = age  # to make attribute protected
        self.__

    # Encapsulation
    def run(self):  # object method
        print("run", self._name)

    def shout(self):  # object method
        print(f"My name is {self._name} and I am {self._age} old.")

    # note that adding_things and adding_things2 is defined with @classmethod and @staticmethod respectively
    # so it can be used without instantiating an object
    # class method take into consideration class attributes
    @classmethod
    def adding_things(cls, num1, num2):
        # docstring for classmethod decorator
        """Class methods are created using the @classmethod decorator.
        Class methods don’t need self as an argument, but they do need a parameter called cls.
        This stands for class, and like self, gets automatically passed in by Python.
        Can access limited methods in the class. Can modify class specific details.
        """
        return cls("Ted", num1 + num2)

    # static method won't care about class attributes
    @staticmethod
    def adding_things2(num1, num2):
        # docstring for staticmethod decorator
        """The @staticmethod decorator was used to tell Python that this method is a static method.
        Static methods are methods that are related to a class in some way, but don’t need to access any class-specific data.
        You don’t have to use self, and you don’t even need to instantiate an instance.
        Cannot access anything else in the class. Totally self-contained code.
        """
        return num1 + num2


# instantiate
person1 = PersonalCharacter("Andy", 25)
person2 = PersonalCharacter("Cindy", 22)

# location of object in memory
print(person1)
print(person2)

# getting details of the objects
print(person1._name, person1._age, "membership", person1._membership)
print(person2._name, person2._age, "membership", person2._membership)

# using object method
person1.run()
person2.run()

# using object method
person1.shout()
person2.shout()

# object method that can be used without Instantiating an object
print(PersonalCharacter.adding_things(2, 3))
