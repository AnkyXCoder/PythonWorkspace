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

    def run(self):
        print(f'ran really fast')

# child object Swardsman
class Swardsman(User):
    def __init__(self, name, power):
        self._name = name
        self._power = power

    def attack(self):
        print(f'attacking with sward power of {self._power}')

# child object Hybrid
class Hybrid(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, arrows)
    
    def attack(self):
        Wizard.attack(self)
        Archer.attack(self)

# Instantiating the wizard object
wizard1 = Wizard('Merlin', 50)

# Instantiating the archer object
archer1 = Archer('Robin', 100)

# Instantiating the swardsman object
swardsman1 = Swardsman('Hercules', 80)

# Instantiating the hybrid object
hybridborg = Hybrid("Hyena", 50, 50)

# using method in wizard object inheritted from parent object
wizard1.sign_in()

# using method in archer object inheritted from parent object
archer1.sign_in()

# using method in swardsman object inheritted from parent object
swardsman1.sign_in()

# using method in hycrid object inheritted from User object
hybridborg.sign_in()

# using method of wizard object
wizard1.attack()

# using method of archer object
archer1.attack()

# using method of swardsman object
swardsman1.attack()

# check if an object is an instance of a class or of a sub-class
print(f'is wizard1 is an instance of Wizard? : {isinstance(wizard1, Wizard)}')
print(f'is archer1 is an instance of Archer? : {isinstance(archer1, Archer)}')
print(f'is swardsman1 is an instance of Swardsman? : {isinstance(swardsman1, Swardsman)}')
print(f'is archer1 is an instance of Wizard? : {isinstance(archer1, Wizard)}')
print(f'is wizard1 is an instance of User? : {isinstance(wizard1, User)}')
print(f'is archer1 is an instance of User? : {isinstance(archer1, User)}')
print(f'is swardsman1 is an instance of User? : {isinstance(swardsman1, User)}')
print(f'is hybridborg is an instance of User? : {isinstance(hybridborg, User)}')
print(f'is hybridborg is an instance of Wizard? : {isinstance(hybridborg, Wizard)}')
print(f'is hybridborg is an instance of Archer? : {isinstance(hybridborg, Archer)}')
print(f'is hybridborg is an instance of Swardsman? : {isinstance(hybridborg, Swardsman)}')

# check if an object is an instance of a base class
print(f'is wizard1 is an instance of base class? : {isinstance(wizard1, object)}')
print(f'is archer1 is an instance of base class? : {isinstance(archer1, object)}')
print(f'is swardsman1 is an instance of base class? : {isinstance(swardsman1, object)}')
print(f'is hybridborg is an instance of base class? : {isinstance(hybridborg, object)}')

#  using method of archer with Hybrid object
hybridborg.run()
hybridborg.attack()