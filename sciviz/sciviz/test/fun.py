import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn3
import seaborn as sns
from pandas import DataFrame, Series

def color_seq_palette(color_val, users_palette=None):
    """
    Generates a sequential color palette based on the given color values.

    Args:
        color_val (pandas.Series): A series of color values.
        users_palette (list, optional): A custom color palette provided by the user. Defaults to None.

    Returns:
        list: A sequential color palette.

    """
    if type(users_palette) == list:
        if len(color_val.unique()) > len(users_palette):
            # cycle the user-defined palette if it has fewer colors than the unique values in color_val
            color_pal = users_palette * (len(color_val.unique()) // len(users_palette)) + users_palette[:len(color_val.unique()) % len(users_palette)]
            color_pal = sns.color_palette(color_pal)
        else:
            color_pal = users_palette
            color_pal = sns.color_palette(color_pal)
    elif type(users_palette) == str:
        color_pal = users_palette
        color_pal = sns.color_palette(color_pal)
    elif len(color_val.unique()) > 10 and users_palette is None:
        color_pal = sns.color_palette('deep')
    else:
        minimal = [
            '#2271B5',
            '#DC0000',
            '#528A63',
            '#FEED70',
            '#603479',
            '#A6CEE3',
            '#E8A29A',
            '#ADC74F',
            '#B195AE',
            '#7E6148'
        ]
        color_pal = sns.color_palette(minimal)
    return color_pal[:len(color_val.unique())]


def color_cont_palette(users_palette):
    """
    Returns a color palette for continuous data.

    Args:
        users_palette (str): The name of the color palette to use.

    Returns:
        color_pal (matplotlib.colors.Colormap): The color palette as a matplotlib colormap object.

    """
    color_pal = sns.color_palette(users_palette, as_cmap=True)
    return color_pal


def shape_palette(shape_val, users_palette=None):
    """
    Generates a shape palette based on the unique values in the shape_val parameter.

    Args:
        shape_val (pandas.Series): A pandas Series containing shape values.
        users_palette (list, optional): A list of shape markers to use as the palette. 
            If not provided, a default palette will be used.

    Returns:
        list: A list of shape markers from the palette, corresponding to the unique values in shape_val.
    """
    if users_palette:
        shape_pal = users_palette
    else:
        shape_pal = ['o', 's', '^', 'X', 'd']
    return shape_pal[:len(shape_val.unique())]


def size_palette(size_val, min_size, max_size):
    """
    Generates a size palette dictionary based on the unique values in `size_val`.

    Args:
        size_val (pandas.Series): A pandas Series containing the size values.
        min_size (float): The minimum size value for the palette.
        max_size (float): The maximum size value for the palette.
        order (list, optional): A list specifying the order of size labels. Defaults to None.

    Returns:
        dict: A dictionary mapping size labels to corresponding size values.

    """
    n = len(size_val.unique())
    sizes = []
    for i in range(n):  # generate n size values between min_size and max_size
        size = min_size + (max_size - min_size) * i / (n - 1)
        sizes.append(size)
    
    size_labels = size_val.unique()
    size_pal = {val: size for val, size in zip(size_labels, sizes)}
    return size_pal


def set_palettes(data, color, shape, size, color_pal, shape_pal, size_pal):
    """
    Set the palettes for color, shape, and size based on the provided data and user preferences.

    Args:
        data (pandas Dataframe): pandas DataFrame containing the data.
        color (str): Column name for color values.
        shape (str): Column name for shape values.
        size (str): Column name for size values.
        color_pal (list or None): User-defined color palette.
        shape_pal (list or None): User-defined shape palette.
        size_pal (list or None): User-defined size palette.

    Returns:
        tuple: Color palette for the plot, shape palette for the plot, size palette for the plot, and a boolean indicating whether the size values are numeric or not.

    """
    if color:
        color_pal = color_seq_palette(color_val=data[color], users_palette=color_pal)
    else:
        color_pal = None

    if shape:
        shape_pal = shape_palette(shape_val=data[shape], users_palette=shape_pal)
    else:
        shape_pal = None

    size_num = False
    if type(size) not in [int, float, None] and size != None:
        size_pal = size_palette(size_val=data[size], min_size=size_pal[0], max_size=size_pal[1])  
    elif size == None: 
        size_pal = None       
    else:
        size_pal = None
        size_num = True
    return color_pal, shape_pal, size_pal, size_num


def set_order(color, color_order, shape, shape_order, size, size_order):
    """
    Sets the order of color, shape, and size based on the given parameters.

    Args:
        color (str): The color parameter.
        color_order (list or None): The order of colors.
        shape (str): The shape parameter.
        shape_order (list or None): The order of shapes.
        size (str): The size parameter.
        size_order (list or None): The order of sizes.

    Returns:
        tuple: Updated color_order, shape_order, and size_order.

    Notes: 
        In case of any conflicts between parameters, 'color' is given the highest priority. 
        Among the remaining parameters, 'shape' is prioritized over 'size'.

    """
    if color == shape and color == size:
        if color_order is not None:
            shape_order = color_order
            size_order = color_order
        elif shape_order is not None:
            color_order = shape_order
            size_order = shape_order
        else:
            color_order = size_order
            shape_order = size_order

    elif color == shape:
        if color_order is not None:
            shape_order = color_order
        else:
            color_order = shape_order

    elif color == size:
        if color_order is not None:
            size_order = color_order
        else:
            color_order = size_order

    elif shape == size:
        if shape_order is not None:
            size_order = shape_order
        else:
            shape_order = size_order
    return color_order, shape_order, size_order


def legend_color(color_val, color_pal, order, handles, labels):
    """
    Adds color legend to a plot.

    Args:
        color_val (array-like): Array of color values.
        color_pal (list): List of color palette.
        order (list, optional): List of ordered color labels. Defaults to None.
        handles (list): List of existing handles.
        labels (list): List of existing labels.

    Returns:
        tuple: Tuple containing updated handles and labels.
    """
    if order:
        color_labels = order
    else:
        color_labels = color_val.unique()
    color_handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10) 
                     for color in color_pal]
    handles.extend(color_handles)
    labels.extend(color_labels)
    return handles, labels


