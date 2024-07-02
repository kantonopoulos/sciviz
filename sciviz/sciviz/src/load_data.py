import pkg_resources
import pandas as pd


def load_data(file_name):
    """
    Loads data from a CSV file.

    Args:
        file_name (str): The name of the CSV file (without the extension).

    Returns:
        pandas.DataFrame: The loaded data as a pandas DataFrame.
    """
    stream = pkg_resources.resource_stream(__name__, f'data/{file_name}.csv')
    return pd.read_csv(stream, index_col=False)