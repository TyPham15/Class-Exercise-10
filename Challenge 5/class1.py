#class only
class insect:
	def __init__(self, legs):
		self.set_legs(legs)

		#mutator
	def set_legs(self, legs):
		self.legs = legs

		#accessor
	def get_legs(self):
		return self.legs


class bee(insect):
	def __init__(self, legs, wings):
		super().__init__(legs)

		self.set_wings(wings)

		#mutator
	def set_wings(self, wings):
		self.wings = wings

		#accessor
	def get_wings(self):
		return self.wings


class grasshopper(insect):
	def __init__(self, legs, wings):
		super().__init__(legs)

		self.set_wings(wings)

		#mutator
	def set_wings(self, wings):
		self.wings = wings

		#accessor
	def get_wings(self):
		return self.wings