import matplotlib.pyplot as plt
import seaborn as sns
from .palettes import color_seq_palette
from .legends import legend_create, legend_parameters


def crossbar_parameters(color_val=None, color_pal=['black'], barstyle='_', barsize=20, barwidth=3):
    """
    Returns a dictionary containing the parameters for a crossbar plot.

    Args:
        color_val (str, optional): The color value for the crossbar plot. Defaults to None.
        color_pal (str, optional): The color palette for the crossbar plot. Defaults to ['black'].
        barstyle (str, optional): The style of the crossbar. Defaults to '_'.
        barsize (float, optional): The size of the crossbar. Defaults to 20.
        barwidth (float, optional): The width of the crossbar. Defaults to 3.

    Returns:
        dict: A dictionary containing the crossbar parameters.

    """
    crossbar_params = {
        'color_val': color_val,
        'color_pal': color_pal, 
        'barstyle': barstyle, 
        'barsize': barsize,
        'barwidth': barwidth,
    }
    return crossbar_params


def jitter(data, x, y, color=None, order=None, jitter=True, dodge=False, size=50, color_pal=None, color_order=None, orient='v', alpha=0.7, legend=legend_parameters(orient='v', posx=1, posy=0.5, title=True, title_size=12, title_bold=False, label_size=11), crossbar=None):
    """
    Plots a jitter plot with optional crossbars.

    Args:
        data (DataFrame): The input data.
        x (str): The column name for the x-axis.
        y (str): The column name for the y-axis.
        color (str, optional): The column name for the color grouping. Defaults to None.
        order (list, optional): The order of the x-axis categories. Defaults to None.
        jitter (bool, optional): Whether to apply jitter to the data points. Defaults to True.
        dodge (bool, optional): Whether to dodge the data points. Defaults to False.
        size (int, optional): The size of the data points. Defaults to 50.
        color_pal (list, optional): The color palette for the color grouping. Defaults to None.
        color_order (list, optional): The order of the color groups. Defaults to None.
        orient (str, optional): The orientation of the plot ('v' for vertical, 'h' for horizontal). Defaults to 'v'.
        alpha (float, optional): The transparency of the data points. Defaults to 0.8.
        legend (dict, optional): The parameters for the legend. Defaults to legend_parameters().
        crossbar (dict, optional): The parameters for the crossbars. Defaults to None.

    Returns:
        Axes: The matplotlib Axes object containing the plot.

    """
    if color_pal is not None and color == None:
        single_color = color_pal[0]
    else:
        single_color = None
    if color:
        color_pal = color_seq_palette(color_val=data[color], users_palette=color_pal)

    fig, ax = plt.subplots(figsize=(6, 6))

    sns.stripplot(
        data=data, 
        x=x, 
        y=y, 
        hue=color if color else (x if color_pal else None), 
        order=order, 
        hue_order=color_order, 
        jitter=jitter, 
        dodge=dodge, 
        orient=orient, 
        color=single_color if single_color else '#2271B5', 
        palette=color_pal, 
        size=size/10, 
        alpha=alpha,
        zorder=0,
        ax=ax
    )
    
    if crossbar:
        sns.pointplot(
            data=data, 
            x=x, 
            y=y, 
            hue=crossbar['color_val'] if crossbar['color_val'] else (color if color else x),
            palette=crossbar['color_pal'] if crossbar['color_pal'] else color_pal,
            dodge=0.4 if dodge else False, 
            linestyle="none", 
            errorbar=None,
            marker=crossbar['barstyle'], 
            markersize=crossbar['barsize'], 
            markeredgewidth=crossbar['barwidth'],
            orient=orient,
            zorder=10,
            legend=False,
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
    return ax