import class2

def main():

	name = str(input('Enter the name of the employee: '))
	number = int(input('Enter the employee number: '))
	shift_number = int(input('Day Shift = 1\nNight Shift = 2\nEnter the shift number: '))
	pay = float(input('Enter the employee hourly pay rate: '))


	worker = class2.ProductionWorker(name, number, shift_number, pay)

	i1 = worker.get_name()
	i2 = worker.get_number()
	i3 = worker.get_shift_number()
	i4 = worker.get_pay()

	print('\nName:' , i1)
	print('Employee Number:' , i2)
	print('Shift:' , i3)
	print('Hourly Pay Rate:' , i4)

main()