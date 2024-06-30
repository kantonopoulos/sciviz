---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Pie

A pie chart, or `pie` in SciViz, is a type of plot that displays proportions. It consists of a circle divided into sectors that each represent a proportion of the whole. They are commonly used for visualizing proportions and compare groups.

## Usage
```python
pie(data, color, order=None, color_pal=None, labels=None, text=None, alpha=0.8, 
        donut=False, legend=legend_parameters())
```

## Arguments

- `data`: The dataset to be plotted.
- `color`: The name of the variable in data that will determine the color of the pie slices.
- `order`: The order in which to display the pie slices. If not specified, the order in the data is used.
- `color_pal`: The color palette to use for the pie slices. If not specified, a default palette is used.
- `labels`: The labels for the pie slices. If not specified, the values of the color variable are used.
- `text`: The text to display on the pie slices. If not specified, no text is displayed.
- `alpha`: The transparency of the pie slices. Ranges from 0 (completely transparent) to 1 (completely opaque).
- `donut`: Whether to create a donut chart (a pie chart with a hole in the middle). If True, a donut chart is created. If False (the default), a regular pie chart is created.
- `legend`: Parameters for the legend. This should be a `legend_parameters` object, which has its own arguments. If not specified, a default legend is shown.

### Labels

```{note}
This is the first time in this package when we will describe functions that act as arguments. In this package all functions that are named as `*_parameters` are functions that return a dictionary that is further utilized in the main function.
```

```python
label_parameters(size=12, font='Arial', color='black')
```

This function allows you to customize the appearance of pie slices labels.

**Arguments**:
- `size`: The font size of the labels. Default is 12.
- `font`: The font of the labels. Default is 'Arial'.
- `color`: The color of the labels. Default is 'black'.

### Text

```python
text_parameters(format='%1.1f%%', size=11, font='Arial', color='black')
```

This function allows you to customize the appearance of pie slices inner text.

**Arguments**:
- `format`: The format of the text. Default is '%1.1f%%', which means the text will be displayed as a percentage with one decimal place.
- `size`: The font size of the text. Default is 11.
- `font`: The font of the text. Default is 'Arial'.
- `color`: The color of the text. Default is 'black'.

## Examples

Let's create a simple pie chart by plotting the proportions of the 3 different species. 
```{code-cell}
:tags: ["remove-cell"]
import warnings
warnings.filterwarnings('ignore')
import seaborn as sns
import sciviz as sv
iris = sns.load_dataset('iris')
iris['size'] = iris['sepal_length'].apply(lambda x: 'big' if x > 5.5 else 'small')
```

```{code-cell}
ax = sv.pie(iris, 'species')
```

Let's add splices labels and inner text. We are going to remove the legend too.

```{code-cell}
ax = sv.pie(iris, 'species', labels=sv.label_parameters(), text=sv.text_parameters(), legend=None)
```

Finally, to make our final plot publication ready, we can remove the labels, add the legend back and customize them further. We can also make it a donut chart instead and slightly decrease `alpha` to make the points more transparent.

```{code-cell}
ax = sv.pie(iris, 'species', donut=True, alpha=0.5, 
text=sv.text_parameters(format='%1.2f%%', size=12, color='white'), 
legend=sv.legend_parameters(title=['Species'], title_bold=True))
```

## Tips

- If labels are activated, consider hiding the legend to minimize information redundancy.
- For visualizing more than 5 categories, a {doc}`bar<bar>` plot might be a more effective choice.
- If there are numerous categories with small proportions, consider grouping them into a single category named "Others".