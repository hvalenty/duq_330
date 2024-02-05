import pandas as pd

class ReadData:

    def __init__(self, path: str):
        pd.read_csv(path)