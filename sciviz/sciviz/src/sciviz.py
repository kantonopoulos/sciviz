import matplotlib.pyplot as plt
import seaborn as sns

def axis_scales(scales):
    """Set the scales of the axes based on the input string.

    Args:
        scales (string): The scale type. One of 'fixed', 'free', 'free_x', or 'free_y'.

    Returns:
        bool: Whether the x-axis should be shared.
        bool: Whether the y-axis should be shared.
    """
    if scales == 'fixed':
        sharex = True
        sharey = True
    elif scales == 'free':
        sharex = False
        sharey = False
    elif scales == 'free_x':
        sharex = False
        sharey = True
    elif scales == 'free_y':
        sharex = True
        sharey = False
    return sharex, sharey

def sciviz(data, height=4, aspect=1, cols=None, rows=None, col_wrap=None, scales='fixed'):
    # Set the scales of the axes
    sharex, sharey = axis_scales(scales)
    
    if rows and cols:
        # Create a grid of subplots
        g = sns.FacetGrid(data, row=rows, col=cols, height=height, aspect=aspect, sharex=sharex, sharey=sharey)
        return g
    elif cols or rows:
        # Create a grid of subplots with only one faceting variable
        g = sns.FacetGrid(data, row=rows, col=cols, col_wrap=col_wrap, height=height, aspect=aspect, sharex=sharex, sharey=sharey)
        return g
    else:
        # Create a single figure and axis
        fig, ax = plt.subplots(figsize=(height * aspect, height))
        return ax