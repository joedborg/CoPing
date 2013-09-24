import argparse
from ping import Ping

class PyPing(object)
	"""
	Send pings and write the results like
	a Cisco router.
    """
	def __init__(self, args):
		"""

        """
		pass

    def __call__(self):
		"""

        """
		pass

def main():
	"""
	Parse the arguments.
    """
	parser = argparse.ArgumentParser()
	parser.add_item('destination')

    args = parser.parse_args()

    do = PyPing(args)
	do()


if __name__ == "__main__":
	main()
