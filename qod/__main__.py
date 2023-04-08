import requests
from .quotes import quote, kinds

class _cli_proc():
	@staticmethod
	def run(channel, kind):
		try:
			q = {'success': quote(kind=kind)}
		except requests.ConnectionError:
			q = {'error':"Network connection not available"}
		except Exception as e:
			q = {'error': str(e)}
		channel.put(q)



def _cli():
	import argparse, textwrap
	from multiprocessing import Process, Queue
	from queue import Empty
	import shutil
	terminal_size = shutil.get_terminal_size(fallback=(80, 25))

	parser = argparse.ArgumentParser()
	parser.add_argument("type", nargs='?', help="Type of quote (optional)", choices=kinds, default='today')
	parser.add_argument("-w", "--width", help="Output print width", type=int, default=terminal_size.columns)
	parser.add_argument("-t", "--timeout", help="Request timeout", type=float, default=1.2)
	parser.add_argument("-s", "--silent", help="Silently fail on error", action="store_true")
	parser.add_argument("-p", "--plain", help="Exclude leading and lagging decorations", action="store_true")
	args = parser.parse_args()

	width = min(terminal_size.columns, max(20, args.width))



	chan = Queue()
	p = Process(target=_cli_proc.run, args=(chan, args.type))
	# p.daemon = True
	try:
		p.start()
		q = chan.get(timeout=args.timeout)
		p.join()
		if 'error' in q:
			raise Exception(q['error'])
		else:
			q = q['success']
	except Empty:
		if args.silent:
			return 0
		else:
			q = "qod error: " + "Network timeout"
	except Exception as e:
		if args.silent:
			return 0
		else:
			q = "qod error: " + str(e)
	finally:
		if p.is_alive():
			p.terminate()
		else:
			p.join()


	if args.plain:
		print(q)
	else:
		print(''.join(["="]*width))
		print("\n".join([l.center(width) for l in  textwrap.wrap(q, width)]))
		print(''.join(["="]*width))




if __name__ == "__main__":
	_cli()
