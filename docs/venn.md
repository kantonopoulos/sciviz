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

# Venn

A Venn diagram, or `venn` in SciViz, is a type of diagram that shows all possible logical relations between a finite collection of different sets. It is usually used to display sets and subsets.

## Usage
```python
venn(data, x, group, color_pal=None, alpha=0.8, labels=label_parameters(size=14, font='Arial', color='black'))
```

## Arguments

- `data`: The dataset to be plotted.
- `x`: This is the column in the data that you want to use for the Venn diagram. The Venn diagram will show the overlap between the different groups in this column.
- `group`: This is the column in the data that you want to group by. Each unique value in this column will be a circle in the Venn diagram.
- `color_pal`: This is an optional argument that specifies the color palette to use for the different groups. If not specified, a default color palette will be used.
- `alpha`: This is an optional argument that specifies the transparency of the circles in the Venn diagram. It should be a float between 0 (completely transparent) and 1 (completely opaque). The default value is 0.8.
- `labels`: This is an optional argument that specifies the parameters for the labels of the circles in the Venn diagram. It should be a dictionary with keys for 'size', 'font', and 'color'. The default values are size 14, font 'Arial', and color 'black'.

```{note}
SciViz employs the `matplotlib_venn` library for generating Venn diagrams. Uniquely among the plots in this package, Venn diagrams do not support legends, given their infrequent use. Instead, labels are conveniently positioned adjacent to their corresponding Venn circles.
```

### Labels

```python
label_parameters(size=12, font='Arial', color='black')
```

This function allows you to customize the appearance of Venn circles labels.

**Arguments**:
- `size`: The font size of the labels. Default is 12.
- `font`: The font of the labels. Default is 'Arial'.
- `color`: The color of the labels. Default is 'black'.

## Examples

Let's construct a Venn diagram to visualize the overlap of sepal lengths across various species within the 'iris' dataset. We can also decrease the alpha value to make the circles more transparent.
```{code-cell}
:tags: ["remove-cell"]
import warnings
warnings.filterwarnings('ignore')
import seaborn as sns
import sciviz as sv
iris = sns.load_dataset('iris')
```

```{code-cell}
ax = sv.venn(iris, x='sepal_length', group='species', alpha=0.5)
```

## Tips

No more than 3 groups can be visualized in a Venn diagram. If you have more than 3 groups, consider using a different visualization method, such as a {doc}`heatmap<heatmap>`.