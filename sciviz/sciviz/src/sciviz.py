import matplotlib.pyplot as plt
import seaborn as sns


def sciviz(height=5, aspect=1):
    """Create a figure.

    Args:
        height (float): The height of the figure or FacetGrid. Default is 5.
        aspect (float): The aspect ratio of the figure or FacetGrid. Default is 1.

    Returns:
        matplotlib.axes._subplots.AxesSubplot: The axis or FacetGrid.
    """
    
    # Create a single figure and axis
    fig, ax = plt.subplots(figsize=(height * aspect, height))
    return ax