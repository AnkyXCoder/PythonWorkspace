# Inheritance
# User
# - Wizard
# - Archer
# - Swardsman

# parent class or parent object
class User():
    def sign_in(self):
        print("User Signed In.")

# children classes or sub-classes or derived classes
# child objects Inherits all the attributes and methods of the parent object

# child object Wizard
class Wizard(User):
    def __init__(self, name, power):
        self._name = name
        self._power = power

    def attack(self):
        print(f'attacking with power of {self._power}')

# child object Archer
class Archer(User):
    def __init__(self, name, num_arrows = 0):
        self._name = name
        self._num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: {self._num_arrows}')

# child object Swardsman
class Swardsman(User):
    def __init__(self, name, power):
        self._name = name
        self._power = power

    def attack(self):
        print(f'attacking with sward power of {self._power}')

# Instantiating the wizard object
wizard1 = Wizard('Merlin', 50)

# Instantiating the archer object
archer1 = Archer('Robin', 100)

# Instantiating the swardsman object
swardsman1 = Swardsman('Hercules', 80)

# using method in wizard object inheritted from parent object
wizard1.sign_in()

# using method in archer object inheritted from parent object
archer1.sign_in()

# using method in swardman object inheritted from parent object
swardsman1.sign_in()

# using method of wizard object
wizard1.attack()

# using method of archer object
archer1.attack()

# using method of swardman object
swardsman1.attack()

# check if an object is an instance of a class or of a sub-class
print(f'is wizard1 is an instance of Wizard? : {isinstance(wizard1, Wizard)}')
print(f'is archer1 is an instance of Archer? : {isinstance(archer1, Archer)}')
print(f'is swardsman1 is an instance of Swardsman? : {isinstance(swardsman1, Swardsman)}')
print(f'is archer1 is an instance of Wizard? : {isinstance(archer1, Wizard)}')
print(f'is wizard1 is an instance of User? : {isinstance(wizard1, User)}')
print(f'is archer1 is an instance of User? : {isinstance(archer1, User)}')
print(f'is swardsman1 is an instance of User? : {isinstance(swardsman1, User)}')

# check if an object is an instance of a base class
print(f'is wizard1 is an instance of base class? : {isinstance(wizard1, object)}')
print(f'is archer1 is an instance of base class? : {isinstance(archer1, object)}')
print(f'is swardsman1 is an instance of base class? : {isinstance(swardsman1, object)}')