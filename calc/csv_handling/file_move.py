"""This holds the class that is responsible for moving the csv files to new directories"""
import shutil


class FileOperator:
    """Contains methods to move files around"""
    # pylint: disable='too-few-public-methods
    @staticmethod
    def move_to_destination(current_csv_file,
                            destination='tests/csvs/output_csv'):
        """Moves csv files from one folder to another"""
        shutil.move(current_csv_file, destination)
