import requests

url = "https://zenquotes.io/api/"

kinds = ['random', 'today']

def quote(kind='random'):
	if kind not in kinds:
		kind = 'random'
	r = requests.get(url + kind).json()
	return r[0]['q'] + " - " + r[0]['a']
