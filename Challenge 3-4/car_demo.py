import vehicles

def main():
	used_car = vehicles.Automobiles('Audi', 2022, 45000, 80000.0, 4)

	print('Make: ' , used_car.get_make())
	print('Model: ' , used_car.get_model())
	print('Mileage: ' , used_car.get_mileage())
	print('Price: ' , used_car.get_price())
	print('Doors: ' , used_car.get_doors())

	print('\n')


	used_car1 = vehicles.Automobiles('Honda', 2022, 45000, 80000.0, 4)

	print('Make: ' , used_car1.get_make())
	print('Model: ' , used_car1.get_model())
	print('Mileage: ' , used_car1.get_mileage())
	print('Price: ' , used_car1.get_price())
	print('Doors: ' , used_car1.get_doors())

main()