from legend import customize_legend
from utils import format_string, set_alpha, create_single_color_palette, reformat_ticks_labels
from palettes import get_palette
import seaborn as sns


def boxplot(ax, data, x, y, color=None, palette='jama', alpha=0.7, orient='v', box_color='black', box_width=0.4, edge_color='black', median_color='black', caps=False, outliers=True, outliers_color='black', outliers_style='o', outliers_size=4, points=False, points_color='black', points_size=4, points_alpha=1, show_legend=True, format_labels=True):
    """Create a boxplot.
    
    Args:
        ax (matplotlib.axes._subplots.AxesSubplot): The axis to plot on.
        data (pandas.DataFrame): The data to plot.
        x (str): The column name for the x-axis.
        y (str): The column name for the y-axis.
        color (str): The column name for the color attribute. Default is None.
        palette (str): The name of the palette or a list of colors. Default is 'jama'.
        alpha (float): The transparency of the boxplot. Default is 0.7.
        orient (str): The orientation of the boxplot. Default is 'v'.
        box_color (str): The color of the box. Default is 'black'.
        box_width (float): The width of the box. Default is 0.4.
        edge_color (str): The color of the edges. Default is 'black'.
        median_color (str): The color of the median. Default is 'black'.
        caps (bool): Whether to show the caps. Default is False.
        outliers (bool): Whether to show the outliers. Default is True.
        outliers_color (str): The color of the outliers. Default is 'black'.
        outliers_style (str): The style of the outliers. Default is 'o'.
        outliers_size (int): The size of the outliers. Default is 4.
        points (bool): Whether to show the points with a stripplot on top. Default is False.
        points_color (str): The color of the points. Default is 'black'.
        points_size (int): The size of the points. Default is 4.
        points_alpha (float): The transparency of the points. Default is 1.
        show_legend (bool): Whether to show the legend. Default is True.
        format_labels (bool): Whether to format the labels. Default is True.
    
    Returns:
        matplotlib.axes._subplots.AxesSubplot: The plot.
    """
    if color is not None:
        palette = get_palette(palette=palette, data=data, color=color)    

    # Set the properties for the boxes
    PROPS = {
    'boxprops':{'edgecolor':edge_color},
    'medianprops':{'color':median_color, 'linewidth':2},
    'whiskerprops':{'color':edge_color},
    'capprops':{'color':edge_color}
    }

    sns.boxplot(data=data, 
                x=x, 
                y=y, 
                hue=color,  
                palette=palette if color else None,
                color=box_color,
                showcaps=caps,
                showfliers=outliers, 
                flierprops=dict(marker=outliers_style,  # Style of the outliers 
                                markerfacecolor=outliers_color, 
                                markeredgecolor=outliers_color, 
                                markersize=outliers_size) 
                                if outliers else None, 
                orient=orient, 
                width=box_width,
                gap=0.2, 
                legend='full',
                zorder=50,
                ax=ax,
                **PROPS)
    
    ax = set_alpha(ax, alpha)

    # Add points on top of the boxplot
    if points:
        points_palette = create_single_color_palette(data=data, color=color, palette=palette, single_color=points_color)
        
        sns.stripplot(data=data, 
                      x=x, 
                      y=y, 
                      hue=color, 
                      dodge=False if color is None else (False if x == color else (False if y == color else True)), 
                      palette=points_palette if color is not None else None, 
                      orient=orient, 
                      color=points_color if points_color is not None else ('black' if color is None else None),
                      size=points_size, 
                      alpha=points_alpha,
                      zorder=100,
                      legend=False,
                      ax=ax)

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