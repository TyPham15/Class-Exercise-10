class Automobiles:
	def __init__(self, make, model, mileage, price):
		self.set_make(make)
		self.set_model(model)
		self.set_mileage(mileage)
		self.set_price(price)

	
	def set_make(self, make):
		self.make = make
	def set_model(self, model):
		self.model = model
	def set_mileage(self, mileage):
		self.mileage = mileage
	def set_price(self, price):
		self.price = price


	def get_make(self):
		return self.make
	def get_model(self):
		return self.model
	def get_mileage(self):
		return self.mileage
	def get_price(self):
		return self.price



class Truck(Automobiles):
	def __init__(self, make, model, mileage, price):
		Automobiles.__init__(self, make, model, mileage, price)

class SUV(Automobiles):
	def __init__(self, make, model, mileage, price):
		Automobiles.__init__(self, make, model, mileage, price)

class Electric(Automobiles):
	def __init__(self, make, model, mileage, price):
		Automobiles.__init__(self, make, model, mileage, price)