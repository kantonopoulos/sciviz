import matplotlib.pyplot as plt
from utils import format_string

def customize_legend_labels(ax, handles, labels, color=None, size=None, style=None):
    """Customize the legend labels and insert a spacer before each section title.

    Args:
        ax (matplotlib.axes._subplots.AxesSubplot): The axis to which the legend belongs.
        handles (list): The list of handles in the legend.
        labels (list): The list of labels in the legend.
        color (str): The name of the color attribute.
        size (str): The name of the size attribute.
        style (str): The name of the style attribute.

    Returns:
        list: The list of handles with spacers and section titles.
        list: The list of labels with spacers and section titles.
    """
    new_handles = []
    new_labels = []
    
    cnt = 0
    for handle, label in zip(handles, labels):
        if label in [color, size, style]:
            # Insert a spacer before the section title if it is not the first section
            if cnt != 0:
                new_handles.append(plt.Line2D([0], [0], color='none'))
                new_labels.append('')

            new_handles.append(handle)
            new_labels.append(label)
        else:
            if cnt == 0:
                chosen_attr = color or style or size
                title_handle = plt.Line2D([0], [0], color='none', label='Color')
                new_handles.append(title_handle)
                new_labels.append(chosen_attr)
                new_handles.append(handle)
                new_labels.append(label)
            else:
                new_handles.append(handle)
                new_labels.append(label)
        cnt += 1
    return new_handles, new_labels


def customize_legend_text(legend, color=None, size=None, style=None):
    """Customize the legend text and allign the section titles to the left.

    Args:
        legend (matplotlib.legend.Legend): The legend to customize.
        color (str): The name of the color attribute.
        size (str): The name of the size attribute.
        style (str): The name of the style attribute.

    Returns:
        matplotlib.legend.Legend: The customized legend.
    """
    # Customize the legend titles font and weight 
    for text in legend.get_texts():
        if text.get_text() in [color, size, style]:
            text.set_text(format_string(text.get_text()))
            text.set_fontsize(11)
            text.set_fontweight('bold')
            text.set_x(-35)
        else: 
            text.set_text(format_string(text.get_text()))
        
    return legend


def calc_facet_legend_pos(ax):
    """Calculate the position of the legend on a FacetGrid.

    Args:
        ax (seaborn.axisgrid.FacetGrid): The FacetGrid to which the legend belongs.

    Returns:
        matplotlib.axes._subplots.AxesSubplot: The last axis of the FacetGrid.
        float: The x position of the legend.
        float: The y position of the legend.
    """
    last_ax = ax.axes.flat[-1]
    num_cols = ax._ncol
    
    for i, axis in enumerate(ax.axes.flat):
        if axis == last_ax:
            row, col = divmod(i, num_cols)
            row += 1
            col += 1

    pos_x = ax._ncol - col + 1.15 if ax._ncol != col else 1.05
    pos_y = 0.5 * ax._nrow + 0.2 if ax._nrow > 1 else 0.5

    return last_ax, pos_x, pos_y


def customize_legend(ax, color=None, size=None, style=None, x_pos=1.05, y_pos=0.5):
    """Customize the legend labels, allign the section titles to the left and 
       insert a spacer before each section title.

    Args:
        ax (matplotlib.axes._subplots.AxesSubplot): The axis to which the legend belongs.
        color (str): The name of the color attribute.
        size (str): The name of the size attribute.
        style (str): The name of the style attribute.
        x_pos (float): The x position of the legend.
        y_pos (float): The y position of the legend.

    Returns:
        matplotlib.axes._subplots.AxesSubplot: The axis with the customized legend.
    """
    handles, labels = ax.get_legend_handles_labels()
    new_handles, new_labels = customize_legend_labels(ax=ax, 
                                                      handles=handles, 
                                                      labels=labels, 
                                                      color=color, 
                                                      size=size, 
                                                      style=style)

    # Redraw the legend with updated handles and labels
    legend = ax.legend(handles=new_handles, 
                       labels=new_labels, 
                       loc='center left', 
                       bbox_to_anchor=(x_pos, y_pos), 
                       frameon=False)

    legend = customize_legend_text(legend=legend, color=color, size=size, style=style)

    return ax