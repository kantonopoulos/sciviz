from legend import customize_legend
from utils import format_string
from palettes import get_palette
import seaborn as sns


def histogram(ax, data, x, y=None, color=None, stat='count', bins='auto', binwidth=None, palette='jama', alpha=0.7, hist_color='black', edge_color='black', show_legend=True, format_labels=True):
    """Create a histogram.

    Args:
        ax (matplotlib.axes._subplots.AxesSubplot): The axis to plot on.
        data (pandas.DataFrame): The data to plot.
        x (str): The column name for the x-axis.
        y (str): The column name for the y-axis. Default is None.
        color (str): The column name for the color attribute. Default is None.
        stat (str): The type of histogram. Default is 'count'.
        bins (int): The number of bins. Default is 'auto'.
        binwidth (float): The width of the bins. Default is None. This will override the bins parameter.
        palette (str): The name of the palette or a list of colors. Default is None.
        alpha (float): The transparency of the histogram. Default is 0.7.
        hist_color (str): The color of the histogram. Default is 'black'.
        edge_color (str): The color of the edges. Default is 'black'.
        show_legend (bool): Whether to show the legend. Default is True.
        format_labels (bool): Whether to format the labels. Default is True.

    Returns:
        matplotlib.axes._subplots.AxesSubplot: The plot.
    """
    if color is not None:
        palette = get_palette(palette=palette, data=data, color=color)    

    ax = sns.histplot(data=data, 
                      x=x, 
                      y=y, 
                      hue=color,
                      stat=stat, 
                      bins=bins,
                      binwidth=binwidth,
                      color=hist_color,
                      ec=edge_color,
                      palette=palette if color else None, 
                      alpha=alpha,
                      ax=ax)
    if color:
        if show_legend:
            ax = customize_legend(ax=ax, color=color, size=None, style=None, format_labels=format_labels)
        else:
            ax.get_legend().remove()

    if format_labels:
        ax.set_xlabel(format_string(x), weight='bold', fontsize=11)
        if y:
            ax.set_ylabel(format_string(y), weight='bold', fontsize=11)
        else:
            ax.set_ylabel(format_string(stat), weight='bold', fontsize=11)
    else: 
        ax.set_xlabel(x, weight='bold', fontsize=11)
        if y:
            ax.set_ylabel(y, weight='bold', fontsize=11)
        else:
            ax.set_ylabel(stat, weight='bold', fontsize=11)
            
    return ax