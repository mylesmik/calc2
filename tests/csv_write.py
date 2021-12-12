# pylint: disable-all
def csvwriter(input_df):
    """takes in a df from history and output to a csv file"""
    input_df.to_csv('tests/csvs/output_csv/output2.csv', mode='a', index=False, header=False)
