def combine_guests(guests1, guests2):
  # Combine both dictionaries into one, with each key listed 
  # only once, and the value from guests1 taking precedence
  ## first merge it with out anu comparison
  final = {**guests1,**guests2}

  ## REMEMBER IT WILL MERGE THE DICT BUT FOR COMMON ITEMS IT WILL NOT ADD 
  ## INSTED IT WILL SELECT THE COMMON ONES
  ## SO WE NEED TO LOOP THROUGH AND ADD THE DICT 1

  for key,value in final.items():
  	if key in guests1 and key in guests2:
  		final[key] = sum([value,guests1[key]])
  		## WE ARE ADDING THE GUEST1 BECAUSE WE DID NOT ADD THIS
  return final

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))