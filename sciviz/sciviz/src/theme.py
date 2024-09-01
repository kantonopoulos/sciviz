import matplotlib.pyplot as plt
import seaborn as sns
from legend import customize_legend_user


def plot_theme(ax, theme='ticks'):
    """Set the theme of the plot.

    Args:
        ax (matplotlib.axes._subplots.AxesSubplot): The axis to set the theme on.
        theme (str): The name of the theme. Default is 'ticks'. Options are 'ticks', 'classic', 'darkgrid', 'whitegrid', 'dark', or 'white'.

    Returns:
        matplotlib.axes._subplots.AxesSubplot: The axis with the theme set.
    """
    sns.set_style(style='ticks' if theme=='classic' else theme)
    if theme not in ['ticks', 'classic', 'darkgrid', 'whitegrid', 'dark', 'white']:
        raise ValueError("Invalid theme option. Please choose from 'ticks', 'classic', 'darkgrid', 'whitegrid', 'dark', or 'white'.")
    elif theme == 'classic':
        ax.spines[['right', 'top']].set_visible(False)
    
    return ax


def set_title(ax, 
              title=None, 
              title_size=12, 
              title_weight='bold', 
              subtitle=None, 
              subtitle_size=11, 
              subtitle_weight='normal'):
    """Set the title and subtitle of the plot.

    Args:
        ax (matplotlib.axes._subplots.AxesSubplot): The axis to set the title on.
        title (str): The title of the plot. Default is None.
        title_size (int): The font size of the title. Default is 12.
        title_weight (str): The font weight of the title. Default is 'bold'.
        subtitle (str): The subtitle of the plot. Default is None.
        subtitle_size (int): The font size of the subtitle. Default is 11.
        subtitle_weight (str): The font weight of the subtitle. Default is 'normal'.

    Returns:
        matplotlib.axes._subplots.AxesSubplot: The axis with the theme set.
    """
    if isinstance(ax, sns.axisgrid.FacetGrid):
        if title is not None:
            ax.figure.subplots_adjust(top=0.85)
        if subtitle is not None:
            plt.suptitle(title, fontsize=title_size, weight=title_weight)
            raise Warning("FacetGrid does not support subtitles.")
        else: 
            plt.suptitle(title, fontsize=title_size, weight=title_weight)
    else:
        if subtitle is not None:
            plt.suptitle(title, fontsize=title_size, weight=title_weight)
            plt.title(subtitle, fontsize=subtitle_size, weight=subtitle_weight)
        else: 
            plt.title(title, fontsize=title_size, weight=title_weight)
    
    return ax


def axes(ax, xlab=None, ylab=None, xlim=None, ylim=None, axislabel_size=11, axislabel_weight='bold'):
    """Set the labels and limits of the axes.

    Args:
        ax (matplotlib.axes._subplots.AxesSubplot): The axis to set the labels and limits on.
        xlab (str): The label for the x-axis. Default is None.
        ylab (str): The label for the y-axis. Default is None.
        xlim (tuple): The limits for the x-axis. Default is None.
        ylim (tuple): The limits for the y-axis. Default is None.
        axislabel_size (int): The font size of the axis labels. Default is 11.
        axislabel_weight (str): The font weight of the axis labels. Default is 'bold'.

    Returns:
        matplotlib.axes._subplots.AxesSubplot: The axis with the theme set.
    """
    if xlab is not None:
        ax.set_xlabel(xlabel=xlab)
    if ylab is not None:
        ax.set_ylabel(ylabel=ylab)
            
    ax.xaxis.label.set_size(axislabel_size)
    ax.yaxis.label.set_size(axislabel_size)
    ax.xaxis.label.set_weight(axislabel_weight)
    ax.yaxis.label.set_weight(axislabel_weight)
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)

    return ax


def axes_ticks(ax, xticks=None, yticks=None, xticks_angle=0, yticks_angle=0, ticklabel_size=10):
    """Set the ticks and tick labels of the axes.

    Args:
        ax (matplotlib.axes._subplots.AxesSubplot): The axis to set the ticks and tick labels on.
        xticks (list): The ticks for the x-axis. Default is None.
        yticks (list): The ticks for the y-axis. Default is None.
        xticks_angle (int): The rotation angle of the x-axis tick labels. Default is 0.
        yticks_angle (int): The rotation angle of the y-axis tick labels. Default is 0.
        ticklabel_size (int): The font size of the tick labels. Default is 10.

    Returns:
        matplotlib.axes._subplots.AxesSubplot: The axis with the theme set.
    """
    if xticks is not None:
        ax.set_xticks(xticks)
        ax.set_xticklabels(xticks)
    if yticks is not None:
        ax.set_yticks(yticks)
        ax.set_yticklabels(yticks)
        
    ax.tick_params(axis='x', rotation=xticks_angle)
    ax.tick_params(axis='y', rotation=yticks_angle)

    for label in ax.get_xticklabels():
        label.set_fontsize(ticklabel_size)
    for label in ax.get_yticklabels():
        label.set_fontsize(ticklabel_size)

    return ax


