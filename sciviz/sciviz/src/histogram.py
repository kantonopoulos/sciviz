from legend import customize_legend
from utils import format_string
from palettes import get_palette
import seaborn as sns


def histogram(ax, data, x, y=None, color=None, stat='count', bins='auto', binwidth=None, fill=True, hist_color='black', palette='jama', alpha=0.7):
    if color is not None:
        palette = get_palette(palette=palette, data=data, color=color)    

    ax = sns.histplot(data=data, 
                      x=x, 
                      y=y, 
                      hue=color,
                      stat=stat, 
                      bins=bins,
                      binwidth=binwidth,
                      fill=fill,
                      color=hist_color,
                      palette=palette if color else None, 
                      alpha=alpha,
                      ax=ax)
    if color:
        ax = customize_legend(ax=ax, color=color, size=None, style=None)

    ax.set_xlabel(format_string(x), weight='bold', fontsize=11)
    if y:
        ax.set_ylabel(format_string(y), weight='bold', fontsize=11)
    else:
        ax.set_ylabel(format_string(stat), weight='bold', fontsize=11)

    return ax