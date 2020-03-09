def get_event_date(event):
	### this will take the 
	### even object and extract the 
	### event date from the object
	return event.date 


def current_users(events):
	## we get a number of events and first we have to
	## sort based on the date
	events.sort(key = get_event_date)
	## and we make a empty dict
	## and we update it 
	## or create a new entry based on the need
	machines = {}
	for event in events:
		if event.machine not in machines:
			## we check if the machine 
			## is already on the list
			## if it is then we update it
			# otherwise we will init it with a set
			# why set?? because for login and logout we dont need 
			## any duplicate value
			machines[event.machine] = set()
		if event.type = "login":
			# if the user now in the machine
			# we add the user in the corresponding set
			machines[event.machine].add(event.user)

		elif event.type = "logout":
			machines[event.machine].remove(event.user)
	return machines


## we take the dict of set containing information
## and generate the report
## remember one machine can have multiple users
def generate_report(machines):
	for machine,users in machines.items():
		if len(users) >0:
			user_list = ", ".join(users)
			print("{}: {}".format(machine,user_list))


## create the event class

class Event:
	def __init__(self,event_date,event_type,machine_name,user):
		self.date = event_date
		self.type = event_type
		self.machine - machine_name
		self.user = user




events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'login', 'mailserver.local', 'chris'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),

]