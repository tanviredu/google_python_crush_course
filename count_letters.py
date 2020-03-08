def count_letters(text):
	result = {}
	for letter in text:
		if letter not in result:
			## create the placeholder for this letter
			## this is just initialize it
			result[letter] = 0


		## now increment it 1
		result[letter]+=1
	return result

print(count_letters("Tanivr Rahman ornob"))