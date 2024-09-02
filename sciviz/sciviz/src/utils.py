def format_string(input_string):
    """Format a string by replacing underscores with spaces and capitalizing the first letter of each word.

    Args:
        input_string (string): The string to format.

    Returns:
        string: The formatted string.
    """
    formatted_string = input_string.replace("_", " ")
    formatted_string = ' '.join(word.capitalize() if not word.isupper() else word for word in formatted_string.split())

    return formatted_string


def set_alpha(ax, alpha):
    """Change the transparency of the patches in a plot.

    Args:
        ax (matplotlib.axes._subplots.AxesSubplot): The axis to modify.
        alpha (float): The transparency value.

    Returns:
        matplotlib.axes._subplots.AxesSubplot: The modified axis.
    """
    # Update the face colors of the patches
    for patch in ax.patches:
            r, g, b, a = patch.get_facecolor()
            patch.set_facecolor((r, g, b, alpha))

    legend = ax.get_legend()
    if legend:
        handles = legend.legend_handles
        # Update the face colors of the legend handles
        for handle in handles:
            r, g, b, a = handle.get_facecolor()
            handle.set_facecolor((r, g, b, alpha))

    return ax


def create_single_color_palette(data, color, palette, single_color='black'):
    """Create a single color palette.

    Args:
        data (pandas.DataFrame): The data.
        color (str): The column name for the color attribute.
        palette (str): The name of the palette or a list of colors.
        single_color (str): The single color to use.

    Returns:
        list: The single color palette.
    """
    if color:
        if single_color is not None:
            ncolors = len(data[color].unique())
            palette = [single_color] * ncolors
        else:
            if palette:
                palette = palette
            else:
                raise ValueError('No `palette` or `points_color` is defined.')
    else:
        palette = None
        
    return palette


def reformat_ticks_labels(ax, orient):
    new_ticks = []
    new_ticks_labels = []
    if orient == 'v':
        for tick, tick_label in zip(ax.get_xticks(), ax.get_xticklabels()):
            new_ticks.append(tick)
            new_ticks_labels.append(format_string(tick_label.get_text()))
        ax.set_xticks(new_ticks)
        ax.set_xticklabels(new_ticks_labels)
    else:
        for tick, tick_label in zip(ax.get_yticks(), ax.get_yticklabels()):
            new_ticks.append(tick)
            new_ticks_labels.append(format_string(tick_label.get_text()))
        ax.set_yticks(new_ticks)
        ax.set_yticklabels(new_ticks_labels)

    return ax
     