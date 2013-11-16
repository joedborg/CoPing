import sys
import argparse
from ping import Ping
from ping import PingSuccess
from ping import PingTimeout


class CoPing(object):
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
        self.ping = Ping(self.destination)
        self.ping.print_header()
        while True:
            attempt = self.ping.do()
            if isinstance(attempt, PingSuccess):
                sys.stdout.write('!')
                sys.stdout.flush()
            elif isinstance(attempt, PingTimeout):
                sys.stdout.write('.')
                sys.stdout.flush()


def main():
    """
    Parse the arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('destination')

    args = parser.parse_args()

    run = CoPing(args)
    try:
        run()
    except KeyboardInterrupt:
        sys.stdout.write('\n')
        run.ping.print_statistics(interrupted=True)
        sys.exit(0)


if __name__ == "__main__":
    main()