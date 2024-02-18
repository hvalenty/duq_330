import pandas as pd


def read_wine() -> pd.DataFrame:
    path = 'data/wine+quality/winequality-white.csv'
    df = pd.read_csv(path, delimiter=';')
    print(df)


if __name__ == '__main__':
    read_wine()