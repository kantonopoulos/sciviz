import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.lines import Line2D
from utils import format_string


def customize_legend_labels(handles, labels, color=None, size=None, style=None):
    """Customize the legend labels and insert a spacer before each section title.

    Args:
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


def check_legend_handles(handles):
    """Check the type of the legend handles and calculate the x distance for the section titles.

    Args:
        handles (list): The list of handles in the legend.

    Returns:
        int: The x distance for the section titles.
    """
    handle = handles[1]
    if isinstance(handle, Rectangle):
        xdist = -45
    elif isinstance(handle, Line2D):
        xdist = -35
    else:
        xdist = -35

    return xdist


def customize_legend_text(legend, color=None, size=None, style=None, xdist=-35, format_labels=True):
    """Customize the legend text and allign the section titles to the left.

    Args:
        legend (matplotlib.legend.Legend): The legend to customize.
        color (str): The name of the color attribute.
        size (str): The name of the size attribute.
        style (str): The name of the style attribute.
        xdist (int): The x distance for the section titles.
        format_labels (bool): Whether to format the labels. Default is True.
        
    Returns:
        matplotlib.legend.Legend: The customized legend.
    """
    # Customize the legend titles font and weight 
    for text in legend.get_texts():
        if text.get_text() in [color, size, style]:
            if format_labels:
                text.set_text(format_string(text.get_text()))
                text.set_fontsize(11)
                text.set_fontweight('bold')
            else:
                text.set_text(text.get_text())
            text.set_x(xdist)
        else: 
            if format_labels:
                text.set_text(format_string(text.get_text()))
            else:
                text.set_text(text.get_text())
        
    return legend


def customize_legend(ax, color=None, size=None, style=None, x_pos=1.17, y_pos=0.5, format_labels=True):
    """Customize the legend labels, allign the section titles to the left and 
       insert a spacer before each section title.

    Args:
        ax (matplotlib.axes._subplots.AxesSubplot): The axis to which the legend belongs.
        color (str): The name of the color attribute.
        size (str): The name of the size attribute.
        style (str): The name of the style attribute.
        x_pos (float): The x position of the legend.
        y_pos (float): The y position of the legend.
        format_labels (bool): Whether to format the labels. Default is True.

    Returns:
        matplotlib.axes._subplots.AxesSubplot: The axis with the customized legend.
    """
    handles = ax.get_legend().legend_handles
    legend_texts = ax.get_legend().get_texts()
    labels = [text.get_text() for text in legend_texts]

    new_handles, new_labels = customize_legend_labels(handles=handles, 
                                                      labels=labels, 
                                                      color=color, 
                                                      size=size, 
                                                      style=style)

    # Redraw the legend with updated handles and labels
    legend = ax.legend(handles=new_handles, 
                       labels=new_labels, 
                       loc='center', 
                       bbox_to_anchor=(x_pos, y_pos), 
                       frameon=False)

    xdist = check_legend_handles(handles)
    legend = customize_legend_text(legend=legend, color=color, size=size, style=style, xdist=xdist, format_labels=format_labels)

    return ax


def create_labels_lists(user_labels):
    """Create lists of titles and labels from the user_labels dictionary.

    Args:
        user_labels (dict): The dictionary of titles and labels.

    Returns:
        list: The list of titles.
        list: The list of labels
    """
    titles_list = list(user_labels.keys())
    labels_list = []
    # Loop through the dictionary
    for key, values in user_labels.items():
        # Append the key
        labels_list.append(key)
        # Extend the list with the values
        labels_list.extend(values)
    return titles_list, labels_list


def customize_legend_labels_user(ax, handles, titles_list, labels_list):
    """Customize the legend labels and insert a spacer before each section title.

    Args:
        ax (matplotlib.axes._subplots.AxesSubplot): The axis to which the legend belongs.
        handles (list): The list of handles in the legend.
        titles_list (list): The list of titles in the legend.
        labels_list (list): The list of labels in the legend.

    Returns:
        list: The list of handles with spacers and section titles.
        list: The list of labels with spacers and section titles.
    """
    new_handles = []
    new_labels = []
    i = 0
    if len(titles_list) > 1:
        for label in labels_list:
            if label in titles_list:
                if i != 0:
                    new_handles.append(plt.Line2D([0], [0], color='none', label='Color'))
                    new_labels.append('')
                    i += 1
                
                new_handles.append(handles[i])
                new_labels.append(label)
            else:
                new_handles.append(handles[i])
                new_labels.append(label)
            i += 1
    else:
        for label in labels_list:
            if label in titles_list:
                title_handle = plt.Line2D([0], [0], color='none', label='Color')
                new_handles.append(title_handle)
                new_labels.append(label)
            else:
                new_handles.append(handles[i])
                new_labels.append(label)
            i += 1

    return new_handles, new_labels


def customize_legend_text_user(legend, titles_list, legendtitles_size=11, legendtitles_weight='bold', legendlabels_size=10, legendlabels_weight='normal', xdist=-35):
    """Customize the legend text and allign the section titles to the left.

    Args:
        legend (matplotlib.legend.Legend): The legend to customize.
        titles_list (list): The list of titles in the legend.
        legendtitles_size (int): The font size of the section titles. Default is 11.
        legendtitles_weight (str): The font weight of the section titles. Default is 'bold'.
        legendlabels_size (int): The font size of the labels. Default is 10.
        legendlabels_weight (str): The font weight of the labels. Default is 'normal'.

    Returns:
        matplotlib.legend.Legend: The customized legend.
    """
    for text in legend.get_texts():
        if text.get_text() in titles_list:
            text.set_fontsize(legendtitles_size)
            text.set_fontweight(legendtitles_weight)
            text.set_x(xdist)
        else: 
            text.set_fontsize(legendlabels_size)
            text.set_fontweight(legendlabels_weight)
        
    return legend


def legend_position(legend_pos):
    """Calculate the position of the legend for different legend orientations.

    Args:
        legend_pos (str): The orientation of the legend. One of 'side', 'bottom', or 'top'.

    Returns:
        float: The x position of the legend.
        float: The y position of the legend.
    """
    if legend_pos == 'side':
        pos_x = 1.17
        pos_y = 0.5
    elif legend_pos == 'bottom':
        pos_x = 0.5
        pos_y = -0.15
    elif legend_pos == 'top':
        pos_x = 0.5
        pos_y = 1.07
    else:
        raise Warning('Invalid legend position. Please choose one of the following: "side", "bottom", or "top".')
    
    return pos_x, pos_y


def customize_legend_user(ax, user_labels, legend=True, legend_pos='side', legendtitles_size=11, legendtitles_weight='bold', legendlabels_size=10, legendlabels_weight='normal'):
    """Customize the legend titles and labels, allign the section titles to the left and
       insert a spacer before each section title.

    Args:
        ax (matplotlib.axes._subplots.AxesSubplot): The axis to which the legend belongs.
        user_labels (dict): The dictionary of titles and labels.
        legend (bool): Whether to show the legend. Default is True.
        legend_pos (str): The orientation of the legend. One of 'side', 'bottom', or 'top'. Default is 'side'.
        legendtitles_size (int): The font size of the section titles. Default is 11.
        legendtitles_weight (str): The font weight of the section titles. Default is 'bold'.
        legendlabels_size (int): The font size of the labels. Default is 10.
        legendlabels_weight (str): The font weight of the labels. Default is 'normal'.

    Returns:
        matplotlib.axes._subplots.AxesSubplot: The axis with the customized legend.
    """
    if not legend:
        ax.legend().set_visible(False)
        return ax
    
    handles = ax.get_legend().legend_handles   
    titles_list, labels_list = create_labels_lists(user_labels=user_labels)
    new_handles, new_labels = customize_legend_labels_user(ax=ax, handles=handles, titles_list=titles_list, labels_list=labels_list)
    
    if type(legend_pos) == str:
        pos_x, pos_y = legend_position(legend_pos)
    else:
        pos_x = legend_pos[1]
        pos_y = legend_pos[2]
        legend_pos = legend_pos[0]
    
    legend = ax.legend(handles=new_handles, 
                       labels=new_labels, 
                       loc='center', 
                       bbox_to_anchor=(pos_x, pos_y),
                       frameon=False,
                       ncol=1 if legend_pos == 'side' else len(new_labels),
                       columnspacing=1)
    
    xdist = check_legend_handles(handles)
    legend = customize_legend_text_user(legend=legend, 
                                        titles_list=titles_list, 
                                        legendtitles_size=legendtitles_size, 
                                        legendtitles_weight=legendtitles_weight, 
                                        legendlabels_size=legendlabels_size, 
                                        legendlabels_weight=legendlabels_weight,
                                        xdist=xdist)

    return ax