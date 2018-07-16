#!/usr/bin/env python2.7

import csv
import gzip
import os
import sys

from pylib.base.flags import Flags

def process_row(row, filename):
    pass

def main():
    Flags.PARSER.add_argument('--input_file', type=str, required=True,
                              help='input gho csv file')
    Flags.PARSER.add_argument('--output_file', type=str, required=True,
                              help='output file')

    Flags.InitArgs()

    rows_written = 0
    filename = os.path.splitext(os.path.basename(Flags.ARGS.input_file))[0]
    print 'Processing %s' % filename

    with gzip.open(Flags.ARGS.input_file, 'rb') as data_file, \
            gzip.open(Flags.ARGS.output_file, 'wb') as f_out:
        reader = csv.DictReader(data_file, skipinitialspace=True)
        for row in reader:
            res = process_row(row, filename)
            for data in res:
                if not data:
                    continue
                f_out.write(data)
                rows_written += 1

        print 'Finished processing!'
        print 'Rows written %d' % rows_written
        return 0

if __name__ == '__main__':
    sys.exit(main())
