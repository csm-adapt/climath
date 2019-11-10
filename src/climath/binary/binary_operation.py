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
import functools


__author__ = "Branden Kappes"
__copyright__ = "Branden Kappes"
__license__ = "mit"

_logger = logging.getLogger(__name__)


def _generate_parse_args(description):
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
        # If called as a main function, this processes command line arguments
        # as main. If this is called as part of an action
        if isinstance(args, list):
            parser = argparse.ArgumentParser(description=description)
        else:
            parser = args
        # add required parameters for this application
        parser.add_argument("operands",
            nargs='+',
            type=float,
            help="List of operands.")
        # add options for this application
        parser.add_argument('--format',
            choices=["answer", "expression"],
            default="answer",
            help="Express the result as a full expression or only the answer; "
                 "e.g., lhs (op) rhs = ans (expression) or ans (answer).")
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
        if isinstance(args, list):
            return parser.parse_args(args)
    return parse_args


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(level=loglevel, stream=sys.stdout,
                        format=logformat, datefmt="%Y-%m-%d %H:%M:%S")

def _generate_main(binary_func, opstr=None):
    if opstr is None:
        opstr = binary_func.__name__
    def main(args):
        """Main entry point allowing external calls

        Args:
          args ([str]): command line parameter list
        """
        if isinstance(args, list):
            args = parse_args(args)
        setup_logging(args.loglevel)
        _logger.debug(f"Starting ({opstr}) operation...")
        answer = functools.reduce(binary_func, args.operands)
        if args.format == "expression":
            sep = f" {opstr} "
            prefix = sep.join([str(x) for x in args.operands]) + " = "
        else:
            prefix = ""
        print(f"{prefix}{answer}")
        _logger.info(f"End climath ({opstr}).")

    opstr = opstr.strip()
    return main
