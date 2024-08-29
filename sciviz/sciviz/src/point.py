from legend import customize_legend, calc_facet_legend_pos
from utils import format_string
import matplotlib.pyplot as plt
import seaborn as sns

def point(data, x, y, color=None, size=None, style=None, palette=None, alpha=0.7, ax=None):
    if isinstance(ax, sns.axisgrid.FacetGrid):
        # Plot on a FacetGrid
        col_var = ax._col_var if ax.col_names is not None else None
        row_var = ax._row_var if ax.row_names is not None else None
        
        for var in [color, size, style]:
            if var and (var == col_var or var == row_var):
                data[var] = data[var].astype('category')

        ax.map_dataframe(sns.scatterplot, x=x, y=y, hue=color, size=size, style=style, palette=palette, alpha=alpha)
        ax.set_axis_labels(format_string(x), format_string(y), weight='bold', fontsize=11)
        ax.set_titles(row_template="{row_name}", col_template="{col_name}")
        for axis in ax.axes.flat:
           axis.set_title(format_string(axis.get_title()), weight='bold', fontsize=11)
        

        last_ax, pos_x, pos_y = calc_facet_legend_pos(ax)

        if color or size or style:
            customize_legend(last_ax, 
                             color=color, 
                             size=size, 
                             style=style,
                             x_pos=pos_x,
                             y_pos=pos_y)
    else:
        # Plot on a single axis
        sns.scatterplot(data=data, x=x, y=y, hue=color, size=size, style=style, palette=palette, alpha=alpha, ax=ax)
        if color or size or style:
            ax = customize_legend(ax=ax, color=color, size=size, style=style)

        # Make axis labels bold and larger
        ax.set_xlabel(format_string(x), weight='bold', fontsize=11)
        ax.set_ylabel(format_string(y), weight='bold', fontsize=11)

    return ax