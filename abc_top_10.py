# Write a simple script which collects the top 10 stories on the ABC front page
# Use requests
# Print today's date, title of article and link.

import requests

# define function to return text between patterns

def between(STRING, indStr, indEnd):
	try:
		start = STRING.index(indStr) + len(indStr) 			# don't include indStr
		end = STRING.index(indEnd)
		return(STRING[start:end])

	except ValueError:
		print(indStr, 'or', indEnd, 'not in string.')
		print('Returning empty string.')
		return('')

# create requests object for abc

abc = requests.get("http://www.abc.net.au/news/")

top_stories = 10 			# Number of top stories




