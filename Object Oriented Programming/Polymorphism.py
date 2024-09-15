# Polymorphism
# Different Object Classes can share Method Names
# User
# - Wizard
# - Archer
# - Swordsman
#
# All the above mentioned Objects are having the method "attack()". This method  is having different functionalities as called from
# different classes. It means that the same "attack()" method gives different Output.
# By using Polymorphism, we can define a single "attack()" method which will give Output as per the Object.


# Introspection: The ability to determine the type of an Object in Runtime.


# parent class or parent object
class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("User Signed In.")

    def attack(self):
        print("do nothing.")


# children classes or sub-classes or derived classes
# child objects Inherits all the attributes and methods of the parent object

# child object Wizard


class Wizard(User):
    def __init__(self, name, power, email):
        User.__init__(self, email)  # Method 1 to add email in the object
        self._name = name
        self._power = power

    def attack(self):
        User.attack(self)
        print(f"attacking with power of {self._power}")


# child object Archer


class Archer(User):
    def __init__(self, name, num_arrows, email):
        # Method 2 to add email in the object, super() allows us to access User Class
        super().__init__(email)
        self._name = name
        self._num_arrows = num_arrows

    def attack(self):
        User.attack(self)
        print(f"attacking with arrows: {self._num_arrows}")


# child object Swordsman


class Swordsman(User):
    def __init__(self, name, power, email):
        User.__init__(self, email)
        self._name = name
        self._power = power

    def attack(self):
        User.attack(self)
        print(f"attacking with sward power of {self._power}")


# Instantiating the wizard object
wizard1 = Wizard("Merlin", 50, "merlin@wizard.com")

# Instantiating the archer object
archer1 = Archer("Robin", 100, "robin@archer.com")

# Instantiating the swordsman object
swordsman1 = Swordsman("Hercules", 80, "hercules@swordsman.com")

# using method in wizard object inherited from parent object
wizard1.sign_in()

# using method in archer object inherited from parent object
archer1.sign_in()

# using method in swordsman object inherited from parent object
swordsman1.sign_in()

# using method of wizard object
wizard1.attack()

# using method of archer object
archer1.attack()

# using method of swordsman object
swordsman1.attack()

# getting email of wizard object
print(wizard1.email)

# getting email of archer object
print(archer1.email)

# getting email of swordsman object
print(swordsman1.email)

# getting all the dunder methods, attributes and methods of an instance
print(dir(wizard1))
