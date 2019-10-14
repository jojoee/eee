"""eee
Usage:
------
    $ eee 10

Available options are:
    -h, --help         Show this help

Contact:
--------
- https://github.com/jojoee/eee

Version:
--------
- eee v0.0.1
"""

import sys
from eee import e


def main():
    """eeee ee ee"""
    if len(sys.argv) > 1:
        e(sys.argv[1])

    else:
        e(10)


"""
when running a package as a script with -m as above,
Python executes the contents of the __main__.py file.

python -m eee
python -m eee 3
"""
if __name__ == "__main__":
    main()
