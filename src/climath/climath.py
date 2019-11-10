#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following line in the
entry_points section in setup.py:

    [console_scripts]
    fibonacci = climath.skeleton:run

Then run `python setup.py install` which will install the command `fibonacci`
inside your current environment.
Besides console scripts, the header (i.e. until _logger...) of this file can
also be used as template for Python modules.

Note: This skeleton file can be safely removed if not needed!
"""

import argparse
import sys
import logging

from .binary.add import parse_args as add_parse_args
from .binary.add import main as add_main
from .binary.subtract import parse_args as subtract_parse_args
from .binary.subtract import main as subtract_main
from .binary.multiply import parse_args as multiply_parse_args
from .binary.multiply import main as multiply_main
from .binary.divide import parse_args as divide_parse_args
from .binary.divide import main as divide_main
from .reduce.mean import parse_args as mean_parse_args
from .reduce.mean import main as mean_main
from .reduce.median import parse_args as median_parse_args
from .reduce.median import main as median_main
from .reduce.std import parse_args as std_parse_args
from .reduce.std import main as std_main

from climath import __version__

__author__ = "Branden Kappes"
__copyright__ = "Branden Kappes"
__license__ = "mit"

_logger = logging.getLogger(__name__)


def parse_args(args):
    """Parse command line parameters

    Args:
    :param args: Argument(s) to process. If args is a list of strings, then
        this is the command line parser for the main function. Otherwise--
        that is, args is a subparser instance--this adds subcommand
        arguments to this function call.
    :type args: list of str or subparser object (see above).

    Returns:
    :return: `argparse.Namespace` if `args` is a list of strings, otherwise
        the subparser object passed as `args` is modified/augmented in place
    :rtype: argparse.Namespace or None (see above).
    """
    # This is the key. If args is an list (ostensibly of strings), then
    # this is a "top level" argument parser. If, instead, args is not
    # and is ostensibly a ArgumentParser instance, then we are adding
    # subcommand options to an existing parser.
    if isinstance(args, list):
        parser = argparse.ArgumentParser(
            description="Just a command line calculator.")
    else:
        parser = args
    # add required parameters for this application
    subparsers = parser.add_subparsers(
        title='Operations',
        required=True,
        help="Mathematical operations available from the CLI.")
    # add
    add_parser = subparsers.add_parser('add',
                                       help='Adds numbers.')
    add_parser.set_defaults(func=add_main)
    add_parse_args(add_parser)
    # subtract
    subtract_parser = subparsers.add_parser('subtract',
                                            help='Subtracts numbers.')
    subtract_parser.set_defaults(func=subtract_main)
    subtract_parse_args(subtract_parser)
    # multiply
    multiply_parser = subparsers.add_parser('multiply',
                                            help='Multiplies numbers.')
    multiply_parser.set_defaults(func=multiply_main)
    multiply_parse_args(multiply_parser)
    # divide
    divide_parser = subparsers.add_parser('divide',
                                          help='Divides numbers.')
    divide_parser.set_defaults(func=divide_main)
    divide_parse_args(divide_parser)
    # mean
    mean_parser = subparsers.add_parser('mean',
                                        help='Calculates the mean of some '
                                             'numbers.')
    mean_parser.set_defaults(func=mean_main)
    mean_parse_args(mean_parser)
    # median
    median_parser = subparsers.add_parser('median',
                                          help='Returns the median of some '
                                               'numbers.')
    median_parser.set_defaults(func=median_main)
    median_parse_args(median_parser)
    # std
    std_parser = subparsers.add_parser('std',
                                       help='Calculates the standard '
                                            'deviation of some numbers.')
    std_parser.set_defaults(func=std_main)
    std_parse_args(std_parser)
    # add options for this application
    parser.add_argument(
        '--version',
        action='version',
        version='climath {ver}'.format(ver=__version__))
    parser.add_argument(
        '-v',
        '--verbose',
        dest="loglevel",
        help="set loglevel to INFO",
        action='store_const',
        const=logging.INFO)
    parser.add_argument(
        '-vv',
        '--very-verbose',
        dest="loglevel",
        help="set loglevel to DEBUG",
        action='store_const',
        const=logging.DEBUG)
    # Only return the parsed args (argparse.Namespace) if this is a top-level
    # argument parser. (See comment above.)
    if isinstance(args, list):
        return parser.parse_args(args)


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(level=loglevel, stream=sys.stdout,
                        format=logformat, datefmt="%Y-%m-%d %H:%M:%S")


def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    if isinstance(args, list):
        args = parse_args(args)
    setup_logging(args.loglevel)
    _logger.debug("Starting calculation from climath...")
    args.func(args)
    _logger.info("End climath")


def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
