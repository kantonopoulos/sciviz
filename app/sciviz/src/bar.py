import matplotlib.pyplot as plt
import seaborn as sns
from misc_utils import alpha_fill, edgecolor_pal, count_values_ordered 
from palettes import color_seq_palette
from legends import legend_create, legend_parameters


def error_parameters(errorbar=('ci', 95), color_pal=['black'], linestyle='-', linewidth=1, capsize=0.2):
    """
    Returns a dictionary containing error plot parameters.

    Args:
        errorbar (tuple): Type of error bars. Default is ('ci', 95).
        color_pal (list): List of colors for error bars. Default is ['black'].
        linestyle (str): The line style for error bars. Default is '-'.
        linewidth (float): The line width for error bars. Default is 1.
        capsize (float): The length of the error bar caps. Default is 0.2.

    Returns:
        dict: A dictionary containing the error plot parameters.

    """
    error_params = {
        'errorbar': errorbar,
        'color_pal': color_pal, 
        'linestyle': linestyle, 
        'linewidth': linewidth,
        'capsize': capsize,  
    }
    return error_params


def bar(data, x, y, color=None, order=None, stat='mean', color_pal=None, color_order=None, fill=True, orient='v', width=0.4, edgecolor='black', alpha=0.7, legend=legend_parameters(orient='v', posx=1, posy=0.5, title=True, title_size=12, title_bold=False, label_size=11), errorbar=None):
    """
    Create a bar plot.

    Args:
        data (pandas.DataFrame): The input data.
        x (str): The column name for the x-axis.
        y (str): The column name for the y-axis. 
        color (str, optional): The column name for the color encoding. Defaults to None.
        order (list, optional): The order of the x-axis categories. Defaults to None.
        stat (str, optional): The statistical function to compute for each category. Defaults to 'mean'. Examples of possible values are 'mean', 'median', 'count', 'sum', 'min', 'max', 'std', etc. 
        color_pal (list, optional): The color palette for the color encoding. Defaults to None.
        color_order (list, optional): The order of the color encoding categories. Defaults to None.
        fill (bool, optional): Whether to fill the bars with color. Defaults to True.
        orient (str, optional): The orientation of the plot ('v' for vertical, 'h' for horizontal). Defaults to 'v'.
        width (float, optional): The width of the bars. Defaults to 0.4.
        edgecolor (str, optional): The color of the bar edges. Defaults to 'black'.
        alpha (float, optional): The transparency of the bars. Defaults to 0.8.
        legend (dict, optional): The legend parameters. Defaults to legend_parameters(orient='v', posx=1, posy=0.5, title=True, title_size=12, title_bold=False, label_size=11).
        errorbar (dict, optional): The errorbar parameters. Defaults to None.

    Returns:
        AxesSubplot: The matplotlib AxesSubplot object.

    """
    if color:
        color_pal = color_seq_palette(color_val=data[color], users_palette=color_pal)
    
    if errorbar:
        error_type = errorbar['errorbar']
        error_pal = errorbar['color_pal']
        error_line = errorbar['linestyle']
        error_width = errorbar['linewidth']
        error_cap = errorbar['capsize']
    
    fig, ax = plt.subplots(figsize=(6, 6))
    sns.barplot(
        data=data, 
        x=x, 
        y=y, 
        hue=color, 
        order=order, 
        hue_order=color_order, 
        estimator=stat, 
        errorbar = error_type if errorbar else None,
        orient=orient, 
        palette=color_pal, 
        fill=fill, 
        width=width, 
        dodge='auto', 
        edgecolor=edgecolor, 
        linewidth=1, 
        capsize=error_cap if errorbar else 0,
        err_kws={'color': error_pal[0], 'linestyle': error_line, 'linewidth': error_width, 'alpha': 1} if errorbar else None,
        ax=ax
    )  


    if legend:
        ax = legend_create(
            ax=ax,
            data=data,
            color_val=color,
            color_pal=color_pal,
            color_order=color_order,
            shape_val=None,
            shape_pal=None,
            shape_order=None,
            size_val=None,
            size_pal=None,
            size_order=None,
            legend=legend
        )
    elif ax.get_legend():
        legend = ax.get_legend()
        legend.remove()

    if fill:
        ax = alpha_fill(ax, alpha)
    ax = edgecolor_pal(ax, fill, edgecolor, color_pal)

    return ax