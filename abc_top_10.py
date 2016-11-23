# Write a simple script which collects the top 10 stories on the ABC front page
# Use requests
# Print today's date, title of article and link.

import requests
import time

# define function to return text between patterns
# s1 is an index defining where to commence search

def find_between(STRING, indStr, indEnd, return_index = False, s1=0):
	try:
		start = STRING.index(indStr, s1) + len(indStr) 			# don't include indStr
		end = STRING.index(indEnd, s1)
		if return_index:
			return(STRING[start:end], start, end)
		else:
			return(STRING[start:end])

	except ValueError:
		print(indStr, 'or', indEnd, 'not in string.')
		print('Returning empty string.')
		return('')


# ------ create requests object for abc -------- #


abc = requests.get("http://www.abc.net.au/news/")
abc_text = abc.text

top_stories = 10 				# Number of top stories

heading_start = '<h3>'			# Top stories located in 3rd heading of HTML of abc
heading_end = '</h3>'
link_start = 'href=\"/news/'	# Beginning of hyperlink
link_end = '\">'
title_end = '</a>'			
s1 = 0							# initially begin search at s1 = 0
story_list = []					# Define empty lists for details, hyperlinks, headings
link_list = []
heading_list =[]


# ----  Find tops stories, get hyperlink and title ----- #

print('ABC top',top_stories, 'for', time.strftime("%c"), 'are:')
print('')

for i in range(top_stories):

	story_details, start, end = find_between(abc_text, heading_start, heading_end,True,s1)
	story_list.append(story_details)

	# Get hyperlinks to stories
	link = abc.url + find_between(story_details, link_start, link_end)
	link_list.append(link)

	# Get title of stories
	story_details = story_details.replace('&#039;', "'")			# insert hyphens
	headings = find_between(story_details, link_end, title_end)
	heading_list.append(headings)

	# print stories with links
	print(headings)
	print(link)
	print("")

	s1 = end + 1





