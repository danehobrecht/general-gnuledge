# https://www.youtube.com/watch?v=6c6NYPjO_rI&t=0s

# Used to create an object
class Guitar:
	# Constructor (method). Automatically called each time we create a new object.
	def __init__(self):
		self.n_strings = 6
		self.play()
		self.__cost = 50

	def play(self):
		print("pam pam pam pam pam pam pam")

# Inheritance. Akin to a child taking DNA from a parent. All attributes and methods are copied over.
class ElectricGuitar(Guitar):
	def __init__(self):
		# Accesses parent __init__!
		super().__init__()
		self.n_strings = 8
		self.color = ("#000000", "#FFFFFF")
		# Private attribute
		self.__cost = 50

	def playLouder(self):
		print("pam pam pam pam pam pam pam".upper())

	# Private method
	def __secret(self):
		print()

my_guitar = ElectricGuitar()
print("child class: ", my_guitar.n_strings)
print("parent class: ", Guitar().n_strings)