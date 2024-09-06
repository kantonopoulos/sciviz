import seaborn as sns
import matplotlib.pyplot as plt
from pandas import DataFrame, Series
from palettes import get_palette
from utils import format_string

def heatmap(ax, data, cluster_rows=True, cluster_cols=True, palette='Spectral', dendrogram=0.1, row_annot=None, row_pal=None, col_annot=None, col_pal=None, col_annot_names=None, show_cbar=True, cbar_ticks=None, cbar_lim=None, xticks=False, yticks=False, format_labels=True):
    # Process row annotations
    if row_annot:  
        if isinstance(row_annot, str):  # Handle single row annotation
            row_annot = [row_annot]
            row_pal = [row_pal]
        row_colors = DataFrame(index=data.index)
        for annot, pal in zip(row_annot, row_pal):
            pal = get_palette(palette=pal, data=data, color=annot) 
            ra = data.pop(annot) 
            lut = dict(zip(ra.unique(), pal))
            row_colors[annot] = ra.map(lut)
    
    # Process column annotations
    col_colors = DataFrame(index=data.columns)
    if col_annot:
            col_colors = []
            if col_annot:
                for col in data.columns:
                    if col in col_annot:
                        col_index = col_annot.index(col)
                        col_colors.append(col_pal[col_index])
                    else:
                        col_colors.append('white')  # Default color for columns not in col_annot
            col_colors = Series(col_colors, index=data.columns, name=col_annot_names)

    if cluster_rows or cluster_cols:
        fig = ax.figure  # Get the figure created by sciviz
        fig_size = fig.get_size_inches()
        plt.close(fig)  # Remove the figure created by sciviz as it is not required for clustermap

        ax = sns.clustermap(data, 
                            cmap=palette,
                            dendrogram_ratio=dendrogram,
                            cbar_pos=(1.05, 0.25, 0.01, 0.5) if show_cbar else None,
                            row_cluster=cluster_rows, 
                            col_cluster=cluster_cols, 
                            row_colors=row_colors, 
                            col_colors=col_colors, 
                            xticklabels=xticks, 
                            yticklabels=yticks,
                            figsize=fig_size)
        
        if show_cbar:
            cbar = ax.ax_heatmap.collections[0].colorbar

    else:
        ax = sns.heatmap(data, 
                         cmap=palette, 
                         xticklabels=xticks, 
                         yticklabels=yticks,
                         ax=ax)

        if show_cbar:
            cbar = ax.collections[0].colorbar
    
    if cbar:
        if cbar_ticks:
            cbar.set_ticks(cbar_ticks)
        if cbar_lim:
            cbar.mappable.set_clim(*cbar_lim)
        
    return ax