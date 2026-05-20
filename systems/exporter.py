import pandas as pd


class Exporter:
    def export_to_csv(self, data, path = 'exports/transactions.csv'):
        return pd.DataFrame(data).to_csv(path, index=False)