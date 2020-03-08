def pig_latin(text):
	tmp=[]
	words = text.split()
	for word in words:
		ans=word[1:]+word[0]+"ay"
		tmp.append(ans)
	return " ".join(tmp)
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"