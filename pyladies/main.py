from __future__ import print_function

import argparse
import sys
import webbrowser

import pkg_resources


#_old_hook = None
_exit_code = 0


def _handbook():
    global _exit_code

    webbrowser.open("http://kit.pyladies.com")

    _exit_code = 1


def main(argv=sys.argv[1:]):
    global _old_hook

    dist = pkg_resources.get_distribution('pyladies')

    parser = argparse.ArgumentParser(
        description="Everything you need to start your own PyLadies location"
    )
    parser.add_argument(
        'handbook',
        help='read the handbook',
    )
    parser.add_argument('--version',
        action='version', default=argparse.SUPPRESS,
        version=dist.version,
        help="show program's version number and exit"
    )

    parsed_args = parser.parse_args(argv)

    if parsed_args.handbook:
        _handbook()
        return _exit_code


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
