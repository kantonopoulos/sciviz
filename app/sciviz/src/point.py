import matplotlib.pyplot as plt
import seaborn as sns
from .palettes import set_order, set_palettes
from .legends import legend_create, legend_parameters

def point(data, x, y, color=None, shape=None, size=50, alpha=0.7, color_pal=None, shape_pal=None, size_pal=[50, 150], color_order=None, shape_order=None, size_order=None, legend=legend_parameters(orient='v', posx=1, posy=0.5, title=True, title_size=12, title_bold=False, label_size=11)):
    """
    Create a scatter plot of x vs y with varying marker color, shape, and size.

    Args:
        data (pandas Dataframe): pandas DataFrame containing the data.
        x (str): Column name representing the x-axis values.
        y (str): Column name representing the y-axis values.
        color (str): Column name representing the color values. Default is None.
        shape (str): Column name representing the shape values. Default is None.
        size (str or int): Size of the markers. Either integer or column name or index representing the size values. Default is 50.
        alpha (float): Transparency of the markers. Default is 0.8.
        color_pal (str, list or None): Color palette for the color values. Default is None.
        shape_pal (str, list or None): Shape palette for the shape values. Default is None.
        size_pal (list or None): The limits for the size values in size palette (e.g., (size_min, size_max)). Default is [50, 150].
        color_order (list or None): Order of the color values. Default is None.
        shape_order (list or None): Order of the shape values. Default is None.
        size_order (list or None): Order of the size values. Default is None.
        legend (dict, optional): The parameters for the legend. Defaults to legend_parameters().

    Returns:
        matplotlib.axes.Axes: The matplotlib Axes object containing the scatter plot.

    """
    color_order, shape_order, size_order = set_order(color=color, color_order=color_order, shape=shape, shape_order=shape_order, size=size, size_order=size_order)
    if color_pal is not None and color == None:
        single_color = color_pal[0]
    else:
        single_color = None
    if shape_pal is not None and shape == None:
        single_shape = shape_pal[0]
    else:
        single_shape = None
    color_pal, shape_pal, size_pal, size_num = set_palettes(data, color=color, shape=shape, size=size, color_pal=color_pal, shape_pal=shape_pal, size_pal=size_pal)
    
    fig, ax = plt.subplots(figsize=(6, 6))
    sns.scatterplot(
        data=data,
        x=x,
        y=y,
        hue=color,
        size=None if size_num else size,
        style=shape,
        alpha=alpha,
        color=single_color if single_color else '#2271B5',
        marker=single_shape if single_shape else 'o',
        palette=color_pal,
        markers=shape_pal,
        sizes=size_pal,
        hue_order=color_order,
        style_order=shape_order,
        size_order=size_order,
        ax=ax
    )

    if size_num:
        ax.collections[0].set_sizes([size])
    
    if legend:
        ax = legend_create(
            ax=ax,
            data=data,
            color_val=color,
            color_pal=color_pal,
            color_order=color_order,
            shape_val=shape,
            shape_pal=shape_pal,
            shape_order=shape_order,
            size_val=size,
            size_pal=size_pal,
            size_order=size_order,
            legend=legend
        )
    elif ax.get_legend():
        legend = ax.get_legend()
        legend.remove()
    return ax