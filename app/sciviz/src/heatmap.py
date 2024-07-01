import matplotlib.pyplot as plt
import seaborn as sns
from pandas import DataFrame, Series
from palettes import color_seq_palette, color_cont_palette
from legends import legend_parameters, legend_title, legend_color, legend_spacer

def tick_parameters(xticks=True, yticks=True, xticks_angle=0, yticks_angle=0, ticklabel_size=11):
    """
    Sets the tick parameters for the plot.

    Args:
        xticks (bool, optional): Whether to show x-axis ticks. Defaults to True.
        yticks (bool, optional): Whether to show y-axis ticks. Defaults to True.
        xticks_angle (int, optional): The rotation angle of x-axis tick labels. Defaults to 0.
        yticks_angle (int, optional): The rotation angle of y-axis tick labels. Defaults to 0.
        ticklabel_size (int, optional): The font size of tick labels. Defaults to 11.

    Returns:
        dict: A dictionary containing the tick parameters.
        
    """
    tick_params = {
        'xticks': xticks,
        'yticks': yticks,  
        'xticks_angle': xticks_angle,
        'yticks_angle': yticks_angle,
        'ticklabel_size': ticklabel_size
    }
    return tick_params


def heatmap(data, gradient_pal='Spectral', row_cluster=True, col_cluster=True, dendrogram=0.1, row1_annot=None, row2_annot=None, col1_annot=None, col2_annot=None, row1_pal=None, row2_pal=None, col1_pal=None, col2_pal=None, cbar=True, ticks=tick_parameters(xticks=True, yticks=True, xticks_angle=0, yticks_angle=0, ticklabel_size=11), legend=legend_parameters(orient='v', posx=1.1, posy=0.5, title=True, title_size=12, title_bold=False, label_size=11)):
    """
    Generates a heatmap plot based on the provided data.

    Args:
        data (DataFrame): The input data to be plotted.
        gradient_pal (str, optional): The color palette for the heatmap. Defaults to 'Spectral'.
        row_cluster (bool, optional): Whether to cluster the rows. Defaults to True.
        col_cluster (bool, optional): Whether to cluster the columns. Defaults to True.
        dendrogram (float, optional): The ratio of the dendrogram size. Defaults to 0.1.
        row1_annot (str, optional): The name of the first row annotation. Defaults to None.
        row2_annot (str, optional): The name of the second row annotation. Defaults to None.
        col1_annot (tuple, optional): The first column annotation as a tuple of (data, name). Defaults to None.
        col2_annot (tuple, optional): The second column annotation as a tuple of (data, name). Defaults to None.
        row1_pal (list, optional): The color palette for the first row annotation. Defaults to None.
        row2_pal (list, optional): The color palette for the second row annotation. Defaults to None.
        col1_pal (list, optional): The color palette for the first column annotation. Defaults to None.
        col2_pal (list, optional): The color palette for the second column annotation. Defaults to None.
        cbar (bool, optional): Whether to show the colorbar. Defaults to True.
        ticks (dict, optional): The tick parameters for the heatmap. Defaults to tick_parameters(xticks=True, yticks=True, xticks_angle=0, yticks_angle=0, ticklabel_size=11).
        legend (dict, optional): The legend parameters for the heatmap. Defaults to legend_parameters().

    Returns:
        ax: The matplotlib Axes object containing the heatmap plot.

    """
    gradient_pal = color_cont_palette(users_palette=gradient_pal)  # "Spectral" for 0 to 1, "coolwarm" for -1 to 1

    # Create annotations
    data_rows = data.copy()
    row_colors = DataFrame()
    col_colors = DataFrame()
    handles = []
    labels = []
    titles = []
    
    if row1_annot != None:
        row1_pal = color_seq_palette(color_val=data[row1_annot], users_palette=row1_pal)
        row_data1 = data_rows.pop(row1_annot)
        legend_labels = data[row1_annot].unique()
        main_palette1 = row1_pal[:len(list(legend_labels))]
        row_color1 = dict(zip(row_data1.unique(), main_palette1))
        row_colors[row1_annot] = row_data1.map(row_color1)
        handles, labels, title = legend_title(handles, labels, data[row1_annot])
        titles.append(title)
        handles, labels = legend_color(data[row1_annot], row1_pal, None, handles, labels)
        legend_spacer(handles, labels)
    
    if row2_annot != None:
        row2_pal = color_seq_palette(color_val=data[row2_annot], users_palette=row2_pal)
        row_data2 = data_rows.pop(row2_annot)
        legend_labels = data[row2_annot].unique()
        second_palette1 = row2_pal[:len(list(legend_labels))]
        row_color2 = dict(zip(row_data2.unique(), second_palette1))
        row_colors[row2_annot] = row_data2.map(row_color2)
        handles, labels, title = legend_title(handles, labels, data[row2_annot])
        titles.append(title)
        handles, labels = legend_color(data[row2_annot], row2_pal, None, handles, labels)
        legend_spacer(handles, labels)
        
    if col1_annot != None:
        col_data1 = Series(col1_annot[0], name=col1_annot[1])
        col1_pal = color_seq_palette(color_val=col_data1, users_palette=col1_pal)
        legend_labels = col_data1.unique()
        main_palette2 = col1_pal[:len(list(legend_labels))]
        col_color1 = dict(zip(legend_labels, main_palette2))
        col_colors[col1_annot[1]] = col_data1.map(col_color1)
        handles, labels, title = legend_title(handles, labels, col_data1)
        titles.append(title)
        handles, labels = legend_color(col_data1, col1_pal, None, handles, labels)
        legend_spacer(handles, labels)
          
    if col2_annot != None:
        col_data2 = Series(col2_annot[0], name=col2_annot[1])
        col2_pal = color_seq_palette(color_val=col_data2, users_palette=col2_pal)
        legend_labels = col_data2.unique()
        second_palette2 = col2_pal[:len(list(legend_labels))]
        col_color2 = dict(zip(legend_labels, second_palette2))
        col_colors[col2_annot[1]] = col_data2.map(col_color2)
        handles, labels, title = legend_title(handles, labels, col_data2)
        titles.append(title)
        handles, labels = legend_color(col_data2, col2_pal, None, handles, labels)
        legend_spacer(handles, labels)

    if row1_annot == None and row2_annot == None:
        row_colors = None
    if col1_annot == None and col2_annot  == None:
        col_colors = None

    data_plot = data.select_dtypes(include='number')  # Select only numeric columns to be plotted
    
    if row_cluster or col_cluster:
        ax = sns.clustermap(
            data_plot,
            row_cluster=row_cluster, 
            col_cluster=col_cluster,
            row_colors=row_colors, 
            col_colors=col_colors,  
            cmap=gradient_pal, 
            dendrogram_ratio=dendrogram if dendrogram else 0.1, 
            colors_ratio=0.02, 
            cbar_pos=(1.05, 0.25, 0.01, 0.5) if cbar else None,
            figsize=(8, 8)
        )
        if dendrogram == None:  # Suppress dendrograms
            ax.ax_row_dendrogram.set_visible(False)
            ax.ax_col_dendrogram.set_visible(False)

        if ticks:
            plt.setp(ax.ax_heatmap.xaxis.get_majorticklabels(), rotation=ticks['xticks_angle'])   
            plt.setp(ax.ax_heatmap.yaxis.get_majorticklabels(), rotation=ticks['yticks_angle'])
            ax.ax_heatmap.tick_params(axis='x', labelsize=ticks['ticklabel_size'])
            ax.ax_heatmap.tick_params(axis='y', labelsize=ticks['ticklabel_size'])
            if ticks['xticks'] == None or ticks['xticks'] == False:
                ax.ax_heatmap.set_xticklabels([], visible=False)
                ax.ax_heatmap.tick_params(axis='x', which='both', bottom=False, top=False)                
            if ticks['yticks'] == None or ticks['yticks'] == False:
                ax.ax_heatmap.set_yticklabels([], visible=False)
                ax.ax_heatmap.tick_params(axis='y', which='both', left=False, right=False)
    else:
        fig, ax = plt.subplots(figsize=(10, 8))
        ax = sns.heatmap(
            data_plot,
            cmap=gradient_pal,
            cbar=cbar,
            cbar_kws={'shrink': 0.6, 'aspect': 50},
            ax=ax
        )

    
    if legend and handles:
        orientation = legend['orient']
        posx = legend['posx']
        posy = legend['posy']
        leg_title = legend['title']
        title_size = legend['title_size']
        title_bold = legend['title_bold']
        label_size = legend['label_size']
        if cbar == False:
            leg = plt.legend(
                handles=handles, 
                labels=labels,
                loc='center left' if orientation == 'v' else 'upper center', 
                bbox_to_anchor=(posx, posy), 
                labelspacing=1, 
                frameon=False,
                ncol=1 if orientation == 'v' else len(labels),
                columnspacing=1
            )
        else:
            leg = plt.legend(
                handles=handles, 
                labels=labels,
                loc='center left' if orientation == 'v' else 'center right',  
                bbox_to_anchor=(posx+7, posy),
                labelspacing=1, 
                frameon=False,
                ncol=1 if orientation == 'v' else len(labels),
                columnspacing=1
            )
        cnt = 0
        for text in leg.get_texts():
            if text.get_text() in titles:
                if leg_title:
                    if type(leg_title) == list:
                        text.set_text(leg_title[cnt])
                    text.set_ha('left')
                    if title_bold:
                        text.set_weight('bold')
                    text.set_x(-35)
                    text.set_fontsize(title_size)
                else: 
                    text.set_text('')
                cnt += 1
            else:
                text.set_fontsize(label_size) 
    return ax