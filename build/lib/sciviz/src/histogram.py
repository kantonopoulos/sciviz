import matplotlib.pyplot as plt
import seaborn as sns
from palettes import color_seq_palette
from legends import legend_create, legend_parameters


def histogram(data, x, y=None, color=None, stat='count', bins='auto', binwidth=None, color_pal=None, color_order=None, edgecolor='black', alpha=0.7, legend=legend_parameters(orient='v', posx=1, posy=0.5, title=True, title_size=12, title_bold=False, label_size=11)):
    """
    Plots a histogram using the given data and parameters.

    Args:
        data (DataFrame): The input data.
        x (str): The column name for the x-axis.
        y (str, optional): The column name for the y-axis. Defaults to None.
        color (str, optional): The column name for the color encoding. Defaults to None.
        stat (str, optional): The type of statistic to compute. Defaults to 'count'. Other possible values are 'density', 'percent', 'probability' and 'frequency'.
        bins (int or str, optional): The number of bins or the method to determine the number of bins. Defaults to 'auto'.
        binwidth (float, optional): The width of each bin. Defaults to None.
        color_pal (list, optional): The color palette for the color encoding. Defaults to None.
        color_order (list, optional): The order of colors for the color encoding. Defaults to None.
        edgecolor (str, optional): The color of the edges of the bars. Defaults to 'black'.
        alpha (float, optional): The transparency of the bars. Defaults to 0.8.
        legend (dict, optional): The parameters for the legend. Defaults to legend_parameters().

    Returns:
        AxesSubplot: The matplotlib AxesSubplot object.

    """
    if color_pal is not None and color == None:
        single_color = color_pal[0]
    else:
        single_color = None
    if color:
        color_pal = color_seq_palette(color_val=data[color], users_palette=color_pal)

    fig, ax = plt.subplots(figsize=(6, 6))
    sns.histplot(
        data=data, 
        x=x, 
        y=y, 
        hue=color, 
        alpha=alpha, 
        stat=stat, 
        bins=bins, 
        binwidth=binwidth, 
        palette=color_pal, 
        hue_order=color_order, 
        color=single_color if single_color else '#2271B5',
        edgecolor=edgecolor, 
        linewidth=1, 
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