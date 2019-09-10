#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
#import pkg_resources
import argparse
import bankparser.parsercsv
import bankparser.qif
import bankparser.config
#import bankparser.banks.vtb24
#from bankparser.parsercsv import ParserCSV



# def get_version():
#     dist = pkg_resources.get_distribution("bankparser")
#     return dist.version


def list_banks(args):
    """
    Выводит список доступных банков
    :param args:
    :return:
    """
    print('list available banks:')
    banks = bankparser.config.bankconfig.get_list_banks()
    for bank in banks:
        print(bank)


def convert(args):
    """
    Конвертация в QIF
    :param args:
    :return:
    """
    print('Convert {0} file {1}'.format(args.bank, args.infile))
    if args.outfile:
        newname = args.outfile
    else:
        newname = os.path.splitext(args.infile)[0] + '.qif'

    bank_parser_class = bankparser.config.bankconfig.get_parser(args.bank)
    bank_parser = bank_parser_class(args.bank)
    statement = bank_parser.parse(args.infile)
    count = len(statement.lines)
    print('Read {} lines'.format(count))
    qif = bankparser.qif.QIF(statement)
    qif.write(newname)
    print('qif saved ({})'.format(newname))


def main(args=None):
    parser = argparse.ArgumentParser(description='Tool to convert proprietary bank statement ' +
                                                 'to QIf format. Ver {}'.format(bankparser.__version__))
    # parser.add_argument("-v", "--version", action="version",
    #                     version='bankparser version %s' % get_version(),
    #                     help="show current version and exit")
    subparsers = parser.add_subparsers(help='List of commands')

    # A list command
    list_parser = subparsers.add_parser('list', help='list available banks')
    list_parser.set_defaults(func=list_banks)
    # A convert command
    convert_parser = subparsers.add_parser('convert', help='Convert to qif format')
    convert_parser.add_argument('bank', help='Bank name')
    convert_parser.add_argument('infile', help='path to bank file')
    convert_parser.add_argument('--outfile', help='path to qif file')
    convert_parser.set_defaults(func=convert)

    args = parser.parse_args()

    if not hasattr(args,"func"):
        parser.print_help()
        sys.exit(1)

    args.func(args)

if __name__ == "__main__":
    sys.exit(main())
