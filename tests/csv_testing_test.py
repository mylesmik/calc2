"""Testing pandas class"""
from calc.file_handling.read_file import PandasParseData
import pytest

def test_pandas_file_type_csv_check():
    """Testing the file type"""
    #Arrange
    file_name = "add1000.csv"
    #Act
    df_test_csv_data = PandasParseData.read_file(file_name)
    #Assert
    assert df_test_csv_data is not None

def test_pandas_file_type_xlsx_check():
    """Testing df creation after extracting data from excel file"""
    #Arrange
    file_name = "addition_15values.xlsx"
    #Act
    df_test_xlsx_data = PandasParseData(file_name).read_file()
    #Assert
    assert df_test_xlsx_data is not None

def test_pandas_file_type_txt_check():
    """Testing the other file type check"""
    #Arrange
    file_name = "sample_test_data.txt"
    #Act
    with pytest.raises(ValueError):
        #Assert
        assert PandasParseData(file_name).read_file() is True

