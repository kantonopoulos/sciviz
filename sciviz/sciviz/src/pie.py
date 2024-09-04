from legend import customize_legend
from utils import format_string
from palettes import get_palette
import matplotlib.pyplot as plt

def pie(ax, data, group, palette='jama', alpha=0.7, donut=False, labels=None, label_color='black', label_size=11, label_weight='bold', innertext=None, innertext_format='%1.1f%%', innertext_color='black', innertext_size=10, format_labels=True):
    """Create a pie chart.

    Args:
        ax (matplotlib.axes.Axes): The axes object to draw the plot on.
        data (pandas.DataFrame): The data to plot.
        group (str): The column name of the data to plot.
        palette (str): The color palette to use. Defaults to 'jama'.
        alpha (float): The transparency of the pie chart. Defaults to 0.7.
        donut (bool): Whether to create a donut chart. Defaults to False.
        labels (bool): Whether to show labels on the pie chart. Defaults to None.
        label_color (str): The color of the labels. Defaults to 'black'.
        label_size (int): The size of the labels. Defaults to 11.
        label_weight (str): The weight of the labels. Defaults to 'bold'.
        innertext (bool): Whether to show the percentage inside the pie chart. Defaults to None.
        innertext_format (str): The format of the percentage inside the pie chart. Defaults to '%1.1f%%'.
        innertext_color (str): The color of the percentage inside the pie chart. Defaults to 'black'.
        innertext_size (int): The size of the percentage inside the pie chart. Defaults to 10.
        format_labels (bool): Whether to format the labels. Defaults to True.

    Returns:
        matplotlib.axes.Axes: The axes object with the plot.        
    """
    palette = get_palette(palette=palette, data=data, color=group) 

    # Get the unique values of the color column and count them
    counts = data[group].value_counts()
    labels_val = counts.index.tolist()
    values = counts.values.tolist()


    patches, texts, autotexts = ax.pie(
        x=values, 
        labels=labels_val if labels else None, 
        autopct=innertext_format if innertext else '', 
        textprops=dict(color=innertext_color, fontsize=innertext_size) if innertext else None,
        startangle=90, 
        colors=palette, 
        wedgeprops={'alpha': alpha},
        pctdistance=0.85 if donut else 0.5
    )

    if donut:
        my_circle=plt.Circle( (0,0), 0.7, color='white')
        p = plt.gcf()
        p.gca().add_artist(my_circle)

    if labels != None:
        for text in range(len(texts)):
            if format_labels:
                formatted_text = format_string(texts[text].get_text())
                texts[text].set_text(formatted_text)
            texts[text].set_fontsize(label_size)
            texts[text].set_color(label_color)
            texts[text].set_fontweight(label_weight)
            
    ax.axis('equal')

    return ax