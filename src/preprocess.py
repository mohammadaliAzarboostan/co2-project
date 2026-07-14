import pandas as pd


class DataLoader:

    def __init__(self, path):

        self.path = path

    def load(self):

        df = pd.read_csv(self.path)

        return df

    def split(self):

        df = self.load()

        X = df.drop("out1", axis=1)

        y = df["out1"]

        return X, y