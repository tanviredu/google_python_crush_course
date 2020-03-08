def guest_list(guests):
	for item in guests:
		x,y,z = item
		print("{} is {} years old and works as {}.".format(x,y,z))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])