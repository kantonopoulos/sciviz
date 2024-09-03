from legend import customize_legend
from utils import format_string, reformat_ticks_labels
from palettes import get_palette
import seaborn as sns


def jitter(ax, data, x, y, color=None, palette='jama', alpha=0.7, dodge=False, orient='v', points_color='black', points_size=5, show_legend=True, format_labels=True):
    """Create a jitter plot.

    Args:
        ax (matplotlib.axes._subplots.AxesSubplot): The axis to plot on.
        data (pandas.DataFrame): The data to plot.
        x (str): The column name for the x-axis.
        y (str): The column name for the y-axis.
        color (str): The column name for the color attribute. Default is None.
        palette (str): The name of the palette or a list of colors. Default is 'jama'.
        alpha (float): The transparency of the points. Default is 0.7.
        dodge (bool): Whether to dodge the points. Default is False.
        orient (str): The orientation of the plot. Default is 'v'.
        points_color (str): The color of the points. Default is 'black'.
        points_size (int): The size of the points. Default is 5.
        show_legend (bool): Whether to show the legend. Default is True.
        format_labels (bool): Whether to format the labels. Default is True.

    Returns:
        matplotlib.axes._subplots.AxesSubplot: The plot.
    """
    if color is not None:
        palette = get_palette(palette=palette, data=data, color=color)    

    sns.stripplot(data=data, 
                  x=x, 
                  y=y, 
                  hue=color, 
                  jitter=True,
                  dodge=dodge, 
                  palette=palette if color is not None else None, 
                  orient=orient, 
                  color=points_color,
                  size=points_size, 
                  alpha=alpha,
                  legend='full',
                  ax=ax)

    if color:
        if show_legend:
            ax = customize_legend(ax=ax, color=color, size=None, style=None, format_labels=format_labels)
        else:
            ax.get_legend().remove()

    if format_labels:
        ax.set_xlabel(format_string(x), weight='bold', fontsize=11)
        ax.set_ylabel(format_string(y), weight='bold', fontsize=11)
        ax = reformat_ticks_labels(ax, orient)
    else: 
        ax.set_xlabel(x, weight='bold', fontsize=11)
        ax.set_ylabel(y, weight='bold', fontsize=11)
        
    return ax