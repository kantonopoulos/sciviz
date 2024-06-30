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

# Boxplot

A `boxplot` is a type of graphical representation that compactly displays the distribution of a continuous variable. It visualises five summary statistics (the median, two hinges and two whiskers), and optionally all "outlying" points individually.

## Usage
```python
boxplot(data, x, y, color=None, order=None, outliers=outlier_parameters(), 
        caps=False, color_pal=None, color_order=None, fill=True, orient='v', width=0.4, 
        edgecolor='black', alpha=0.8, jitter=None, legend=legend_parameters())
```

## Arguments

- `data`: The dataset to be plotted.
- `x`, `y`: The names of the variables in `data` to be plotted on the x and y axes.
- `color`: This is an optional argument that specifies the column in the data that you want to use to color the boxes. If not specified, all boxes will be the same color.
- `order`: This is an optional argument that specifies the order in which to display the categories on the x-axis. If not specified, the categories will be displayed in the order they appear in the data.
- `outliers`: This argument specifies the parameters for the outliers. The default is the result of the `outlier_parameters` function.
- `caps`: This boolean argument, when set to True, adds caps to the ends of the whiskers. The default is False.
- `color_pal`: This is an optional argument that specifies the color palette to use for the different groups.
- `color_order`: This is an optional argument that specifies the order in which to apply the color palette. If not specified, the colors will be applied in the order they appear in the color palette.
- `fill`: This is an optional argument that specifies whether to fill the boxes. The default is True.
- `orient`: This is an optional argument that specifies the orientation of the boxes. The default is 'v' for vertical boxes. Use 'h' for horizontal boxes.
- `width`: This is an optional argument that specifies the width of the boxes. The default is 0.4.
- `edgecolor`: This is an optional argument that specifies the color of the edges of the boxes. The default is 'black'.
- `alpha`: This is an optional argument that specifies the transparency of the boxes. It should be a float between 0 (completely transparent) and 1 (completely opaque). The default value is 0.8.
- `jitter`: Parameters for the overlaying data points. This should be a `jitter_parameters` object, which has its own arguments. If not specified, no data points will be displayed.
- `legend`: Parameters for the legend. This should be a `legend_parameters` object, which has its own arguments. If not specified, a default legend is shown.

### Outliers

```python
outlier_parameters(color='black', shape='o', size=5)
```

This function allows you to customize the appearance of the outlier points.

**Arguments**:
- `color`: This argument specifies the color of the outlier points. In this case, the color is set to 'black'.
- `shape`: This argument specifies the shape of the outlier points. In this case, the shape is set to 'o', which typically represents a circle.
- `size`: This argument specifies the size of the outlier points. In this case, the size is set to 5.

### Overlaying Data Points

```python
jitter_parameters(jitter=0.1, color_pal=None, size=50, alpha=0.8, pos='front')
```

This function allows you to customize the appearance of the overlaying data points.

**Arguments**:
- `jitter`: This argument specifies the amount of jitter (random noise) to apply to the data points. The default value is 0.1.
- `color_pal`: This is a list of colors that will be used for the error bars. The default color is black.
- `size`: This argument specifies the size of the jittered points. The default size is 50.
- `alpha`: This argument specifies the transparency of the jittered points. The default is 0.8.
- `pos`: This argument specifies the position of the jittered points relative to the boxes. The default is 'front', which means the points are drawn in front of the boxes.

## Examples

Let's create a simple box plot displaying the distribution of the 'sepal_width' variable of the different species in the 'iris' dataset.
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
ax = sv.boxplot(iris, 'species', 'sepal_width')
```

If we want to further emphasize the groups we can color them.

```{code-cell}
ax = sv.boxplot(iris, 'species', 'sepal_width', color='species')
```

We can also use different `x` and `color` variables. In this example, we will showcase the option to change the color palette via the `color_pal` argument.

```{code-cell}
ax = sv.boxplot(iris, 'species', 'sepal_width', color='size', color_pal=['#FEED70', '#603479'])
```

If we want a different aesthetic, for example if we are after a black and white plot, we can set `fill` to `False` and change the `edgecolor`.

```{code-cell}
ax = sv.boxplot(iris, 'species', 'sepal_width', fill=False, edgecolor='black')
```

We can also add over- or underlaying parameters. In this example, we will overlay the data points on the box plot and make them black and more transparent. We will also remove the outlier points.

```{code-cell}
ax = sv.boxplot(iris, 'species', 'sepal_width', color='species', outliers=None,
        jitter=sv.jitter_parameters(color_pal=['black'], alpha=0.5))
```

Finally, to make our final plot publication ready, we can utilize the {doc}`theme<aesthetics>` and {doc}`legend_parameters<legend>` functions to customize the theme, axis labels, limits, ticks and legend. We will also slightly decrease `alpha` to make the boxes more transparent, increase the boxes width, remove the points and customize the outliers using the `outlier_parameters` function.

```{code-cell}
ax = sv.boxplot(iris, 'species', 'sepal_width', color='size', alpha=0.5, width=0.6,
        outliers=sv.outlier_parameters(size=3),
        legend=sv.legend_parameters(title=['Size'], title_bold=True))
ax = sv.theme(ax, theme='classic', xlab='Species', ylab='Sepal Width', 
        ylim=(1, 5), yticks=[1, 2, 3, 4, 5])
```

## Tips

- Use box plots mostly to compare distributions between different groups. If you just want to compare means or medians, consider using a {doc}`bar plot<bar>` instead.
- If different groups have different numbers of observations, consider adding overlaying data points to better visualize the distribution. Another option could be a {doc}`violin plot<violin>`.