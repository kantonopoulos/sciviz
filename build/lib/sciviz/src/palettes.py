import seaborn as sns

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