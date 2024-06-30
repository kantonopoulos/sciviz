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

# Line

A line plot, or `line` in SciViz, is a type of plot that displays one continuous variable (y) in order of another variable x (usually **time**). It basically connects the observations of a scatterplot. They are excellent for visualizing trends and relationships between two variables.

## Usage
```python
line(data, x, y, color=None, shape=None, stat=None, errorbar=None, 
        errorbar_style='bars', alpha=0.8, color_pal=None, shape_pal=None, 
        color_order=None, shape_order=None, legend=legend_parameters())
```

## Arguments

- `data`: The dataset to be plotted.
- `x`, `y`: The names of the variables in `data` to be plotted on the x and y axes.
- `color`: The name of the variable in data that will determine the color of the lines.
- `shape`: The name of the variable in data that will determine the shape of the points on the line.
- `stat`: The statistical transformation to use on the data for this layer. If it is a string, it must be the name of a pandas method, such as 'mean', 'max', 'min', etc. Default is 'mean'.
- `errorbar`: The name of errorbar method (either 'ci', 'pi', 'se', or 'sd'), or a tuple with a method name and a level parameter, such as ('ci', 95).
- `errorbar_style`: The style of the error bars. Can be 'bars' or 'band'.
- `alpha`: The transparency of the lines. Ranges from 0 (completely transparent) to 1 (completely opaque).
- `color_pal`, `shape_pal`: The color and shape palettes to use for the lines and points. If not specified, default palettes are used.
- `color_order`, `shape_order`: The order in which to apply the color and shape palettes. If not specified, the order in the data is used.
- `legend`: Parameters for the legend. This should be a `legend_parameters` object, which has its own arguments. If not specified, a default legend is shown.

## Examples

For this plot we are going to use a different dataset as the Iris dataset does not have a time variable. We will use the `flights` dataset from Seaborn. We have modified this dataset by introducing an additional column named 'season'. This new attribute categorizes the months into *winter* and *summer* groups. This dataset will be imported using the seaborn library and will be modified with the following commands:

```{code-cell}
import seaborn as sns
flights = sns.load_dataset("flights")
flights['season'] = flights['month'].apply(lambda x: 'winter' if x in ['Jan', 'Feb', 'Mar', 'Oct', 'Nov', 'Dec'] else 'summer')
```

Let's create a simple line plot by plotting the average number of passengers per year. 
```{code-cell}
:tags: ["remove-cell"]
import warnings
warnings.filterwarnings('ignore')
import sciviz as sv
```

```{code-cell}
ax = sv.line(flights, 'year', 'passengers')
```

Let's add another dimension by using different colors for summer and winter with `color` argument. Let's make sure that winter is plotted first with blue, while summer is plotted second with orange.

```{code-cell}
ax = sv.line(flights, 'year', 'passengers', color='season', 
        color_pal=['#2271B5', '#FF964F'], color_order=['winter', 'summer'])
```

If we want to emphasize the different seasons even more, we can add different shapes and line styles to the markers and lines respectively.

```{code-cell}
ax = sv.line(flights, 'year', 'passengers', color='season', shape='season',
        color_pal=['#2271B5', '#FF964F'], color_order=['winter', 'summer'])
```

We can also add errorbars or errorbands to our plot. Let's add errorbars displaying the 95% confidence interval.

```{code-cell}
ax = sv.line(flights, 'year', 'passengers', color='season', shape='season',
        color_pal=['#2271B5', '#FF964F'], color_order=['winter', 'summer'], errorbar=('ci', 95))
```

Finally, to make our final plot publication ready, we can utilize the {doc}`theme<aesthetics>` and {doc}`legend_parameters<legend>` functions to customize the theme, axis labels, limits, ticks and legend. We can also try to change the errorbars to errorbands.

```{code-cell}
ax = sv.line(flights, 'year', 'passengers', color='season', shape='season',
        color_pal=['#2271B5', '#FF964F'], color_order=['winter', 'summer'], errorbar=('ci', 95), 
        errorbar_style='band', legend=sv.legend_parameters(title=['Season'], title_bold=True))
ax = sv.theme(ax, theme='classic', xlab='Time (years)', ylab='Number of Passengers', ylim=(0, 600))
```

## Tips

- When one of your variables is time, line plot is usually the way too go.
- Keep the ordered variable (time) in x axis as it is easier to read.
- Try to start axis from 0 to avoid misleading visualizations. However, if starting from 0 makes the plot hard to read, consider starting from the minimum value of the data.
- If none of your variables is ordered consider using a {doc}`scatterplot<points>` instead.