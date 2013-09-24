import argparse
from ping import Ping

class PyPing(object):
	"""
	Send pings and write the results like
	a Cisco router.
	"""
	def __init__(self, args):
		"""
		Move the arguments into the instance's
		namespace.
		"""
		self.destination = args.destination

	def __call__(self):
		"""
		Run the ping, print '!' for success
		and '.' for failure.
		"""
		p = Ping(self.destination)
		if p.do():
			print "!"
		else:
			print "."

def main():
	"""
	Parse the arguments.
	"""
	parser = argparse.ArgumentParser()
	parser.add_argument('destination')

	args = parser.parse_args()

	do = PyPing(args)
	do()


if __name__ == "__main__":
	main()
