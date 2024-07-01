import matplotlib.pyplot as plt
import seaborn as sns
from .palettes import set_order, set_palettes
from .legends import legend_create, legend_parameters


def line(data, x, y, color=None, shape=None, stat='mean', errorbar=None, errorbar_style='bars', alpha=0.7, color_pal=None, shape_pal=None, color_order=None, shape_order=None, legend=legend_parameters(orient='v', posx=1, posy=0.5, title=True, title_size=12, title_bold=False, label_size=11)):
    """
    Plots a line chart using the provided data.

    Args:
        data (DataFrame): The input data.
        x (str): The column name for the x-axis.
        y (str): The column name for the y-axis.
        color (str, optional): The column name for coloring the lines. Defaults to None.
        shape (str, optional): The column name for shaping the lines. Defaults to None.
        stat (str, optional): The statistical function to apply. Defaults to None.
        errorbar (str or tuple, optional): Name of errorbar method (either 'ci', 'pi', 'se', or 'sd'), 
            or a tuple with a method name and a level parameter. Defaults to None.
        errorbar_style (str, optional): The style of error bars. Defaults to 'bars'.
        alpha (float, optional): The transparency of the lines. Defaults to 0.8.
        color_pal (str, optional): The color palette to use. Defaults to None.
        shape_pal (str, optional): The shape palette to use. Defaults to None.
        color_order (list, optional): The order of colors. Defaults to None.
        shape_order (list, optional): The order of shapes. Defaults to None.
        legend (dict, optional): The parameters for the legend. Defaults to legend_parameters().

    Returns:
        Axes: The matplotlib Axes object containing the line chart.

    """
    color_order, shape_order, size_order = set_order(color=color, color_order=color_order, shape=shape, shape_order=shape_order, size=None, size_order=None)
    color_pal, shape_pal, size_pal, size_num = set_palettes(data, color=color, shape=shape, size=None, color_pal=color_pal, shape_pal=shape_pal, size_pal=None)

    fig, ax = plt.subplots(figsize=(6, 6))
    sns.lineplot(
        data=data, 
        x=x, 
        y=y, 
        hue=color, 
        style=shape,
        palette=color_pal, 
        hue_order=color_order,        
        markers=shape_pal, 
        style_order=shape_order, 
        estimator=stat, 
        errorbar=errorbar,
        err_style=errorbar_style,
        alpha=alpha, 
        ax=ax
    )

    if legend:
        ax = legend_create(
            ax=ax,
            data=data,
            color_val=color,
            color_pal=color_pal,
            color_order=color_order,
            shape_val=shape,
            shape_pal=shape_pal,
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