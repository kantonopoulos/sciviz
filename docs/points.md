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

# Points

A scatter plot, or `point` in SciViz, is a type of plot that displays the relationship between two continuous variables. It uses dots to represent the values obtained for each observation in the dataset. They are excellent for visualizing correlations between variables and identifying trends, clusters, or outliers.

## Usage
```python
point(data, x, y, color=None, shape=None, size=50, alpha=0.8, color_pal=None, 
        shape_pal=None, size_pal=[50, 150], color_order=None, shape_order=None, 
        size_order=None, legend=legend_parameters())
```

## Arguments

- `data`: The dataset to be plotted.
- `x`, `y`: The names of the variables in `data` to be plotted on the x and y axes.
- `color`: The name of the variable in `data` that will determine the color of the points.
- `shape`: The name of the variable in `data` that will determine the shape of the points.
- `size`: The size of the points. Can be a single value or a variable in `data`.
- `alpha`: The transparency of the points. Ranges from 0 (completely transparent) to 1 (completely opaque).
- `color_pal`, `shape_pal`, `size_pal`: The color, shape, and size palettes to use for the points. If not specified, default palettes are used.
- `color_order`, `shape_order`, `size_order`: The order in which to apply the color, shape, and size palettes. If not specified, the order in the data is used.
- `legend`: Parameters for the legend. This should be a `legend_parameters` object, which has its own arguments. If not specified, a default legend is shown.

## Examples

Let's create a simple scatter plot using the Iris dataset. We'll plot the sepal length against the sepal width, coloring the points by species.
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
ax = sv.point(iris, 'sepal_width', 'sepal_length')
```

Let's add some color to the points based on their 'species'.

```{code-cell}
ax = sv.point(iris, 'sepal_width', 'sepal_length', color='species')
```

If we want to print this plot in black and white, we can use different shapes for each species and make points black.

```{note}
Do not forget that in SciViz, both single colors and color palettes are defined as lists by the `color_pal` argument. If you want to use a single color, you can pass it as a list with a single element.
```

```{code-cell}
ax = sv.point(iris, 'sepal_width', 'sepal_length', shape='species', color_pal=['black'])
```

We can also add another layer of information by using the size of the points. Let's use `size` for this. We can also specify the `size_order` so that the *big* flowers are displayed with bigger points.

```{code-cell}
ax = sv.point(iris, 'sepal_width', 'sepal_length', color='species', 
        size='size', size_order=['small', 'big'])
```

Finally, to make our final plot publication ready, we can utilize the {doc}`theme<aesthetics>` and {doc}`legend_parameters<legend>` functions to customize the theme, axis labels, limits, ticks and legend. We will also slightly decrease `alpha` to make the points more transparent.

```{note}
The `theme` and `legend_parameters` functions are going to be presented in more detail in the following sections.
```

```{code-cell}
ax = sv.point(iris, 'sepal_width', 'sepal_length', color='species', 
        size='size', size_order=['small', 'big'], alpha=0.6, 
        legend=sv.legend_parameters(title=['Species', 'Size'], title_bold=True))
ax = sv.theme(ax, theme='classic', xlab='Sepal Width', ylab='Sepal Length', 
        xlim=(1, 5), ylim=(4, 8), xticks=[1, 2, 3, 4, 5], yticks=[4, 5, 6, 7, 8])
```

## Tips

- Use color, shape and size meaningfully to visualize more dimensions and display more information. For example, use big points to represent big flowers and not the other way arround. This will make the plot more intuitive and easier to interpret.
- Be careful not to overdo it and make it too complex. A scatter plot is meant to be simple and easy to interpret. Avoid adding too many variables or elements that could clutter the plot.
- A typical problem in scatter plots is overplotting (having too many points). Avoid it by using transparency (`alpha`) to make the points more distinguishable. If you still have a lot of points, consider using a {doc}`2D density plot<histogram>` or a seaborn [hexbin plot](https://seaborn.pydata.org/examples/hexbin_marginals.html) instead of a scatter plot. These are better at handling large datasets and can show the distribution of points more clearly.
- Keep the axis lengths equal to avoid distorting the data. This is especially important when the variables have different units or scales. You can use the `theme` function to set the axis limits accordingly.
- If you have one categorical and one continuous variable, consider using a {doc}`boxplot<boxplot>` or a {doc}`violin plot<violin>` instead of a scatter plot. These plots are better at showing the distribution of the continuous variable within each category.