def legend_shape(shape_val, shape_pal, order, handles, labels):
    """
    Creates legend handles and labels for different shapes.

    Args:
        shape_val (pandas.Series): A series containing shape values.
        shape_pal (list): A list of shape markers.
        order (list or None): The order of the shape labels. Defaults to None.
        handles (list): A list of existing legend handles.
        labels (list): A list of existing legend labels.

    Returns:
        tuple: A tuple containing the updated handles and labels lists.
    """
    if order:
        shape_labels = order
    else:
        shape_labels = shape_val.unique()
    shape_handles = [plt.Line2D([0], [0], marker=shape, color='k', linestyle='', markersize=10) 
                     for shape in shape_pal]
    handles.extend(shape_handles)
    labels.extend(shape_labels)
    return handles, labels


def legend_size(size_val, size_pal, order, handles, labels):
    """
    Adds size legend to a plot.

    Args:
        size_val (pandas.Series): Array of size values.
        size_pal (dict): Dictionary mapping size values to colors.
        order (list, optional): A list specifying the order of size labels. Defaults to None.
        handles (list): List of existing handles.
        labels (list): List of existing labels.

    Returns:
        tuple: Tuple containing updated handles and labels.
    """
    if order:
        size_labels = order
    else:
        size_labels = size_val.unique()
    size_handles = [plt.Line2D([0], [0], marker='o', color='k', linestyle='', markersize=int(size)/12) 
                    for size in size_pal.values()]
    handles.extend(size_handles)
    labels.extend(size_labels)
    return handles, labels


def legend_colorshape(colorshape_val, color_pal, shape_pal, order, handles, labels):
    """
    Creates legend handles and labels based on color and shape values.

    Args:
        colorshape_val (pandas.Series): A series containing color and shape values.
        color_pal (list): A list of color values.
        shape_pal (list): A list of shape values.
        order (list, optional): A list specifying the order of colorshape labels. Defaults to None.
        handles (list): A list of existing legend handles.
        labels (list): A list of existing legend labels.

    Returns:
        tuple: A tuple containing the updated handles and labels lists.
    """
    if order:
        colorshape_labels = order
    else:
        colorshape_labels = colorshape_val.unique()
    colorshape_handles = [plt.Line2D([0], [0], marker=shape, color='w', linestyle='', markerfacecolor=color, markersize=10) 
                          for color, shape in zip(color_pal, shape_pal)]
    handles.extend(colorshape_handles)
    labels.extend(colorshape_labels)
    return handles, labels


def legend_colorsize(colorsize_val, color_pal, size_pal, order, handles, labels):
    """
    Creates legend handles and labels based on color and size values.

    Args:
        colorsize_val (pandas.Series): The color or size values.
        color_pal (list): The list of color values.
        size_pal (pandas.Series): The size values.
        order (list, optional): The order of the legend labels. Defaults to None.
        handles (list): The existing list of legend handles.
        labels (list): The existing list of legend labels.

    Returns:
        tuple: A tuple containing the updated list of handles and labels.
    """
    if order:
        colorsize_labels = order
    else:
        colorsize_labels = colorsize_val.unique()
    colorsize_handles = [plt.Line2D([0], [0], marker='o', color='w', linestyle='', markerfacecolor=color, markersize=int(size)/12)
                         for color, size in zip(color_pal, size_pal.values())]
    handles.extend(colorsize_handles)
    labels.extend(colorsize_labels)
    return handles, labels


def legend_shapesize(shapesize_val, shape_pal, size_pal, order, handles, labels):
    """
    Create legend handles and labels for shapes and sizes.

    Args:
        shapesize_val (pandas.Series): The values used for determining the shapes and sizes.
        shape_pal (list): The list of shape markers.
        size_pal (pandas.Series): The mapping of sizes to markers.
        order (list): The desired order of the legend labels.
        handles (list): The existing list of handles for the legend.
        labels (list): The existing list of labels for the legend.

    Returns:
        tuple: A tuple containing the updated handles and labels lists.

    """
    if order:
        shapesize_labels = order
    else:
        shapesize_labels = shapesize_val.unique()
    shapesize_handles = [plt.Line2D([0], [0], marker=shape, color='k', linestyle='', markersize=int(size)/12)
                         for shape, size in zip(shape_pal, size_pal.values())]
    handles.extend(shapesize_handles)
    labels.extend(shapesize_labels)
    return handles, labels


