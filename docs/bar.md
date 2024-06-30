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

# Bar

A bar plot, or `bar` in SciViz, is a type of graphical representation that uses bars to display proportions. The height of the bars can represent various statistical properties such as the number of observations, their mean, etc. Bar plots are particularly effective for visualizing the proportions across multiple categories.

## Usage
```python
bar(data, x, y, color=None, order=None, stat='mean', color_pal=None, color_order=None, 
      fill=True, orient='v', width=0.4, edgecolor='black', alpha=0.8, errorbar=None, 
      legend=legend_parameters())
```

## Arguments

- `data`: The dataset to be plotted.
- `x`, `y`: The names of the variables in `data` to be plotted on the x and y axes.
- `color`: This is an optional argument that specifies the column in the data that you want to use to color the bars. If not specified, all bars will be the same color.
- `order`: This is an optional argument that specifies the order in which to display the categories on the x-axis. If not specified, the categories will be displayed in the order they appear in the data.
- `stat`: This is an optional argument that specifies the statistic to compute when y not is specified. The default is 'mean'.
- `color_pal`: This is an optional argument that specifies the color palette to use for the different groups.
- `color_order`: This is an optional argument that specifies the order in which to apply the color palette. If not specified, the colors will be applied in the order they appear in the color palette.
- `fill`: This is an optional argument that specifies whether to fill the bars. The default is True.
- `orient`: This is an optional argument that specifies the orientation of the bars. The default is 'v' for vertical bars. Use 'h' for horizontal bars.
- `width`: This is an optional argument that specifies the width of the bars. The default is 0.4.
- `edgecolor`: This is an optional argument that specifies the color of the edges of the bars. The default is 'black'.
- `alpha`: This is an optional argument that specifies the transparency of the bars. It should be a float between 0 (completely transparent) and 1 (completely opaque). The default value is 0.8.
- `errorbar`: Parameters for the error bars. This should be a `errorbar_parameters` object, which has its own arguments. If not specified, no error bars will be displayed.
- `legend`: Parameters for the legend. This should be a `legend_parameters` object, which has its own arguments. If not specified, a default legend is shown.

### Error Bars

```python
error_parameters(errorbar=('ci', 95), color_pal=['black'], linestyle='-', linewidth=1, capsize=0.2)
```

This function allows you to customize the appearance of the error bars.

**Arguments**:
- `errorbar`: The name of errorbar method (either 'ci', 'pi', 'se', or 'sd'), or a tuple with a method name and a level parameter, such as ('ci', 95).
- `color_pal`: This is a list of colors that will be used for the error bars. The default color is black.
- `linestyle`: This is a string that specifies the style of the line for the error bars. The default style is a solid line ('-').
- `linewidth`: This is a number that specifies the width of the line for the error bars. The default width is 1.
- `capsize`: This is a number that specifies the size of the caps on the error bars. The default size is 0.2.

## Examples

Let's create a simple bar plot displaying the mean of the 'sepal_width' variable of the different species in the 'iris' dataset.
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
ax = sv.bar(iris, 'species', 'sepal_width')
```

If we want to further emphasize the groups we can color them.

```{code-cell}
ax = sv.bar(iris, 'species', 'sepal_width', color='species')
```

We can also use different `x` and `color` variables. In this example, we will showcase the option to change the color palette via the `color_pal` argument.

```{code-cell}
ax = sv.bar(iris, 'species', 'sepal_width', color='size', color_pal=['#FEED70', '#603479'])
```

Instead of their mean, we can count the observations in each category by setting `stat` to 'count'.

```{note}
In this case, it does not matter what we set the `y` variable to, as it will just count the observations. It can be any numerical column in the dataset.
```

```{code-cell}
ax = sv.bar(iris, 'species', 'sepal_width', color='size', color_pal=['#FEED70', '#603479'], stat='count')
```

If we want a different aesthetic, for example if we are after a black and white plot, we can set `fill` to `False` and change the `edgecolor`.

```{code-cell}
ax = sv.bar(iris, 'species', 'sepal_width', stat='mean', fill=False, edgecolor='black')
```

We can also add error bars, using the `errorbar` argument and the `errorbar_parameters` function. We will also remove the legend for this example.

```{code-cell}
ax = sv.bar(iris, 'species', 'sepal_width', color='species', stat='mean', legend=None,
        errorbar=sv.error_parameters())
```

Finally, to make our final plot publication ready, we can utilize the {doc}`theme<aesthetics>` and {doc}`legend_parameters<legend>` functions to customize the theme, axis labels, limits, ticks and legend. We will also slightly decrease `alpha` to make the bars more transparent, customize the errorbars using the `errorbar_parameters` function and change the width of the bars.

```{code-cell}
ax = sv.bar(iris, 'species', 'sepal_width', color='size', alpha=0.5, width=0.6,
        errorbar=sv.error_parameters(errorbar=('sd', 2), color_pal=['black'], capsize=0.1), 
        legend=sv.legend_parameters(title=['Size'], title_bold=True))
ax = sv.theme(ax, theme='classic', xlab='Species', ylab='Sepal Width Mean', 
        ylim=(0, 6), yticks=[0, 1, 2, 3, 4, 5, 6])
```

## Tips

- Barplots are usually easier to understand than pie charts.
- If you are going to use errorbars be sure to know what they represent and how to interpret them. Also, consider mention them in the figure legend in your report.
- When displaying multiple groups in a plot, it's advisable to highlight the group you want the viewer to focus on by using a distinct color, while maintaining the rest in grey. This approach enhances the interpretability of the plot.