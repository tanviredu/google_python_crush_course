def skip_elements(elements):
	elements1=[]
	for index,item in enumerate(elements):
	  if index%2==0:
	    elements1.append(item)
	
	return elements1

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']