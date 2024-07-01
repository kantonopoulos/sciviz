import matplotlib.pyplot as plt
import seaborn as sns
from .misc_utils import alpha_fill
from .palettes import color_seq_palette
from .legends import legend_create, legend_parameters


def outlier_parameters(color='black', shape='o', size=5):
    """
    Returns a dictionary of parameters for plotting outliers.

    Args:
        color (str, optional): The color of the outliers. Defaults to 'black'.
        shape (str, optional): The shape of the outliers. Defaults to 'o'.
        size (int, optional): The size of the outliers. Defaults to 5.

    Returns:
        dict: A dictionary containing the outlier parameters.

    """
    outlier_params = {
        'color': color,
        'shape': shape,  
        'size': size
    }
    return outlier_params


def jitter_parameters(jitter=0.1, color_pal=None, size=50, alpha=0.8, pos='front'):
    """
    Returns a dictionary of jitter plot parameters.

    Args:
        jitter (float, optional): The amount of jitter to apply. Defaults to 0.1.
        color_pal (list, optional): A list of colors for the jitter plot. Defaults to None.
        size (float, optional): The size of the jitter points. Defaults to 50.
        alpha (float, optional): The transparency of the jitter points. Defaults to 0.8.
        pos (float, optional): The position of the jitter points. Defaults to 'front'.

    Returns:
        dict: A dictionary containing the jitter plot parameters.

    """
    jitter_params = {
        'jitter': jitter,
        'color_pal': color_pal, 
        'size': size,
        'alpha': alpha,
        'pos': pos
    }
    return jitter_params


def boxplot(data, x, y, color=None, order=None, outliers=outlier_parameters(color='black', shape='o', size=4), caps=False, color_pal=None, color_order=None, fill=True, orient='v', width=0.4, edgecolor='black', alpha=0.7, legend=legend_parameters(orient='v', posx=1, posy=0.5, title=True, title_size=12, title_bold=False, label_size=11), jitter=None):
    """
    Creates a box plot with optional overlaying data points.

    Args:
        data (DataFrame): The input data.
        x (str): The column name for the x-axis variable.
        y (str): The column name for the y-axis variable.
        color (str, optional): The column name for the color variable. Defaults to None.
        order (list, optional): The order of the categories on the x-axis. Defaults to None.
        outliers (dict, optional): The parameters for the outliers. Defaults to outlier_parameters(color='black', shape='o', size=5).
        caps (bool, optional): Whether to show caps. Defaults to False.
        color_pal (list, optional): The color palette for the plot. Defaults to None.
        color_order (list, optional): The order of the colors. Defaults to None.
        fill (bool, optional): Whether to fill the boxes. Defaults to True.
        orient (str, optional): The orientation of the plot ('v' for vertical, 'h' for horizontal). Defaults to 'v'.
        width (float, optional): The width of the boxes. Defaults to 0.4.
        edgecolor (str, optional): The color of the box edges. Defaults to 'black'.
        alpha (float, optional): The transparency of the boxes. Defaults to 0.8.
        legend (legend_parameters, optional): The legend parameters. Defaults to legend_parameters().
        jitter (jitter_parameters, optional): The jitter parameters. Defaults to None.

    Returns:
        AxesSubplot: The matplotlib AxesSubplot object.

    """
    if color_pal is not None and color == None:
        single_color = color_pal[0]
    else:
        single_color = None
    if color:
        color_pal = color_seq_palette(color_val=data[color], users_palette=color_pal)

    if fill == False and edgecolor != None:
        color_pal = [edgecolor]

    if outliers:
        outliers_color = outliers['color']
        outliers_shape = outliers['shape']
        outliers_size = outliers['size']

    fig, ax = plt.subplots(figsize=(6, 6))
    sns.boxplot(
        data=data, 
        x=x, 
        y=y, 
        hue=color, 
        order=order,
        hue_order=color_order,
        palette=color_pal, 
        color=single_color if single_color else '#2271B5', 
        showfliers=True if outliers else False, 
        showcaps=caps,
        flierprops=dict(marker=outliers_shape, markerfacecolor=outliers_color, 
                        markeredgecolor=outliers_color, markersize=outliers_size) 
                        if outliers else None, 
        orient=orient, 
        fill=fill,
        width=width,
        gap=0.2,
        zorder=50,
        ax=ax
    )
        
    ax = alpha_fill(ax, alpha)

    if jitter:
        sns.stripplot(
            data=data, 
            x=x, 
            y=y, 
            hue=color, 
            order=order, 
            hue_order=color_order, 
            jitter=jitter['jitter'], 
            dodge=False if x == color else (False if y == color else True), 
            orient=orient, 
            color=single_color if single_color else '#2271B5', 
            palette=jitter['color_pal'] if jitter['color_pal'] else color_pal, 
            size=jitter['size']/10, 
            alpha=jitter['alpha'],
            zorder=100 if jitter['pos']=='front' else 0,
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