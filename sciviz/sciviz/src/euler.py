from matplotlib_set_diagrams import EulerDiagram
from palettes import get_palette
from utils import format_string, prepare_sets, calculate_colors


def euler(ax, data, group, var, palette='jama', alpha=0.7, label_color='black', label_size=11, label_weight='bold', innertext=None, innertext_color='black', innertext_size=10, format_labels=True):
    """Create a Euler diagram.

    Args:
        ax (matplotlib.axes.Axes): The axes object to draw the plot on.
        data (pandas.DataFrame): The data to plot.
        group (str): The column name of the data to plot.
        var (str): The column name of the data to plot.
        palette (str): The color palette to use. Defaults to 'jama'.
        alpha (float): The transparency of the pie chart. Defaults to 0.7.
        label_color (str): The color of the labels. Defaults to 'black'.
        label_size (int): The size of the labels. Defaults to 11.
        label_weight (str): The weight of the labels. Defaults to 'bold'.
        innertext (bool): Whether to show the percentage inside the pie chart. Defaults to None.
        innertext_color (str): The color of the percentage inside the pie chart. Defaults to 'black'.
        innertext_size (int): The size of the percentage inside the pie chart. Defaults to 10.
        format_labels (bool): Whether to format the labels. Defaults to True.

    Returns:
        matplotlib.axes.Axes: The axes object with the plot
    """
    set_labels, subset_labels = prepare_sets(data, group, var)
    
    palette = get_palette(palette=palette, data=data, color=group)    
    color_map = calculate_colors(subset_labels, palette)
    ax = EulerDiagram(subset_labels, set_labels=set_labels, ax=ax)

    # Set colors
    for subset, color in color_map.items():
        artist = ax.subset_artists[subset]
        artist.set_facecolor(color)
        artist.set_edgecolor(None)
        artist.set_alpha(alpha)

    # Set labels
    for ii, text in enumerate(ax.set_label_artists):
        if format_labels:
            text.set_text(format_string(text.get_text()))
        text.set_color(label_color)
        text.set_fontsize(label_size)
        text.set_weight(label_weight)

    for subset in subset_labels.keys():
        text = ax.subset_label_artists[subset]
        text.set_color(innertext_color)
        text.set_fontsize(innertext_size)

    return ax

    