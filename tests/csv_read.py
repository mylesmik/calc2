"""Function to read CSV"""
import pandas as pd
from tests.abspath import absolutepath

out_file = "tests/csvs/output_csv/output2.csv"


class Read:
    # pylint: disable-all
    @staticmethod
    def csvreader():
        file = pd.read_csv(absolutepath(out_file))
        return file