def legend_colorshapesize(colorshapesize_val, color_pal, shape_pal, size_pal, order, handles, labels):
    """
    Create legend handles and labels based on color, shape, and size values.

    Args:
        colorshapesize_val (pandas.Series): Series containing color, shape, and size values.
        color_pal (list): List of color values.
        shape_pal (list): List of shape values.
        size_pal (dict): Dictionary mapping size values to integers.
        order (list, optional): List specifying the order of the legend labels. Defaults to None.
        handles (list): List of existing handles for the legend.
        labels (list): List of existing labels for the legend.

    Returns:
        tuple: A tuple containing the updated handles and labels lists.
    """
    if order:
        colorshapesize_labels = order
    else:
        colorshapesize_labels = colorshapesize_val.unique()
    colorshapesize_handles = [plt.Line2D([0], [0], marker=shape, color='w', linestyle='', markerfacecolor=color, markersize=int(size)/12) 
                     for color, shape, size in zip(color_pal, shape_pal, size_pal.values())]
    handles.extend(colorshapesize_handles)
    labels.extend(colorshapesize_labels)
    return handles, labels


def legend_title(handles, labels, val):
    """
    Adds a legend title to the given handles and labels.

    Args:
        handles (list): A list of handles for the legend.
        labels (list): A list of labels for the legend.
        val (pandas.Series): The value to be used as the legend title.

    Returns:
        tuple: A tuple containing the updated handles, labels, and the legend title.
    """
    title = plt.Line2D([0], [0], color='none', label='Color')
    handles.append(title)
    labels.append(val.name)
    return handles, labels, val.name


def legend_spacer(handles, labels):
    """
    Adds a spacer to the legend by appending an empty handle and label.

    Args:
        handles (list): List of handles for the legend.
        labels (list): List of labels for the legend.

    Returns:
        tuple: A tuple containing the updated handles and labels lists.
    """
    handles.append(plt.Line2D([0], [0], color='none'))
    labels.append('')
    return handles, labels


def legend_order(data, color_val, color_pal, shape_val, shape_pal, size_val, size_pal):
    """
    Determines the order of legends to show based on the provided parameters.

    Args:
        data (pandas.Series): The data used to create the plot.
        color_val (str): The color value.
        color_pal (list): A list of color palettes.
        shape_val (str): The shape value.
        shape_pal (list): A list of shape palettes.
        size_val (str): The size value.
        size_pal (list): A list of size palettes.

    Returns:
        list: A list of tuples representing the order of legends to show. Each tuple contains the legend type,
        the corresponding data values, and the palettes to use.

    """
    legends_to_show = []
    if color_val is not None:
        if shape_val is not None and color_val == shape_val:
            if size_val is not None and color_val == size_val:
                legends_to_show.append(('color_shape_size', data[color_val], [color_pal, shape_pal, size_pal]))
            else:
                legends_to_show.append(('color_shape', data[color_val], [color_pal, shape_pal]))
                
        elif size_val is not None and color_val == size_val:
            legends_to_show.append(('color_size', data[color_val], [color_pal, size_pal]))
        else:
            legends_to_show.append(('color', data[color_val], color_pal))
    
    if shape_val is not None and shape_val != color_val:
        if size_val is not None and shape_val == size_val:
            legends_to_show.append(('shape_size', data[shape_val], [shape_pal, size_pal]))
        else:
            legends_to_show.append(('shape', data[shape_val], shape_pal))
    
    if type(size_val) not in [int, float, None] and size_val is not None and size_val != color_val and size_val != shape_val:
        legends_to_show.append(('size', data[size_val], size_pal))
    return legends_to_show


def legend_customize(ax, legend, titles, leg_title, title_size, title_bold, label_size):
    """
    Customize the legend in a matplotlib plot.

    Args:
        ax (matplotlib.axes.Axes): The axes object containing the plot.
        legend (matplotlib.legend.Legend): The legend object to be customized.
        titles (list): A list of titles to be displayed for specific legend entries.
        leg_title (bool or list): If True, display the titles from the 'titles' list as legend titles.
                                  If a list, display the corresponding title for each legend entry.
        title_size (int): The font size of the legend titles.
        title_bold (bool): If True, make the legend titles bold.
        label_size (int): The font size of the legend labels.

    Returns:
        matplotlib.axes.Axes: The modified axes object.
    """
    fig = ax.get_figure()
    fig.canvas.draw()
    cnt = 0
    for text in legend.get_texts():
        
        if text.get_text() in titles:
            if leg_title:
                if type(leg_title) == list:
                    text.set_text(leg_title[cnt])
                text.set_ha('left')
                if title_bold:
                    text.set_weight('bold')
                text.set_x(-35)
                text.set_fontsize(title_size)
            else: 
                text.set_text('')
            cnt += 1
        else:
            text.set_fontsize(label_size)
    return ax


