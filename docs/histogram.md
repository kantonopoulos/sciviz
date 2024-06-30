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

# Histogram

A `histogram` is a graphical representation that organizes a group of data points and is ideal for displaying distributions. It takes one or two variables by dividing the x (and optionally y) axis into bins and then calculates a statistic, such as the count of observations per bin. These statistics are visually represented using bars.

## Usage
```python
histogram(data, x, y=None, color=None, stat='count', bins='auto', binwidth=None, color_pal=None, 
            color_order=None, edgecolor='black', alpha=0.8, legend=legend_parameters())
```

## Arguments

- `data`: The dataset to be used for creating the histogram.
- `x`: The data for the x-axis.
- `y`: Optional. The data for the y-axis. If not provided, the histogram will be 1-dimensional.
- `color`: Optional. The variable in the data to be used for color encoding.
- `stat`: Optional. The statistic to compute for each bin. Default is 'count'.
- `bins`: Optional. The method for calculating the number of bins. Default is 'auto', which will determine the number of bins automatically.
- `binwidth`: Optional. The width of the bins. If not provided, it will be determined automatically.
- `color_pal`: Optional. The color palette to be used for color encoding.
- `color_order`: Optional. The order of colors for the color encoding.
- `edgecolor`: Optional. The color of the edge of the bars. Default is 'black'.
- `alpha`: Optional. The transparency of the bars. Default is 0.8.
- `legend`: Parameters for the legend. This should be a `legend_parameters` object, which has its own arguments. If not specified, a default legend is shown.

`````{admonition} Tip
:class: tip
Use either the `bins` or the `binwidth` argument.
`````

## Examples

Let's create a simple histogram displaying the distribution of the 'sepal_length' variable in the 'iris' dataset.
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
ax = sv.histogram(iris, 'sepal_length')
```

Let's separate the flowers of different size by using the `color` argument. We can also increase the number of bins.

```{code-cell}
ax = sv.histogram(iris, 'sepal_length', color='size', bins=20)
```

We can do 2D histograms as well. But they are not commonly used and can be misleading. Let's create a 2D histogram displaying the relationship between 'sepal_width' and 'sepal_length'. Let's also showcase the use of `binwidth` instead of `bins` this time, as well as remove the edge color.

```{code-cell}
ax = sv.histogram(iris, 'sepal_width', 'sepal_length', binwidth=0.1, edgecolor=None)
```

`````{admonition} Tip
:class: tip
When employing plots, such as scatterplots with a large number of points and 2D histograms, it's recommended to avoid from using color as it can add unnecessary complexity.
`````

Finally, to make our final plot publication ready, we can utilize the {doc}`theme<aesthetics>` and {doc}`legend_parameters<legend>` functions to customize the theme, axis labels, limits, ticks and legend. We will also slightly decrease `alpha` to make the points more transparent.

```{code-cell}
ax = sv.histogram(iris, 'sepal_length', color='size', bins=20, alpha=0.6,
        legend=sv.legend_parameters(title=['Size'], title_bold=True))
ax = sv.theme(ax, theme='classic', xlab='Sepal Length', ylab='Count', 
        xlim=(4, 8), xticks=[4, 5, 6, 7, 8])
```

## Tips

- Excessive use of colors can lead to a cluttered and confusing plot. For comparing multiple groups (more than 2), it's advisable to create separate plots with consistent bin counts and axis limits to ensure comparability.