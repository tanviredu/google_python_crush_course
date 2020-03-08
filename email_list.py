def email_list(domains):
	emails = []
	for domain,users in domains.items():
	  for user in users:
	  	tmp = "{}@{}".format(user,domain)
	    emails.append(tmp)
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))





###ans:
emails = []
for domain,users in data.items():
     for user in users:
         tmp = "{}@{}".format(user,domain)
         emails.append(tmp)