def legend_create(ax, data, color_val, color_pal, color_order, shape_val, shape_pal, shape_order, size_val, size_pal, size_order, legend):
    """
    Create a legend for a matplotlib Axes object.

    Args:
        ax (matplotlib.axes.Axes): The Axes object to add the legend to.
        data (pandas.Series): The data used for creating the legend.
        color_val (str): The color value for the legend.
        color_pal (list): The color palette for the legend.
        color_order (list): The order of colors in the legend.
        shape_val (str): The shape value for the legend.
        shape_pal (list): The shape palette for the legend.
        shape_order (list): The order of shapes in the legend.
        size_val (str): The size value for the legend.
        size_pal (list): The size palette for the legend.
        size_order (list): The order of sizes in the legend.
        legend (dict): A dictionary containing legend properties.

    Returns:
        matplotlib.axes.Axes: The Axes object with the legend added.
    """
    legends_to_show = legend_order(data, color_val, color_pal, shape_val, shape_pal, size_val, size_pal)
    
    if legends_to_show == []:
        return ax
    
    orientation = legend['orient']
    posx = legend['posx']
    posy = legend['posy']
    leg_title = legend['title']
    title_size = legend['title_size']
    title_bold = legend['title_bold']
    label_size = legend['label_size']
    
    handles = []
    labels = []
    titles = []
    cnt = 0
    for (legend_type, val, pal) in legends_to_show:
        if cnt > 0:
            legend_spacer(handles, labels)
        if legend_type == 'color_shape_size':
            handles, labels, title = legend_title(handles, labels, val)
            titles.append(title)
            handles, labels = legend_colorshapesize(
                val, 
                pal[0], 
                pal[1], 
                pal[2], 
                color_order if color_order else (shape_order if shape_order else size_order), 
                handles, 
                labels
            )
        elif legend_type == 'color_shape':
            handles, labels, title = legend_title(handles, labels, val)
            titles.append(title)
            handles, labels = legend_colorshape(
                val, 
                pal[0], 
                pal[1], 
                color_order if color_order else shape_order, 
                handles, 
                labels
            )
        elif legend_type == 'color_size':
            handles, labels, title = legend_title(handles, labels, val)
            titles.append(title)
            handles, labels = legend_colorsize(
                val, 
                pal[0], 
                pal[1], 
                color_order if color_order else size_order, 
                handles, 
                labels
            )
        elif legend_type == 'shape_size':
            handles, labels, title = legend_title(handles, labels, val)
            titles.append(title)
            handles, labels = legend_shapesize(
                val, 
                pal[0], 
                pal[1], 
                shape_order if shape_order else size_order, 
                handles, 
                labels
            )
        elif legend_type == 'color':
            handles, labels, title = legend_title(handles, labels, val)
            titles.append(title)
            handles, labels = legend_color(val, pal, color_order, handles, labels)
        elif legend_type == 'shape':
            handles, labels, title = legend_title(handles, labels, val)
            titles.append(title)
            handles, labels = legend_shape(val, pal, shape_order, handles, labels)
        elif legend_type == 'size':
            handles, labels, title = legend_title(handles, labels, val)
            titles.append(title)
            handles, labels = legend_size(val, pal, size_order, handles, labels)
        cnt += 1

    legend = ax.legend(
        handles, 
        labels, 
        loc='center left' if orientation == 'v' else 'upper center', 
        bbox_to_anchor=(posx, posy), 
        labelspacing=1, 
        frameon=False, 
        ncol=1 if orientation == 'v' else len(labels),
        columnspacing=1
    )
    
    ax = legend_customize(ax=ax, legend=legend, titles=titles, leg_title=leg_title, title_size=title_size, title_bold=title_bold, label_size=label_size)
    return ax


def legend_parameters(orient='v', posx=1, posy=0.5, title=True, title_size=12, title_bold=False, label_size=11):
    """
    Creates a dictionary of legend parameters.

    Args:
        orient (str): The orientation of the legend ('horizontal' or 'vertical').
        posx (float): The x-coordinate of the legend position.
        posy (float): The y-coordinate of the legend position.
        title (str): The title of the legend.
        title_size (int): The font size of the legend title.
        title_bold (bool): Whether the legend title should be bold or not.
        label_size (int): The font size of the legend labels.

    Returns:
        dict: A dictionary containing the legend parameters.

    """
    legend_params = {
        'orient': orient, 
        'posx': posx, 
        'posy': posy, 
        'title': title, 
        'title_size': title_size, 
        'title_bold': title_bold, 
        'label_size': label_size
    }
    return legend_params


