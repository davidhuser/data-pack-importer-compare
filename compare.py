import json
import os
from datetime import datetime

import pandas as pd

folders = {'jason', 'david'}
country = 'swazi'


class color:
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'


def get_path(directory, level, typ):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(dir_path, 'data', directory, '{}_{}_{}.json'.format(country, level, typ))


def file_identifier(file_path):
    common = file_path
    for i in range(2):
        common = os.path.dirname(common)
    return os.path.relpath(file_path, common)


def detailed(df1, df2):
    df = df1.merge(df2, how='outer', indicator=True)
    print(df)
    now = datetime.now().strftime('%F-%H%M%S')
    filename = "{}_diff_{}.csv".format('_'.join(folders), now)
    pd.DataFrame.to_csv(df, filename)
    print("Saved to {}{}{}".format(color.BOLD, filename, color.END))


def compare(levels, types):
    for level in levels:
        for typ in types:
            comparable_files = [get_path(f, level, typ) for f in folders]
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
            print("Comparing {2}{0}{4} with {2}{1}{4} - equal: {2}{3}{4}".format(filename1, filename2, c, equal,
                                                                                 color.END))
            if not equal:
                print("LEFT/DF1:{} - RIGHT/DF2:{}".format(filename1, filename2))
                detailed(df1, df2)


if __name__ == '__main__':
    compare(
        levels=['psnu', 'site'],
        types=['normal', 'hts']
    )
