import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn3
from palettes import color_seq_palette
from pie import label_parameters


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