def x_y_axis_main(ax, x_label, y_label, xlim, ylim, label_size):
    """
    Set the x and y axis labels, limits, and font size properties for a given matplotlib Axes object.

    Args:
        ax (matplotlib.axes.Axes): The Axes object to modify.
        x_label (str): The label for the x-axis.
        y_label (str): The label for the y-axis.
        xlim (tuple): The limits for the x-axis (e.g., (xmin, xmax)).
        ylim (tuple): The limits for the y-axis (e.g., (ymin, ymax)).
        label_size (int): The font size for the axis labels.

    Returns:
        matplotlib.axes.Axes: The modified Axes object.

    """
    if x_label:
        ax.set_xlabel(xlabel=x_label)
    if y_label:
        ax.set_ylabel(ylabel=y_label)
    ax.xaxis.label.set_size(label_size)
    ax.yaxis.label.set_size(label_size)
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    return ax


def x_y_axis_ticks(ax, xticks, yticks, xticks_angle, yticks_angle, tick_size):
    """
    Set the tick labels and sizes for the x and y axes of a given matplotlib Axes object.

    Args:
        ax (matplotlib.axes.Axes): The Axes object to modify.
        xticks (list or None): The tick locations for the x-axis. If None, no changes are made to the x-axis ticks.
        yticks (list or None): The tick locations for the y-axis. If None, no changes are made to the y-axis ticks.
        xticks_angle (int): The rotation angle of the x-axis tick labels.
        yticks_angle (int): The rotation angle of the y-axis tick labels.
        tick_size (int): The font size of the tick labels.

    Returns:
        matplotlib.axes.Axes: The modified Axes object.

    """
    if xticks is not None:
        ax.set_xticks(xticks)
        ax.set_xticklabels(xticks)
    if yticks is not None:
        ax.set_yticks(yticks)
        ax.set_yticklabels(yticks)
    if xticks_angle:
        ax.tick_params(axis='x', rotation=xticks_angle)
        ax.set_xticklabels(ax.get_xticklabels(), ha='center', va='center')
    if yticks_angle:
        ax.tick_params(axis='y', rotation=yticks_angle)
        ax.set_yticklabels(ax.get_yticklabels(), ha='center', va='center')
    for label in ax.get_xticklabels():
        label.set_fontsize(tick_size)

    for label in ax.get_yticklabels():
        label.set_fontsize(tick_size)
    return ax


def theme(ax, theme='ticks', title=None, xlab=None, ylab=None, xlim=None, ylim=None, xticks=None, yticks=None, xticks_angle=0, yticks_angle=0, title_size=14, axislabel_size=12, ticklabel_size=11, font='Arial'):
    """
    Set the labels, limits, ticks, and font properties for the x and y axes of a matplotlib Axes object.

    Args:
        ax (matplotlib Axes): The Axes object to modify.
        theme (str): The theme style for the plot. Default is 'ticks'.
        title (str): The title of the plot.
        xlab (str): The label for the x-axis.
        ylab (str): The label for the y-axis.
        xlim (tuple): The limits for the x-axis (in the form of a tuple (xmin, xmax)).
        ylim (tuple): The limits for the y-axis (in the form of a tuple (ymin, ymax)).
        xticks (list): The tick locations for the x-axis.
        yticks (list): The tick locations for the y-axis.
        xticks_angle (int): The rotation angle of the x-axis tick labels.
        yticks_angle (int): The rotation angle of the y-axis tick labels.
        title_size (int): The font size for the title.
        axislabel_size (int): The font size for the axis labels.
        ticklabel_size (int): The font size for the tick labels.

    Returns:
        matplotlib Axes: The modified Axes object.

    """
    sns.set_style(style='ticks' if theme=='classic' else theme)
    if theme not in ['ticks', 'classic', 'darkgrid', 'whitegrid', 'dark', 'white']:
        raise ValueError("Invalid theme option. Please choose from 'ticks', 'classic', 'darkgrid', 'whitegrid', 'dark', or 'white'.")

    if theme == 'classic':
        ax.spines[['right', 'top']].set_visible(False)

    if title:
        plt.title(title, fontsize=title_size)

    ax = x_y_axis_main(ax=ax, x_label=xlab, y_label=ylab, xlim=xlim, ylim=ylim, label_size=axislabel_size)
    ax = x_y_axis_ticks(ax=ax, xticks=xticks, yticks=yticks, xticks_angle=xticks_angle, yticks_angle=yticks_angle, tick_size=ticklabel_size)

    return ax


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


def label_parameters(size=12, color='black'):
    """
    Returns a dictionary of label parameters.

    Args:
        size (int, optional): The font size of the label. Defaults to 12.
        color (str, optional): The color of the label. Defaults to 'black'.

    Returns:
        dict: A dictionary containing the label parameters.

    """
    label_params = {
        'size': size,
        'color': color
    }
    return label_params


def text_parameters(format='%1.1f%%', size=11, color='black'):
    """
    Returns a dictionary of text parameters.

    Args:
        format (str, optional): The format string for text. Defaults to '%1.1f%%'.
        size (int, optional): The font size. Defaults to 11.
        color (str, optional): The text color. Defaults to 'black'.

    Returns:
        dict: A dictionary containing the text parameters.

    """
    text_params = {
        'format': format,
        'size': size,
        'color': color
    }
    return text_params


