import matplotlib.pyplot as plt
import seaborn as sns


def sciviz(data, height=4, aspect=1):
    """Create a figure.

    Args:
        data (pandas.DataFrame): The data to plot.
        height (float): The height of the figure or FacetGrid. Default is 4.
        aspect (float): The aspect ratio of the figure or FacetGrid. Default is 1.

    Returns:
        matplotlib.axes._subplots.AxesSubplot: The axis or FacetGrid.
    """
    
    # Create a single figure and axis
    fig, ax = plt.subplots(figsize=(height * aspect, height))
    return ax