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

# Violin

A violin plot, or `violin` in SciViz, is a graphical tool that efficiently illustrates the distribution of a continuous variable. It mirrors a density plot, similar in presentation to a box plot, and can optionally be paired with a box plot for enhanced data interpretation.

## Usage
```python
violin(data, x, y, color=None, order=None, color_pal=None, color_order=None, fill=True, split=False, orient='v', width=0.4, edgecolor='black', alpha=0.8, box=None, legend=legend_parameters())
```

## Arguments

- `data`: The dataset to be plotted.
- `x`, `y`: The names of the variables in `data` to be plotted on the x and y axes.
- `color`: This is an optional argument that specifies the column in the data that you want to use to color the violins. If not specified, all violins will be the same color.
- `order`: This is an optional argument that specifies the order in which to display the categories on the x-axis. If not specified, the categories will be displayed in the order they appear in the data.
- `color_pal`: This is an optional argument that specifies the color palette to use for the different groups.
- `color_order`: This is an optional argument that specifies the order in which to apply the color palette. If not specified, the colors will be applied in the order they appear in the color palette.
- `fill`: This is an optional argument that specifies whether to fill the violins. The default is True.
- `split`: This boolean argument, when set to True, splits the violin plot in half along the y-axis for better comparison of two categories. The default is False.
- `orient`: This is an optional argument that specifies the orientation of the violins. The default is 'v' for vertical violins. Use 'h' for horizontal violins.
- `width`: This is an optional argument that specifies the width of the violins. The default is 0.4.
- `edgecolor`: This is an optional argument that specifies the color of the edges of the violins. The default is 'black'.
- `alpha`: This is an optional argument that specifies the transparency of the violins. It should be a float between 0 (completely transparent) and 1 (completely opaque). The default value is 0.8.
- `box`: Parameters for the overlaying box plots. This should be a `box_parameters` object, which has its own arguments. If not specified, no box plots will be displayed.
- `legend`: Parameters for the legend. This should be a `legend_parameters` object, which has its own arguments. If not specified, a default legend is shown.

### Box Plots

```python
box_parameters(fill_color='white', edge_color='black', edge_width=1, median_color='black', 
                median_width=1.5, outliers=True, outlier_color='black', outlier_shape='o', 
                outlier_size=2)
```

This function allows you to customize the appearance of the box plots.

**Arguments**:
- `fill_color`: Sets the fill color of the box in the box plot to white.
- `edge_color`: Sets the color of the box's edges to black.
- `edge_width`: Sets the width of the box's edges to 1.
- `median_color`: Sets the color of the median line in the box plot to black.
- `median_width`: Sets the width of the median line to 1.5.
- `outliers`: Indicates that outliers should be included in the box plot.
- `outlier_color`: Sets the color of the outlier points to black.
- `outlier_shape`: Sets the shape of the outlier points to 'o' (likely meaning circles).
- `outlier_size`: Sets the size of the outlier points to 2.

## Examples

Let's create a simple violin plot displaying the distribution of the 'sepal_width' variable of the different species in the 'iris' dataset.
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
ax = sv.violin(iris, 'species', 'sepal_width')
```

If we want to further emphasize the groups we can color them.

```{code-cell}
ax = sv.violin(iris, 'species', 'sepal_width', color='species')
```

We can also use different `x` and `color` variables. In this example, we will showcase the option to change the color palette via the `color_pal` argument.

```{code-cell}
ax = sv.violin(iris, 'species', 'sepal_width', color='size', color_pal=['#FEED70', '#603479'])
```

If we want to make the whole plot more compact we can split the violins in half and combine the two groups.

```{code-cell}
ax = sv.violin(iris, 'species', 'sepal_width', color='size', color_pal=['#FEED70', '#603479'], 
                split=True)
```

```{note}
This can be done only in cases where the `color` variable has two categories.
```

If we want a different aesthetic, for example if we are after a black and white plot, we can set `fill` to `False` and change the `edgecolor`.

```{code-cell}
ax = sv.violin(iris, 'species', 'sepal_width', fill=False, edgecolor='black')
```

We can also combine it with a box plot. We will remove the legend as well.

```{code-cell}
ax = sv.violin(iris, 'species', 'sepal_width', color='species', legend=None, box=sv.box_parameters())
```

Finally, to make our final plot publication ready, we can utilize the {doc}`theme<aesthetics>` and {doc}`legend_parameters<legend>` functions to customize the theme, axis labels, limits, ticks and legend. We will also slightly decrease `alpha` to make the violins more transparent, increase the violins width and customize the boxes using the `box_parameters` function.

```{code-cell}
ax = sv.violin(iris, 'species', 'sepal_width', color='size', alpha=0.5, width=0.8,
        box=sv.box_parameters(median_color='red', outliers=False),
        legend=sv.legend_parameters(title=['Size'], title_bold=True))
ax = sv.theme(ax, theme='classic', xlab='Species', ylab='Sepal Width', 
        ylim=(1, 5), yticks=[1, 2, 3, 4, 5])
```

## Tips

- Violins provide more information than a box plot, but can be harder to interpret. If you do not need the actual distributions, a {doc}`box plot<boxplot>` might be more appropriate.