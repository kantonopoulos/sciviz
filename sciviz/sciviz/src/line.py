from legend import customize_legend
from utils import format_string
from palettes import get_palette
import seaborn as sns


def line(ax, data, x, y, color=None, size=None, style=None, stat='mean', palette='jama', alpha=0.7, line_color='black', markers = True, errorbar=None, errorbar_style='band', show_legend=True, format_labels=True):
    """Create a line plot.

    Args:
        ax (matplotlib.axes.Axes): Axes object to draw the plot onto.
        data (pandas.DataFrame): Dataframe containing the data to be plotted.
        x (str): Column name of the x-axis variable.
        y (str): Column name of the y-axis variable.
        color (str): Column name of the color variable. Defaults to None.
        size (str): Column name of the size variable. Defaults to None.
        style (str): Column name of the style variable. Defaults to None.
        stat (str): Statistic to compute. Defaults to 'mean'.
        palette (str): Name of the color palette. Defaults to 'jama'.
        alpha (float): Transparency of the line. Defaults to 0.7.
        line_color (str): Color of the line. Defaults to 'black'.
        markers (bool): Whether to show markers. Defaults to True.
        errorbar (str): Column name of the errorbar variable. Defaults to None.
        errorbar_style (str): Style of the errorbar. Defaults to 'band'.
        show_legend (bool): Whether to show the legend. Defaults to True.
        format_labels (bool): Whether to format the labels. Defaults to True.

    Returns:
        matplotlib.axes.Axes: Axes object with the plot.
    """
    if color is not None:
        palette = get_palette(palette=palette, data=data, color=color)    

    sns.lineplot(data=data, 
                 x=x, 
                 y=y, 
                 hue=color, 
                 size=size, 
                 style=style, 
                 palette=palette if color else None, 
                 alpha=alpha, 
                 color=line_color,
                 dashes=False if markers else True,
                 marker='o' if markers else None,
                 markers=markers,
                 estimator=stat,
                 errorbar=errorbar,
                 err_style=errorbar_style,
                 ax=ax)
    
    if color or size or style:
        if show_legend:
            ax = customize_legend(ax=ax, color=color, size=size, style=style, format_labels=format_labels)
        else:
            ax.get_legend().remove()
    
    if format_labels:
        ax.set_xlabel(format_string(x), weight='bold', fontsize=11)
        ax.set_ylabel(format_string(y), weight='bold', fontsize=11)

    return ax