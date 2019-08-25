import requests
import random
import re

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


def cleanhtml(raw_html):
	cleanr = re.compile('<.*?>')
	cleantext = re.sub(cleanr, '', raw_html)
	cleantext = cleantext.replace("&nbsp;", " ")
	cleantext = cleantext.replace("&amp;", "&")
	return cleantext


def quote(sort='random'):
	r = requests.get(url.format(sort=sort), headers=headers)
	j = random.choice(r.json())
	return cleanhtml(' '.join([j['body'], "-", j['author']['name']]))


def _cli():
	import argparse, textwrap
	parser = argparse.ArgumentParser()
	parser.add_argument("type", nargs='?', help="Type of quote (optional)", choices=sorts.keys(), default='random')
	parser.add_argument("-w", "--width", nargs='?', help="Width to print", type=int, default=80)
	parser.add_argument("-s", "--silent", help="Silently fail on error", action="store_true")
	parser.add_argument("-p", "--plain", help="Exclude leading and lagging decorations", action="store_true")
	args = parser.parse_args()

	width = min(150, max(40, args.width))
	try:
		q = quote(sort=sorts.get(args.type, 'random'))
		q = textwrap.fill(q, width)
	except Exception as e:
		if args.silent:
			return 0
		else:
			q = "qod error: " + str(e)
	if not args.plain: print(''.join(["="]*width))
	print(q)
	if not args.plain: print(''.join(["="]*width))


if __name__ == "__main__":
	_cli()