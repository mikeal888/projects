#!/usr/bin/python3.5

# Write a script which encrypts some text and saves the encryption to a log file which 
# only the 
# user has access to. 
# Two keys are generated, one for the password, the other for the encryption. 

import string
import random 
import pickle

# All text characters
chars = string.ascii_letters + string.digits + string.punctuation + ' ' + string.whitespace

# Use random numbers for encryption
numbers = random.sample(range(0,len(chars)),len(chars))

# Randomly assign chars in dict = {"chars": "encrypt chars"}
def encrypt(TEXT):
	
	# Generate random encryption

	randchars = {}
	for i, item in enumerate(numbers):
		randchars[chars[i]] = chars[item]
	
	text_list = list(TEXT)	

	# Encrypt text

	en_text_list = [randchars[ind] for ind in text_list]
	en_text = "".join(en_text_list)

	# Return encrypted text and mapping between characters

	return(en_text, randchars)


# Import text file to encrypt
file_name = input('Enter file: ')
file_open = open(file_name)
file_text = file_open.read()

en_file_text, key = encrypt(file_text)

# Save file to encrypted_text directory
en_dir = 'encrypted_text/'
en_file_name = 'encrypted_'+file_name
en_file = open(en_dir+en_file_name,'w')
en_file.write(en_file_text)
en_file.close()

# Save encryption key as pickle file to keys/
keys_dir = 'keys/'
keys_name = 'keys_'+file_name.split('.')[0]+'.pickle'
with open(key_name, 'wb') as handle:
	pickle.dump(key, handle)