#!/usr/bin/env python2.7

import os
import sys
import gzip

import pandas as pd
from pylib.base.flags import Flags

def load_df(path):
    return pd.read_excel(Flags.ARGS.input_file, sheet_name='Linelist', skiprows=5)

def process_row(row):
    return ''

def main():
    Flags.PARSER.add_argument('--input_file', type=str, required=True,
                              help='input file')
    Flags.PARSER.add_argument('--output_file', type=str, required=True,
                              help='output file')

    Flags.InitArgs()

    filename = os.path.splitext(os.path.basename(Flags.ARGS.input_file))[0]
    print 'Processing %s' % filename


    df = load_df(Flags.ARGS.input_file)

    rows_written = 0
    with gzip.open(Flags.ARGS.output_file, 'wb') as f_out:
        for _, row in df.iterrows():
            res = process_row(row)
            f_out.write(res)
            rows_written += 1

    print 'Finished processing!'
    print 'Rows written %d' % rows_written
    return 0

if __name__ == '__main__':
    sys.exit(main())
