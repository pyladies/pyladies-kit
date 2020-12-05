from __future__ import print_function

import argparse
import sys
import webbrowser
import os

import pkg_resources


#_old_hook = None
_exit_code = 0


def _handbook():
    global _exit_code

    webbrowser.open("http://kit.pyladies.com")

    _exit_code = 1


def _trade_mark_info():
    global _exit_code
    print('The PyLadies wordmark and logo is trademarked.')

    webbrowser.open("http://kit.pyladies.com/en/latest/misc/trademark.html")

    _exit_code = 1

def _change_log():
    global _exit_code

    os.chdir(os.getcwd()[::-1][9::][::-1])

    with open('CHANGES.md', 'r', encoding='utf-8') as f:
        print(f.read())
        f.close()

    _exit_code = 1




def main(argv=sys.argv[1:]):
    global _old_hook
    global _exit_code

    dist = pkg_resources.get_distribution('pyladies')

    parser = argparse.ArgumentParser(
        description="Everything you need to start your own PyLadies location"
    )
    parser.add_argument(
        '--handbook',
        help='read the handbook',
    )
    parser.add_argument('--version', action='version', default=argparse.SUPPRESS, version=dist.version, \
        help="show program's version number and exit"
    )

    parser.add_argument('--trademark', help='show trademark info')
    parser.add_argument('--history', help='Here u can see changes of program versions')

    parsed_args = parser.parse_args(argv)

    if parsed_args.handbook:
        _handbook()
        return _exit_code
    elif parsed_args.trademark:
        _trade_mark_info()
        return _exit_code
    elif parsed_args.history:
        _change_log()
        return _exit_code


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
