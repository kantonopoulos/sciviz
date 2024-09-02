from legend import customize_legend
from utils import format_string, set_alpha, reformat_ticks_labels
from palettes import get_palette
import seaborn as sns


def bar(ax, data, x, y, color=None, stat='mean', palette='jama', alpha=0.7, orient='v', bar_color='black', bar_width=0.4, edge_color='black', errorbar=None, errorbar_color='black', errorbar_linestyle='-', errorbar_linewidth=1, errorbar_capsize=0.2, show_legend=True, format_labels=True):
    """Create a bar plot.

    Args:
        ax (matplotlib.axes._subplots.AxesSubplot): The axis to plot on.
        data (pandas.DataFrame): The data to plot.
        x (str): The column name for the x-axis.
        y (str): The column name for the y-axis.
        color (str): The column name for the color attribute. Default is None.
        stat (str): The type of bar plot. Default is 'mean'.
        palette (str): The name of the palette or a list of colors. Default is 'jama'.
        alpha (float): The transparency of the bars. Default is 0.7.
        orient (str): The orientation of the bars. Default is 'v'.
        bar_color (str): The color of the bars. Default is 'black'.
        bar_width (float): The width of the bars. Default is 0.4.
        edge_color (str): The color of the edges. Default is 'black'.
        errorbar (str or tuple): Name of errorbar method (either 'ci', 'pi', 'se', or 'sd'), or a tuple with a method name and a level parameter. Default is None.
        errorbar_color (str): The color of the error bars. Default is 'black'.
        errorbar_linestyle (str): The style of the error bars. Default is '-'.
        errorbar_linewidth (float): The width of the error bars. Default is 1.
        errorbar_capsize (float): The size of the error bars caps. Default is 0.2.
        show_legend (bool): Whether to show the legend. Default is True.
        format_labels (bool): Whether to format the labels. Default is True.

    Returns:
        matplotlib.axes._subplots.AxesSubplot: The plot.
    """
    if color is not None:
        palette = get_palette(palette=palette, data=data, color=color)    

    sns.barplot(data=data,
                x=x,
                y=y, 
                hue=color,
                estimator=stat, 
                errorbar = errorbar,
                orient=orient, 
                palette=palette if color else None, 
                color=bar_color,
                width=bar_width, 
                dodge='auto', 
                edgecolor=edge_color, 
                linewidth=1, 
                capsize=errorbar_capsize if errorbar else 0,
                err_kws={'color': errorbar_color, 'linestyle': errorbar_linestyle, 'linewidth': errorbar_linewidth, 'alpha': 1} if errorbar else None,
                ax=ax)  
    
    ax = set_alpha(ax, alpha)

    if color:
        if show_legend:
            ax = customize_legend(ax=ax, color=color, size=None, style=None, format_labels=format_labels)
        else:
            ax.get_legend().remove()

    if format_labels:
        if orient == 'v':
            ax.set_xlabel(format_string(x), weight='bold', fontsize=11)
            ax.set_ylabel(format_string(y + " (" + stat + ")"), weight='bold', fontsize=11)
        else:
            ax.set_xlabel(format_string(x + " (" + stat + ")"), weight='bold', fontsize=11)
            ax.set_ylabel(format_string(y), weight='bold', fontsize=11)
        
        ax = reformat_ticks_labels(ax, orient)

    return ax