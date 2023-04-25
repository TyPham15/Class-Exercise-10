class Employee:
	def __init__(self, name, number):
		self.set_name(name)
		self.set_number(number)


	def set_name(self, name):
		self.name = name
	def set_number(self, number):
		self.number = number


	def get_name(self):
		return self.name
	def get_number(self):
		return self.number


class ProductionWorker(Employee):
	def __init__(self, name, number, shift_number, pay):
		super().__init__(name, number)

		if shift_number < 1 or shift_number > 2:
			print("Enter in either 1 or 2 for day and night shift.")
			print(type(shift_number))
			print(shift_number)
			quit()
		if shift_number == 2:
			self.set_shift_number_night()
		else:
			self.set_shift_number_day()
			
		self.set_pay(pay)


	def set_shift_number_day(self):
		self.shift_number = "day shift"

	def set_shift_number_night(self):
		self.shift_number = "night shift"

	def set_pay(self, pay):
		self.pay = pay


	def get_shift_number(self):
		return self.shift_number
	def get_pay(self):
		return self.pay
	
