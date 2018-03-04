import pandas as pd
import keywords


def read_csv(path):
    df = []
    if keywords.CONST_BIKES not in path:
        df = pd.read_csv(path)
    else:
        df = pd.read_csv(path, sep=';', encoding='latin1', parse_dates=['Date'], dayfirst=True,
                    index_col='Date')

    return df

