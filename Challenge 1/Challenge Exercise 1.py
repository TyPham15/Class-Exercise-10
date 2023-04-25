#Challenge Exercise 1
class AnimalType:
	def eats(self):
		print("This animal likes to eat?")

class rabbits(AnimalType):
	def munch(self):
		print(" carrots ")

class birds(rabbits):
	def munch1(self):
		print(" seeds ")

class horses(birds):
	def munch2(self):
		print(" hay ")


RabbitObject = rabbits()

RabbitObject.eats()
RabbitObject.munch()


BirdObject = birds()

BirdObject.eats()
BirdObject.munch1()
BirdObject.munch()


HorseObject = horses()

HorseObject.eats()
HorseObject.munch2()
HorseObject.munch()