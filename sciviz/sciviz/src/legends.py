import matplotlib.pyplot as plt

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