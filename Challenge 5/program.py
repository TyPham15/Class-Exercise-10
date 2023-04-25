import class1

def main():
	bumblebee = class1.bee(6, 4)

	print('Bumblebee legs:', bumblebee.get_legs())
	print('Bumblebee wings:', bumblebee.get_wings())

	print('\n')


	grasshopper = class1.grasshopper(6, 2)

	print('Grasshopper legs:', grasshopper.get_legs())
	print('Grasshopper wings:', grasshopper.get_wings())

main()