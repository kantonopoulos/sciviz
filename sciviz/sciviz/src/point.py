from legend import customize_legend
from utils import format_string
from palettes import get_palette
import seaborn as sns


def point(ax, data, x, y, color=None, size=None, style=None, marker_color = 'black', marker_style = 'o', marker_size = 50, palette='jama', alpha=0.7):
    """Create a scatter plot.

    Args:
        ax (matplotlib.axes._subplots.AxesSubplot): The axis to plot on.
        data (pandas.DataFrame): The data to plot.
        x (str): The column name for the x-axis.
        y (str): The column name for the y-axis.
        color (str): The column name for the color attribute. Default is None.
        size (str): The column name for the size attribute. Default is None.
        style (str): The column name for the style attribute. Default is None.
        marker_color (str): The color of the markers. Default is 'black'. It will be ignored if color is not None.
        marker_style (str): The style of the markers. Default is 'o'. It will be ignored if style is not None.
        marker_size (int): The size of the markers. Default is 50. It will be ignored if size is not None.
        palette (str): The name of the palette or a list of colors. Default is None.
        alpha (float): The transparency of the points. Default is 0.7.

    Returns:
        matplotlib.axes._subplots.AxesSubplot: The plot.
    """
    if color is not None:
        palette = get_palette(palette=palette, data=data, color=color)    

    sns.scatterplot(data=data, 
                    x=x, 
                    y=y, 
                    hue=color, 
                    size=size, 
                    style=style, 
                    palette=palette if color else None, 
                    alpha=alpha, 
                    color=marker_color,
                    marker=marker_style,
                    s=marker_size,
                    ax=ax)
    if color or size or style:
        ax = customize_legend(ax=ax, color=color, size=size, style=style)

    ax.set_xlabel(format_string(x), weight='bold', fontsize=11)
    ax.set_ylabel(format_string(y), weight='bold', fontsize=11)

    return ax