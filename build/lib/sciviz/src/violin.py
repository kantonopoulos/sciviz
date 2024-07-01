import matplotlib.pyplot as plt
import seaborn as sns
from palettes import color_seq_palette
from legends import legend_create, legend_parameters


def box_parameters(fill_color='white', edge_color='black', edge_width=1, median_color='black', median_width=1.5, outliers=True, outlier_color='black', outlier_shape='o', outlier_size=2):
    """
    Returns a dictionary of parameters for customizing a box plot.

    Args:
        fill_color (str, optional): The color to fill the box with. Defaults to 'white'.
        edge_color (str, optional): The color of the box's edges. Defaults to 'black'.
        edge_width (int, optional): The width of the box's edges. Defaults to 1.
        median_color (str, optional): The color of the median line. Defaults to 'black'.
        median_width (float, optional): The width of the median line. Defaults to 1.5.
        outliers (bool, optional): Whether to show outliers. Defaults to True.
        outlier_color (str, optional): The color of the outliers. Defaults to 'black'.
        outlier_shape (str, optional): The shape of the outliers. Defaults to 'o'.
        outlier_size (int, optional): The size of the outliers. Defaults to 2.

    Returns:
        dict: A dictionary of box plot parameters.

    """
    
    box_params = {
        'fill_color': fill_color,
        'edge_color': edge_color,  
        'edge_width': edge_width,
        'median_color': median_color,
        'median_width': median_width,
        'outliers': outliers,
        'outlier_color': outlier_color,
        'outlier_shape': outlier_shape,
        'outlier_size': outlier_size
    }
    return box_params


def violin(data, x, y, color=None, order=None, color_pal=None, color_order=None, fill=True, split=False, orient='v', width=0.4, edgecolor='black', alpha=0.7, legend=legend_parameters(orient='v', posx=1, posy=0.5, title=True, title_size=12, title_bold=False, label_size=11), box=None):
    """
    Creates a violin plot with optional box plot overlay.

    Args:
        data (DataFrame): The input data.
        x (str): The column name or index level name to group by on the x-axis.
        y (str): The column name or index level name to group by on the y-axis.
        color (str, optional): The column name or index level name to group by for color encoding. Defaults to None.
        order (list, optional): The order of the x-axis groups. Defaults to None.
        color_pal (list, optional): The color palette for color encoding. Defaults to None.
        color_order (list, optional): The order of the color groups. Defaults to None.
        fill (bool, optional): Whether to fill the violin plot. Defaults to True.
        split (bool, optional): Whether to split the violin plot when using hue. Defaults to False.
        orient (str, optional): The orientation of the violin plot ('v' for vertical, 'h' for horizontal). Defaults to 'v'.
        width (float, optional): The width of the violin plot. Defaults to 0.4.
        edgecolor (str, optional): The color of the violin plot edges. Defaults to 'black'.
        alpha (float, optional): The transparency of the violin plot. Defaults to 0.8.
        legend (dict, optional): The parameters for the legend. Defaults to legend_parameters().
        box (dict, optional): The parameters for the box plot overlay. Defaults to None.

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
    
    fig, ax = plt.subplots(figsize=(6, 6))
    sns.violinplot(
        data=data, 
        x=x, 
        y=y, 
        hue=color, 
        order=order,
        dodge='auto',
        split=split,
        hue_order=color_order,
        palette=color_pal, 
        color=single_color if single_color else '#2271B5', 
        orient=orient, 
        fill=fill,
        width=width,
        linewidth=0 if fill else 1,
        gap=0 if split else 0.2,
        inner=None,
        ax=ax
    )

    for patch in ax.collections:
        patch.set_alpha(alpha)

    if box:
        box_pal = [box['fill_color']]
        sns.boxplot(
            data=data, 
            x=x, 
            y=y, 
            hue=color if color is not None else (x if orient == 'v' else y),  
            gap=0 if color is None or color==x or color==y else 0.85,
            palette=box_pal, 
            showfliers=box['outliers'], 
            flierprops = dict(marker=box['outlier_shape'], markeredgecolor=box['outlier_color'], 
                              markerfacecolor=box['outlier_color'], markersize=box['outlier_size']),
            width=0.06 if color is None or color==x or color==y else 0.8, 
            boxprops = dict(zorder=2, edgecolor=box['edge_color'], linewidth=box['edge_width']),
            whiskerprops=dict(color=box['edge_color'], linewidth=box['edge_width']),
            capprops = dict(linewidth = 0),
            medianprops = dict(color = box['median_color'], linewidth = box['median_width']),
            dodge='auto', 
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