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

# Jitter

A jitter plot, or `jitter` in SciViz, is a type of graphical representation that uses jittered points to display the distribution of data points. Jitter plots are particularly effective for visualizing the spread and density of data points across multiple categories. One axis represents the categories, while the other represents the values of the data points.

## Usage
```python
jitter(data, x, y, color=None, order=None, jitter=True, dodge=False, size=50, color_pal=None, 
      color_order=None, orient='v', alpha=0.8, crossbar=None, legend=legend_parameters())
```

## Arguments

- `data`: The dataset to be plotted.
- `x`, `y`: The names of the variables in `data` to be plotted on the x and y axes.
- `color`: This is an optional argument that specifies the column in the data that you want to use to color the points. If not specified, all points will be the same color.
- `order`: This is an optional argument that specifies the order in which to display the categories on the x-axis. If not specified, the categories will be displayed in the order they appear in the data.
- `jitter`: This boolean argument, when set to True, adds a small amount of random noise to the bar positions to make them easier to distinguish. The default is True. If it is a number (from 0 to 1), it specifies the amount of jitter to apply.
- `dodge`: This boolean argument, when set to True, separates the points for different categories based on the `color` variable. The default is False.
- `size`: This argument specifies the size of the points. The default size is 50.
- `color_pal`: This is an optional argument that specifies the color palette to use for the different groups.
- `color_order`: This is an optional argument that specifies the order in which to apply the color palette. If not specified, the colors will be applied in the order they appear in the color palette.
- `orient`: This is an optional argument that specifies the orientation of the points. The default is 'v' for vertical points. Use 'h' for horizontal points.
- `alpha`: This is an optional argument that specifies the transparency of the points. It should be a float between 0 (completely transparent) and 1 (completely opaque). The default value is 0.8.
- `crossbar`: Parameters for the cross bars. This should be a `crossbar_parameters` object, which has its own arguments. If not specified, no cross bars will be displayed.
- `legend`: Parameters for the legend. This should be a `legend_parameters` object, which has its own arguments. If not specified, a default legend is shown.

### Cross Bars

```python
crossbar_parameters(color_val=None, color_pal=['black'], barstyle='_', barsize=20, barwidth=3)
```

This function allows you to customize the appearance of the cross bars.

**Arguments**:
- `color_val`: This optional argument specifies the color value for the cross bars. If not provided, the color is determined by the `color_pal` argument.
- `color_pal`: This is a list of colors that will be used for the cross bars. The default color is black.
- `barstyle`: This argument specifies the style of the cross bars. The default style is underscore ('_').
- `barsize`: This argument specifies the size of the cross bars. The default size is 20.
- `barwidth`: This argument specifies the width of the cross bars. The default width is 3.

## Examples

Let's create a simple jitter plot displaying the mean of the 'sepal_width' variable of the different species in the 'iris' dataset.
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
ax = sv.jitter(iris, 'species', 'sepal_width')
```

If we want to further emphasize the groups we can color them.

```{code-cell}
ax = sv.jitter(iris, 'species', 'sepal_width', color='species')
```

We can also use different `x` and `color` variables. In this example, we will showcase the option to change the color palette via the `color_pal` argument.

```{code-cell}
ax = sv.jitter(iris, 'species', 'sepal_width', color='size', color_pal=['#FEED70', '#603479'])
```

We can also add cross bars, using the `crossbar` argument and the `crossbar_parameters` function. We will also remove the legend for this example.

```{code-cell}
ax = sv.jitter(iris, 'species', 'sepal_width', color='species', legend=None,
        crossbar=sv.crossbar_parameters())
```

Finally, to make our final plot publication ready, we can utilize the {doc}`theme<aesthetics>` and {doc}`legend_parameters<legend>` functions to customize the theme, axis labels, limits, ticks and legend. We will also decrease `alpha` to make the points more transparent, customize the cross bars and orient the plot horizontally.

```{code-cell}
ax = sv.jitter(iris, 'sepal_width', 'species', color='size', alpha=0.4, orient='h',
        crossbar=sv.crossbar_parameters(color_val='species', barstyle='|'), 
        legend=sv.legend_parameters(title=['Size'], title_bold=True))
ax = sv.theme(ax, theme='classic', xlab='Sepal Width Mean', ylab=None, 
        xlim=(1, 5), xticks=[1, 2, 3, 4, 5])
```

## Tips

- Jitter plots effectively illustrate the distribution of data points across various categories.
- Avoid using multiple color variables within the same x category to maintain clarity and ease of interpretation in your plot.