def theme(ax, 
          theme='ticks', 
          title=None, 
          subtitle=None, 
          xlab=None, 
          ylab=None, 
          xlim=None, 
          ylim=None,
          xticks=None,
          yticks=None,
          xticks_angle=0,
          yticks_angle=0,
          title_size=12,
          title_weight='bold',
          subtitle_size=11,
          subtitle_weight='normal',
          axislabel_size=11,
          axislabel_weight='bold',
          ticklabel_size=10,
          legend=True,
          legend_labels=None,
          legendtitles_size=14,
          legendtitles_weight="normal",
          legendlabels_size=9,
          legendlabels_weight="bold",
          legend_pos="side"
          ):
    """Modify the aesthetics of the plot. Set the theme, title, subtitle, labels, limits, ticks, and tick labels.

    Args:
        ax (matplotlib.axes._subplots.AxesSubplot): The axis to set the theme on.
        theme (str): The name of the theme. Default is 'ticks'. Options are 'ticks', 'classic', 'darkgrid', 'whitegrid', 'dark', or 'white'.
        title (str): The title of the plot. Default is None.
        subtitle (str): The subtitle of the plot. Default is None.
        xlab (str): The label for the x-axis. Default is None.
        ylab (str): The label for the y-axis. Default is None.
        xlim (tuple): The limits for the x-axis. Default is None.
        ylim (tuple): The limits for the y-axis. Default is None.
        xticks (list): The ticks for the x-axis. Default is None.
        yticks (list): The ticks for the y-axis. Default is None.
        xticks_angle (int): The rotation angle of the x-axis tick labels. Default is 0.
        yticks_angle (int): The rotation angle of the y-axis tick labels. Default is 0.
        title_size (int): The font size of the title. Default is 12.
        title_weight (str): The font weight of the title. Default is 'bold'.
        subtitle_size (int): The font size of the subtitle. Default is 11.
        subtitle_weight (str): The font weight of the subtitle. Default is 'normal'.
        axislabel_size (int): The font size of the axis labels. Default is 11.
        axislabel_weight (str): The font weight of the axis labels. Default is 'bold'.
        ticklabel_size (int): The font size of the tick labels. Default is 10.
        legend (bool): Whether to show the legend. Default is True.
        legend_labels (list): The labels for the legend. Default is None.
        legendtitles_size (int): The font size of the legend titles. Default is 14.
        legendtitles_weight (str): The font weight of the legend titles. Default is 'normal'.
        legendlabels_size (int): The font size of the legend labels. Default is 9.
        legendlabels_weight (str): The font weight of the legend labels. Default is 'bold'.
        legend_pos (str or list): The position of the legend. Default is 'side'. Options are 'side', 'bottom', 'top'. If it is a list, the second and third elements are the x and y positions of the legend.

    Returns:
        matplotlib.axes._subplots.AxesSubplot: The axis with the theme set.
    """
    ax = plot_theme(ax=ax, theme=theme)
    
    ax = set_title(ax=ax, 
                   title=title, 
                   title_size=title_size, 
                   title_weight=title_weight, 
                   subtitle=subtitle, 
                   subtitle_size=subtitle_size, 
                   subtitle_weight=subtitle_weight)       
    
    ax = axes(ax=ax, 
              xlab=xlab, 
              ylab=ylab, 
              xlim=xlim, 
              ylim=ylim, 
              axislabel_size=axislabel_size, 
              axislabel_weight=axislabel_weight)
    
    ax = axes_ticks(ax=ax, 
                    xticks=xticks, 
                    yticks=yticks, 
                    xticks_angle=xticks_angle, 
                    yticks_angle=yticks_angle, 
                    ticklabel_size=ticklabel_size)
    
    if legend_labels is not None:
        ax = customize_legend_user(ax=ax,                        
                                   user_labels=legend_labels,
                                   legend=legend, 
                                   legend_pos=legend_pos,
                                   legendtitles_size=legendtitles_size, 
                                   legendtitles_weight=legendtitles_weight, 
                                   legendlabels_size=legendlabels_size, 
                                   legendlabels_weight=legendlabels_weight)
    return ax