def tick_parameters(xticks=True, yticks=True, xticks_angle=0, yticks_angle=0, ticklabel_size=11):
    """
    Sets the tick parameters for the plot.

    Args:
        xticks (bool, optional): Whether to show x-axis ticks. Defaults to True.
        yticks (bool, optional): Whether to show y-axis ticks. Defaults to True.
        xticks_angle (int, optional): The rotation angle of x-axis tick labels. Defaults to 0.
        yticks_angle (int, optional): The rotation angle of y-axis tick labels. Defaults to 0.
        ticklabel_size (int, optional): The font size of tick labels. Defaults to 11.

    Returns:
        dict: A dictionary containing the tick parameters.
        
    """
    tick_params = {
        'xticks': xticks,
        'yticks': yticks,  
        'xticks_angle': xticks_angle,
        'yticks_angle': yticks_angle,
        'ticklabel_size': ticklabel_size
    }
    return tick_params


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


def alpha_fill(ax, alpha):
    """
    Set the transparency of objects without chaninging their edge color.

    Args:
        ax (matplotlib.axes.Axes): The Axes object containing the bar plot.
        alpha (float): The transparency value for the bars.
    
    Returns:
        AxesSubplot: The matplotlib AxesSubplot object.

    """
    for patch in ax.patches:
            r, g, b, a = patch.get_facecolor()
            patch.set_facecolor((r, g, b, alpha))
    return ax


def edgecolor_pal(ax, fill, edgecolor, color_pal):
    """
    Sets the edgecolor of patches in the given ax object based on the color_pal.

    Args:
        ax (matplotlib.axes.Axes): The axes object to modify.
        fill (bool): Whether to fill the patches or not.
        edgecolor (str or None): The edgecolor to use for the patches. If None, the edgecolor will be set based on the color_pal.
        color_pal (list): A list of colors to use for setting the edgecolor of patches.

    Returns:
        matplotlib.axes.Axes: The modified axes object.

    """
    if fill != True and edgecolor == None:
        num_bars = len(ax.patches)
        for i in range(num_bars):
            ax.patches[i].set_edgecolor(color_pal[i])
    return ax


def count_values_ordered(data, color, order):
    """
    Counts the occurrences of each unique value in the specified column of a DataFrame and returns the counts in the specified order.

    Args:
        data (pandas.DataFrame): The DataFrame containing the data.
        color (str): The name of the column to count the values from.
        order (list or None): The desired order of the values. If None, the values will be returned in the default order.

    Returns:
        tuple: A tuple containing two lists. The first list contains the unique values in the specified order, and the second list contains the corresponding counts.

    """
    counts = data[color].value_counts()
    if order is not None:
        counts = counts.reindex(order)
    return counts.index.tolist(), counts.values.tolist()


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


