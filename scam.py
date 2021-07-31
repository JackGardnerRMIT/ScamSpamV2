import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = 'https://docs.google.com/forms/u/0/d/e/1FAIpQLSfjpZ8P3uPqTc6-8HjBalPpSlIO9jWx83hQeHrp8eZwW7CswA/formResponse'
#input the request-url from the dev console in headers

names = json.loads(open('namesfull.json').read())
email_list = ["@icloud.com", "@outlook.com", "@yahoo.com", "@gmail.com", "@hotmail.com"]
name_number = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

for name in names:
	
	username = name + ''.join(random.choice(name_number) for i in range(1,3)) + ''.join(random.choice(email_list))
	password = ''.join(random.choice(chars) for i in range(1,9))

	requests.post(url, allow_redirects=False, data={
		'entry.165056968': username,
		'entry.912993514': password
        #where password and username data is stored from dev console
	})

	print('Sending Username: %s and Password: %s' % (username, password))