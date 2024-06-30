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

# Heatmap

A `heatmap` is a graphical representation of data where the individual values contained in a matrix are represented as colors. Heatmaps are particularly useful for visualizing complex data sets, such as those with multiple variables or large numbers of observations. They are commonly used when multiple variables are involved in the analysis, and the relationships between them need to be visualized.

## Usage
```python
heatmap(data, gradient_pal='Spectral', row_cluster=True, col_cluster=True, dendrogram=0.1, 
          row1_annot=None, row2_annot=None, col1_annot=None, col2_annot=None, row1_pal=None, 
          row2_pal=None, col1_pal=None, col2_pal=None, cbar=True, ticks=tick_parameters(), 
          legend=legend_parameters())
```

## Arguments

- `data`: The dataset to be visualized as a heatmap. It should be a 2D array-like structure (like a DataFrame).
- `gradient_pal`: The color palette selected for the heatmap gradient significantly influences the visual interpretation of the data. The 'Spectral' palette, a diverging color scheme, is particularly recommended for data ranging from 0 to a positive value. For data spanning -value to +value, the "coolwarm" palette is more suitable due to its ability to distinctly represent both negative (blue) and positive values (red), while zero values remain white.
- `row_cluster` and `col_cluster`: If set to True, hierarchical clustering is performed on the rows and columns respectively, and the heatmap is reordered to reflect this clustering.
- `dendrogram`: The size of the dendrogram to be displayed alongside the heatmap. If set to 0, no dendrogram is displayed.
- `row1_annot`, `row2_annot`, `col1_annot`, `col2_annot`: These are additional annotations for the rows and columns. They should be array-like structures of the same length as the number of rows/columns.
- `row1_pal`, `row2_pal`, `col1_pal`, `col2_pal`: These are color palettes for the row and column annotations. If not provided, default colors are used.
- `cbar`: If set to True, a colorbar is displayed alongside the heatmap.
- `ticks`: Parameters for the heatmap ticks. This should be a `tick_parameters` object, which has its own arguments. If not specified, default ticks will be displayed.
- `legend`: Parameters for the legend. This should be a `legend_parameters` object, which has its own arguments. If not specified, a default legend is shown.

### Ticks

```python
tick_parameters(xticks=True, yticks=True, xticks_angle=0, yticks_angle=0, ticklabel_size=11)
```

This function allows you to customize the appearance of the box plots.

**Arguments**:
- `xticks` and `yticks`: If set to True, x and y tick marks are displayed.
- `xticks_angle` and `yticks_angle`: The angle at which to display the x and y tick labels.
- `ticklabel_size`: The font size of the tick labels.

## Examples

Let's create a simple clustered heatmap displaying the values of all variables in all observations in the 'iris' dataset.
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
ax = sv.heatmap(iris)
```

If we do not want to cluster them, we have to turn the `row_cluster` and `col_cluster` arguments to `None`.

```{code-cell}
ax = sv.heatmap(iris, row_cluster=None, col_cluster=None)
```

We have the option to exclusively cluster the samples, leaving the variables unclustered. Simultaneously, we can enhance the visibility of distinct clusters by enlarging the dendrogram and deactivate the colorbar.

```{code-cell}
ax = sv.heatmap(iris, row_cluster=True, col_cluster=None, dendrogram=0.3, cbar=None)
```

We could also incorporate annotations for both rows and columns. Specifically, we'll annotate rows with the 'species' variable and columns based on whether the variable pertains to 'petal' or 'sepal'. We'll change the palette for the column annotation, so that it does not clash with the row annotation palette.

```{code-cell}
col_annot1 = [{'sepal_length': 'sepal', 'petal_width': 'petal', 'petal_length': 'petal', 
                'sepal_width': 'sepal'}, 'Flower\'s Part']
ax = sv.heatmap(iris, row_cluster=True, col_cluster=None, dendrogram=0.1, row1_annot='species', 
                  col1_annot=col_annot1, col1_pal=['#FFFF80', '#603479'])
```

```{note}
To create the column annotation, a dictionary is used to map the variable names to the corresponding part of the flower. The dictionary is then passed as an argument to the `col1_annot` parameter.
```

Finally, to make our final plot publication ready, we can utilize the `tick_parameters` and {doc}`legend_parameters<legend>` functions to customize the ticks and legend. 

```{code-cell}
col_annot1 = [{'sepal_length': 'sepal', 'petal_width': 'petal', 'petal_length': 'petal', 
                'sepal_width': 'sepal'}, 'Flower\'s Part']
ax = sv.heatmap(iris, row_cluster=True, col_cluster=None, dendrogram=0.1, row1_annot='species', 
                  col1_annot=col_annot1, col1_pal=['#FFFF80', '#603479'],
                  ticks=sv.tick_parameters(xticks=True, yticks=None, ticklabel_size=12),
                  legend=sv.legend_parameters(orient='h', posx=0, posy=-0.6, 
                      title=['Species', 'Flower\'s Part'], title_bold=True))
```

## Tips

- Heatmaps are particularly useful for visualizing complex data sets, such as those with multiple variables or large numbers of observations.
- You can add more layers of information to your heatmap by incorporating annotations for both rows and columns. Do not forget to adjust the color palette for the annotations to ensure they are visually distinct.
- If clustering makes no sense for your data, you can turn off the row and column clustering by setting the `row_cluster` and `col_cluster` arguments to `None`.
- If you just want to compare the values of one or two variables in different categories, consider also using a {doc}`bar plot<bar>`.