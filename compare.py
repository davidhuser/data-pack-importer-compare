import argparse
import json
import os
from datetime import datetime

import pandas as pd


class color:
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'


def parse_args():
    parser = argparse.ArgumentParser(usage='%(prog)s',
                                     description="Compare data JSONs in folders")
    parser.add_argument('--folder1',
                        dest='folder1',
                        action='store',
                        required=True,
                        help="File path of first folder"
                        )

    parser.add_argument('--folder2',
                        dest='folder2',
                        action='store',
                        required=True,
                        help="File path of second folder"
                        )

    parser.add_argument('--country',
                        dest='country',
                        action='store',
                        required=True,
                        help="Country string"
                        )

    parser.add_argument('--level',
                        dest='level',
                        action='store',
                        required=True,
                        choices={'psnu', 'site'},
                        help="Level"
                        )

    parser.add_argument('--type',
                        dest='type',
                        action='store',
                        required=True,
                        choices={'normal', 'hts'},
                        help="Type"
                        )

    return parser.parse_args()


def get_path(directory, country, level, typ):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(dir_path, directory, '{}_{}_{}.json'.format(country, level, typ))


def file_identifier(file_path):
    common = file_path
    for i in range(2):
        common = os.path.dirname(common)
    return os.path.relpath(file_path, common)


def detailed(df1, df2, paths):
    df = df1.merge(df2, how='outer', indicator=True)
    with pd.option_context('display.max_rows', 30, 'display.max_columns', 8):
        print(df.copy().rename(columns={
            'attributeoptioncombo': 'aoc',
            'categoryoptioncombo': 'coc',
            'supportType': 'st'
        })[df['_merge'] != 'both'])
    now = datetime.now().strftime('%F-%H%M%S')
    filename = "{}_diff_{}.csv".format('_'.join(paths).replace('/', '_'), now)
    pd.DataFrame.to_csv(df, filename)
    print("Saved to {}{}{}".format(color.BOLD, filename, color.END))


def compare(dir_paths, country, level, typ):
        comparable_files = [get_path(f, country, level, typ) for f in dir_paths]
        path1 = comparable_files[0]
        filename1 = file_identifier(path1)
        path2 = comparable_files[1]
        filename2 = file_identifier(path2)

        with open(path1, 'r') as jf:
            data = json.dumps(json.load(jf).get('data'))
            df1 = pd.read_json(data)

        with open(path2, 'r') as jf:
            data = json.dumps(json.load(jf).get('data'))
            df2 = pd.read_json(data)

        equal = pd.DataFrame.equals(df1, df2)
        c = color.RED if not equal else color.BOLD
        print("Comparing {0}{2}{1} with {0}{3}{1} - equal: {0}{4}{1}".format(c,
                                                                             color.END,
                                                                             filename1,
                                                                             filename2,
                                                                             equal))
        if not equal:
            print("{0}LEFT/DF1:{2}{1} - {0}RIGHT/DF2:{3}{1}".format(color.BOLD, color.END, filename1, filename2))
            detailed(df1, df2, dir_paths)


if __name__ == '__main__':
    args = parse_args()
    compare(
        dir_paths=[args.folder1, args.folder2],
        country=args.country,
        level=args.level,
        typ=args.type
    )
