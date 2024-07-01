import matplotlib.pyplot as plt
from .misc_utils import count_values_ordered 
from .palettes import color_seq_palette
from .legends import legend_create, legend_parameters


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