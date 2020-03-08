def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = input_string.lower()
	new_string = "".join(new_string.split())
	#print (new_string)
	
	reverse_string = ""
	# Traverse through each letter of the input string
	for i in range(len(new_string)):
		# Add any non-blank letters to the 
		# end of one string, and to the front
		# of the other string. 
			
			reverse_string += new_string[len(new_string)-i-1]
	reverse_string = reverse_string.lower()
	#print (reverse_string)
	# Compare the strings
	if new_string==reverse_string:
		return True
	return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True