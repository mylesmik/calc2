"""Class for exporting data to external file"""

import pandas as pd
#from calc.file_handling.read_file import PandasParseData
from calc.history.calculations import Calculations

class Export:
    """Exporting data class"""
    @staticmethod
    def export_result_excel_file():
        """Exporting the calculated result to excel file using pandas"""
        result = Calculations.history
        df_result = pd.DataFrame(result, columns=['result'])
        with pd.ExcelWriter('../../../../Downloads/calc2-refactor_part7_pandas/tests/input_excel_files/addition_15values.xlsx', mode='a', if_sheet_exists='replace') as writer:
            df_result.to_excel(writer, sheet_name='Test_output', index=False)
            writer.save()
