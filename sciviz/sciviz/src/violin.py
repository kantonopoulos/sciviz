from legend import customize_legend
from utils import format_string, set_alpha, create_single_color_palette, reformat_ticks_labels
from palettes import get_palette
import seaborn as sns


def violin(ax, data, x, y, color=None, palette='jama', alpha=0.8, split=False, orient='v', violin_color='silver', violin_width=0.4, box=True, box_color='white', box_edgecolor='black', box_capsize=0, median_color='black', outliers=False, outliers_color='black', outliers_style='o', outliers_size=4, show_legend=True, format_labels=True):
    """Create a violin plot.

    Args:
        ax (matplotlib.axes._subplots.AxesSubplot): The axis to plot on.
        data (pandas.DataFrame): The data to plot.
        x (str): The column name for the x-axis.
        y (str): The column name for the y-axis.
        color (str): The column name for the color attribute. Default is None.
        palette (str): The name of the palette or a list of colors. Default is 'jama'.
        alpha (float): The transparency of the violin plot. Default is 0.6.
        split (bool): Whether to split the violins. Default is False.
        orient (str): The orientation of the violin plot. Default is 'v'.
        violin_color (str): The color of the violin. Default is 'grey'.
        violin_width (float): The width of the violin. Default is 0.4.
        box (bool): Whether to show the boxplot. Default is True.
        box_color (str): The color of the box. Default is 'white'.
        box_edgecolor (str): The color of the edges of the box. Default is 'black'.
        box_capsize (int): The size of the caps. Default is 0.
        median_color (str): The color of the median. Default is 'black'.
        outliers (bool): Whether to show the outliers. Default is False.
        outliers_color (str): The color of the outliers. Default is 'black'.
        outliers_style (str): The style of the outliers. Default is 'o'.
        outliers_size (int): The size of the outliers. Default is 4.
        show_legend (bool): Whether to show the legend. Default is True.
        format_labels (bool): Whether to format the labels. Default is True.

    Returns:
        matplotlib.axes._subplots.AxesSubplot: The plot.
    """
    if color is not None:
        palette = get_palette(palette=palette, data=data, color=color)    

    sns.violinplot(data=data,
                   x=x, 
                   y=y, 
                   hue=color, 
                   dodge='auto',
                   split=split,
                   palette=palette if color else None, 
                   color=violin_color, 
                   orient=orient, 
                   saturation=1,
                   fill=True,
                   width=violin_width,
                   linewidth=0,
                   gap=0 if split else 0.2,
                   inner=None,
                   legend='full',
                   ax=ax)
    
    ax = set_alpha(ax, alpha)

    # Add boxplots to the violins
    if box:
        box_palette = create_single_color_palette(data=data, color=color, palette=palette, single_color=box_color)

        PROPS = {
        'boxprops':{'edgecolor':box_edgecolor},
        'medianprops':{'color':median_color, 'linewidth':2},
        'whiskerprops':{'color':box_edgecolor},
        'capprops':{'color':box_edgecolor, 'linewidth':box_capsize}
        }
        
        sns.boxplot(data=data, 
                    x=x, 
                    y=y, 
                    hue=color if split == False else None, 
                    dodge='auto', 
                    palette=box_palette if color and split==False else None,
                    color=box_color,
                    showfliers=outliers, 
                    flierprops=dict(marker=outliers_style,  # Style of the outliers 
                                    markerfacecolor=outliers_color, 
                                    markeredgecolor=outliers_color, 
                                    markersize=outliers_size) 
                                    if outliers else None, 
                    orient=orient, 
                    width=0.06 if color is None or color==x or color==y or split==True else 0.4, 
                    gap=0 if color is None or color==x or color==y or split==True else 0.75,
                    legend=False,
                    zorder=100,
                    ax=ax,
                    **PROPS)
        '''sns.boxplot(
            data=data, 
            x=x, 
            y=y, 
            hue=color if color is not None else (x if orient == 'v' else y),  
            gap=0 if color is None or color==x or color==y else 0.85,
            palette=None,#box_palette if color is not None else None, 
            color=box_color,

            width=0.06 if color is None or color==x or color==y else 0.8, 
            
            dodge='auto', 
            ax=ax
            )'''

    if color:
        if show_legend:
            ax = customize_legend(ax=ax, color=color, size=None, style=None, format_labels=format_labels)
        else:
            ax.get_legend().remove()

    if format_labels:
        ax.set_xlabel(format_string(x), weight='bold', fontsize=11)
        ax.set_ylabel(format_string(y), weight='bold', fontsize=11)
        ax = reformat_ticks_labels(ax, orient)
    else: 
        ax.set_xlabel(x, weight='bold', fontsize=11)
        ax.set_ylabel(y, weight='bold', fontsize=11)
        
    return ax