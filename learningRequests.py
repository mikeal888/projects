import requests

# define url string
URL = 'https://en.wikipedia.org/wiki/Uniform_Resource_Locator'

# define additional key parameters
payload = {'key1': 'value1', 'key2': 'value2'}

# assign request object to test. 
# params encodes url with above parameters
# test = requests.get(URL, params = payload)
test = requests.get(URL)

