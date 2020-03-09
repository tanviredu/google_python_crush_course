def count_letters(text):
  result = {}
  # Go through each letter in the text
  for letter in text.lower().split():
  	if letter 
    # Check if the letter needs to be counted or not
    ___
    # Add or increment the value in the dictionary
    ___
  return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}




##ans

result = {}

tmp=[]
text = "".join(text.lower().split())
for letter in text:
	if letter.isdigit()==False:
		tmp.append(letter)
tmp2 = "".join(tmp)
str1 = ''.join(e for e in tmp2 if e.isalnum())

for letter in str1:
     if letter not in result:
        
       result[letter] = 0
     result[letter]+=1
return result








































# def count_letters(text):
#   result = {}
#   # Go through each letter in the text
#   reject=[0,1,2,3,4,5,6,7,8,9]
#   for letter in "".join(text.lower()):
#     if letter not in result and letter not in reject:
        
#       result[letter] = 0
#     result[letter]+=1
  
#   #for letter in ___:
#     # Check if the letter needs to be counted or not
#     ___
#     # Add or increment the value in the dictionary
#     ___
#   return result

# print(count_letters("AaBbCc"))
# # Should be {'a': 2, 'b': 2, 'c': 2}

# print(count_letters("Math is fun! 2+2=4"))
# # Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

# print(count_letters("This is a sentence."))
# # Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}