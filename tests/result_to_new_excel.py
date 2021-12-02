"""Class for exporting data to external file"""

import pandas as pd
from tests.csv_testing import PandasParseData
from calc.history.calculations import Calculations

class Export(PandasParseData):
    # pylint: disable=abstract-class-instantiated
    """Exporting data class"""
    @staticmethod
    def result_to_new_excel():
        """Exporting the calculated result to excel file using pandas"""
        result = Calculations.history
        df_result = pd.DataFrame(result, columns=['result'])
        with pd.ExcelWriter('test_data/add1000.csv',
                            mode='a', if_sheet_exists='replace') as writer:
            df_result.to_excel(writer, sheet_name='output_sheet', index=False)
            writer.save()