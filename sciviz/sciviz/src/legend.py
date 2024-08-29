import matplotlib.pyplot as plt
from utils import format_string

def customize_legend_labels(ax, handles, labels, color=None, size=None, style=None):
    new_handles = []
    new_labels = []
    
    cnt = 0
    for handle, label in zip(handles, labels):
        if label in [color, size, style]:
            # Insert a spacer before the section title
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


def customize_legend(ax, color=None, size=None, style=None, x_pos=1.05, y_pos=0.5):
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


def calc_facet_legend_pos(ax):
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
