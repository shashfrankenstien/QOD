import requests
import random
import argparse

headers = {
	'Host': 'api.quotery.com',
	'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
	'Accept': 'application/json',
	'Accept-Language': 'en-US,en;q=0.5',
	'Referer': 'https://www.quotery.com/quotes',
	'Origin': 'https://www.quotery.com',
}
url = 'https://api.quotery.com/wp-json/quotery/v1/quotes?orderby={sort}&page=1&per_page=20'

sorts = dict(
	random = 'random',
	latest = 'latest',
	popular = 'poplar',
)

def quote(sort):
	r = requests.get(url.format(sort=sort), headers=headers)
	j = random.choice(r.json())
	return ' '.join([j['body'], "-", j['author']['name']])


def _cli():
	parser = argparse.ArgumentParser()
	parser.add_argument("type", nargs='?', help="Type of quote (optional)", choices=sorts.keys(), default='random')
	parser.add_argument("-s", "--silent", help="Don't print errors", action="store_true")
	args = parser.parse_args()

	try:
		print(quote(sort=sorts.get(args.type, 'random')))
	except Exception as e:
		if not args.silent:
			print(e)


if __name__ == "__main__":
	_cli()