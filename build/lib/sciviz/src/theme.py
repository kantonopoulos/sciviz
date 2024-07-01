import matplotlib.pyplot as plt
import seaborn as sns

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