def pie(data, color, order=None, color_pal=None, labels=None, text=None, alpha=0.7, donut=False, legend=legend_parameters(orient='v', posx=1, posy=0.5, title=True, title_size=12, title_bold=False, label_size=11)):
    """
    Creates a pie chart based on the given data.

    Args:
        data (DataFrame): The input data.
        color (str): The column name of the data to be used for coloring the pie slices.
        order (list, optional): The order in which the pie slices should be displayed. Defaults to None.
        color_pal (list, optional): The color palette to be used for coloring the pie slices. Defaults to None.
        labels (dict, optional): The labels configuration for the pie chart. Defaults to None.
        text (dict, optional): The text configuration for the pie chart. Defaults to None.
        alpha (float, optional): The transparency of the pie slices. Defaults to 0.8.
        donut (bool, optional): If True, creates a donut chart instead of a regular pie chart. Defaults to False.
        legend (dict, optional): The legend configuration for the pie chart. Defaults to legend_parameters().

    Returns:
        ax (Axes): The matplotlib Axes object containing the pie chart.

    """
    if color:
        color_pal = color_seq_palette(color_val=data[color], users_palette=color_pal)

    labels_val, values = count_values_ordered(data, color, order)

    if text:
        text_format = text['format']
        text_size = text['size']
        text_color = text['color']

    fig, ax = plt.subplots(figsize=(6, 6))
    patches, texts, autotexts = ax.pie(
        x=values, 
        labels=labels_val if labels else None, 
        autopct=text_format if text else '', 
        textprops=dict(color=text_color, fontsize=text_size) if text else None,
        startangle=90, 
        colors=color_pal, 
        wedgeprops={'alpha': alpha},
        pctdistance=0.85 if donut is True else 0.5
    )

    if labels:
        label_size = labels['size']
        label_color = labels['color']

    if donut == True:
        my_circle=plt.Circle( (0,0), 0.7, color='white')
        p = plt.gcf()
        p.gca().add_artist(my_circle)
    if labels != None:
        for text in range(len(texts)):
            texts[text].set_fontsize(label_size)
            texts[text].set_color(label_color)
    ax.axis('equal')
    
    if legend:
        ax = legend_create(
            ax=ax,
            data=data,
            color_val=color,
            color_pal=color_pal,
            color_order=None,
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


def venn(data, x, group, color_pal=None, alpha=0.7, labels=label_parameters(size=14, color='black')):
    """
    Creates a Venn diagram based on the given data.

    Args:
        data (DataFrame): The input data containing the values for the Venn diagram.
        x (str): The column name in the data to be used for the Venn diagram.
        group (str): The column name in the data to group the Venn diagram by.
        color_pal (list, optional): The color palette to use for the Venn diagram. Defaults to None.
        alpha (float, optional): The transparency level of the Venn diagram. Defaults to 0.8.
        labels (dict, optional): The parameters for customizing the labels of the Venn diagram. Defaults to label_parameters(size=14, color='black').

    Returns:
        matplotlib.axes.Axes: The axes object containing the Venn diagram.

    """
    grouped = data.groupby(group)[x].unique()
    set_var = [set(values) for values in grouped]
    labs = list(grouped.index)
    num_sets = len(labs)

    color_pal = color_seq_palette(color_val=data[group], users_palette=color_pal)
    
    plt.figure(figsize=(6, 6))
    if num_sets == 2:
        ax = venn2(
            set_var, 
            set_labels=labs if labels else None, 
            set_colors=color_pal, 
            alpha=alpha
        )
    elif num_sets == 3: 
        ax = venn3(
            set_var, 
            set_labels=labs if labels else None, 
            set_colors=color_pal, 
            alpha=alpha
        )
    else:
        print('Venn plots only support 2 or 3 sets.')

    if labels:
        for text in ax.set_labels:
            if text:
                text.set_fontsize(labels['size'])
                text.set_color(labels['color'])
    return ax


def heatmap(data, gradient_pal='Spectral', row_cluster=True, col_cluster=True, dendrogram=0.1, row1_annot=None, row2_annot=None, col1_annot=None, col2_annot=None, row1_pal=None, row2_pal=None, col1_pal=None, col2_pal=None, cbar=True, ticks=tick_parameters(xticks=True, yticks=True, xticks_angle=0, yticks_angle=0, ticklabel_size=11), legend=legend_parameters(orient='v', posx=1.1, posy=0.5, title=True, title_size=12, title_bold=False, label_size=11)):
    """
    Generates a heatmap plot based on the provided data.

    Args:
        data (DataFrame): The input data to be plotted.
        gradient_pal (str, optional): The color palette for the heatmap. Defaults to 'Spectral'.
        row_cluster (bool, optional): Whether to cluster the rows. Defaults to True.
        col_cluster (bool, optional): Whether to cluster the columns. Defaults to True.
        dendrogram (float, optional): The ratio of the dendrogram size. Defaults to 0.1.
        row1_annot (str, optional): The name of the first row annotation. Defaults to None.
        row2_annot (str, optional): The name of the second row annotation. Defaults to None.
        col1_annot (tuple, optional): The first column annotation as a tuple of (data, name). Defaults to None.
        col2_annot (tuple, optional): The second column annotation as a tuple of (data, name). Defaults to None.
        row1_pal (list, optional): The color palette for the first row annotation. Defaults to None.
        row2_pal (list, optional): The color palette for the second row annotation. Defaults to None.
        col1_pal (list, optional): The color palette for the first column annotation. Defaults to None.
        col2_pal (list, optional): The color palette for the second column annotation. Defaults to None.
        cbar (bool, optional): Whether to show the colorbar. Defaults to True.
        ticks (dict, optional): The tick parameters for the heatmap. Defaults to tick_parameters(xticks=True, yticks=True, xticks_angle=0, yticks_angle=0, ticklabel_size=11).
        legend (dict, optional): The legend parameters for the heatmap. Defaults to legend_parameters().

    Returns:
        ax: The matplotlib Axes object containing the heatmap plot.

    """
    gradient_pal = color_cont_palette(users_palette=gradient_pal)  # "Spectral" for 0 to 1, "coolwarm" for -1 to 1

    # Create annotations
    data_rows = data.copy()
    row_colors = DataFrame()
    col_colors = DataFrame()
    handles = []
    labels = []
    titles = []
    
    if row1_annot != None:
        row1_pal = color_seq_palette(color_val=data[row1_annot], users_palette=row1_pal)
        row_data1 = data_rows.pop(row1_annot)
        legend_labels = data[row1_annot].unique()
        main_palette1 = row1_pal[:len(list(legend_labels))]
        row_color1 = dict(zip(row_data1.unique(), main_palette1))
        row_colors[row1_annot] = row_data1.map(row_color1)
        handles, labels, title = legend_title(handles, labels, data[row1_annot])
        titles.append(title)
        handles, labels = legend_color(data[row1_annot], row1_pal, None, handles, labels)
        legend_spacer(handles, labels)
    
    if row2_annot != None:
        row2_pal = color_seq_palette(color_val=data[row2_annot], users_palette=row2_pal)
        row_data2 = data_rows.pop(row2_annot)
        legend_labels = data[row2_annot].unique()
        second_palette1 = row2_pal[:len(list(legend_labels))]
        row_color2 = dict(zip(row_data2.unique(), second_palette1))
        row_colors[row2_annot] = row_data2.map(row_color2)
        handles, labels, title = legend_title(handles, labels, data[row2_annot])
        titles.append(title)
        handles, labels = legend_color(data[row2_annot], row2_pal, None, handles, labels)
        legend_spacer(handles, labels)
        
    if col1_annot != None:
        col_data1 = Series(col1_annot[0], name=col1_annot[1])
        col1_pal = color_seq_palette(color_val=col_data1, users_palette=col1_pal)
        legend_labels = col_data1.unique()
        main_palette2 = col1_pal[:len(list(legend_labels))]
        col_color1 = dict(zip(legend_labels, main_palette2))
        col_colors[col1_annot[1]] = col_data1.map(col_color1)
        handles, labels, title = legend_title(handles, labels, col_data1)
        titles.append(title)
        handles, labels = legend_color(col_data1, col1_pal, None, handles, labels)
        legend_spacer(handles, labels)
          
    if col2_annot != None:
        col_data2 = Series(col2_annot[0], name=col2_annot[1])
        col2_pal = color_seq_palette(color_val=col_data2, users_palette=col2_pal)
        legend_labels = col_data2.unique()
        second_palette2 = col2_pal[:len(list(legend_labels))]
        col_color2 = dict(zip(legend_labels, second_palette2))
        col_colors[col2_annot[1]] = col_data2.map(col_color2)
        handles, labels, title = legend_title(handles, labels, col_data2)
        titles.append(title)
        handles, labels = legend_color(col_data2, col2_pal, None, handles, labels)
        legend_spacer(handles, labels)

    if row1_annot == None and row2_annot == None:
        row_colors = None
    if col1_annot == None and col2_annot  == None:
        col_colors = None

    data_plot = data.select_dtypes(include='number')  # Select only numeric columns to be plotted
    
    if row_cluster or col_cluster:
        ax = sns.clustermap(
            data_plot,
            row_cluster=row_cluster, 
            col_cluster=col_cluster,
            row_colors=row_colors, 
            col_colors=col_colors,  
            cmap=gradient_pal, 
            dendrogram_ratio=dendrogram if dendrogram else 0.1, 
            colors_ratio=0.02, 
            cbar_pos=(1.05, 0.25, 0.01, 0.5) if cbar else None,
            figsize=(8, 8)
        )
        if dendrogram == None:  # Suppress dendrograms
            ax.ax_row_dendrogram.set_visible(False)
            ax.ax_col_dendrogram.set_visible(False)

        if ticks:
            plt.setp(ax.ax_heatmap.xaxis.get_majorticklabels(), rotation=ticks['xticks_angle'])   
            plt.setp(ax.ax_heatmap.yaxis.get_majorticklabels(), rotation=ticks['yticks_angle'])
            ax.ax_heatmap.tick_params(axis='x', labelsize=ticks['ticklabel_size'])
            ax.ax_heatmap.tick_params(axis='y', labelsize=ticks['ticklabel_size'])
            if ticks['xticks'] == None or ticks['xticks'] == False:
                ax.ax_heatmap.set_xticklabels([], visible=False)
                ax.ax_heatmap.tick_params(axis='x', which='both', bottom=False, top=False)                
            if ticks['yticks'] == None or ticks['yticks'] == False:
                ax.ax_heatmap.set_yticklabels([], visible=False)
                ax.ax_heatmap.tick_params(axis='y', which='both', left=False, right=False)
    else:
        fig, ax = plt.subplots(figsize=(10, 8))
        ax = sns.heatmap(
            data_plot,
            cmap=gradient_pal,
            cbar=cbar,
            cbar_kws={'shrink': 0.6, 'aspect': 50},
            ax=ax
        )

    
    if legend and handles:
        orientation = legend['orient']
        posx = legend['posx']
        posy = legend['posy']
        leg_title = legend['title']
        title_size = legend['title_size']
        title_bold = legend['title_bold']
        label_size = legend['label_size']
        if cbar == False:
            leg = plt.legend(
                handles=handles, 
                labels=labels,
                loc='center left' if orientation == 'v' else 'upper center', 
                bbox_to_anchor=(posx, posy), 
                labelspacing=1, 
                frameon=False,
                ncol=1 if orientation == 'v' else len(labels),
                columnspacing=1
            )
        else:
            leg = plt.legend(
                handles=handles, 
                labels=labels,
                loc='center left' if orientation == 'v' else 'center right',  
                bbox_to_anchor=(posx+7, posy),
                labelspacing=1, 
                frameon=False,
                ncol=1 if orientation == 'v' else len(labels),
                columnspacing=1
            )
        cnt = 0
        for text in leg.get_texts():
            if text.get_text() in titles:
                if leg_title:
                    if type(leg_title) == list:
                        text.set_text(leg_title[cnt])
                    text.set_ha('left')
                    if title_bold:
                        text.set_weight('bold')
                    text.set_x(-35)
                    text.set_fontsize(title_size)
                else: 
                    text.set_text('')
                cnt += 1
            else:
                text.set_fontsize(label_size) 
    return ax