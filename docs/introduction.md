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

# Introduction

**SciViz** is a data visualization package designed to transform your data into meaningful insights. In this chapter, we will guide you through the installation process, introduce you to its key features, and delve into its minimalistic grammar of graphics.

## Installation

Installing SciViz is as simple as running a single command in your terminal. If you have Python installed on your system, you can install SciViz using pip.

```bash
pip install sciviz
```

This command will download and install SciViz and its dependencies. Once the installation is complete, you can import SciViz in your Python scripts and start using it to create stunning visualizations.

```{code-cell}
import sciviz as sv
```

## Grammar of Graphics

The design philosophy of **SciViz** is rooted in simplicity and minimalism. Creating a plot involves two main steps: selecting the plot type and customizing its aesthetics.

### Selecting the Plot

In SciViz, you choose the type of plot you want to create and provide the necessary arguments. The arguments typically include the data, the variables to be plotted, and other parameters specific to each plot type. The available plot types are:

- {doc}`Points<points>`
- {doc}`Line<line>`
- {doc}`Pie<pie>`
- {doc}`Histogram<histogram>`
- {doc}`Bar<bar>`
- {doc}`Boxplot<boxplot>`
- {doc}`Jitter<jitter>`
- {doc}`Violin<violin>`
- {doc}`Venn<venn>`
- {doc}`Heatmap<heatmap>`


`````{admonition} Tip
:class: tip
To explore the arguments of any function without leaving your notebook, you can utilize Python's built-in `help()` function. For instance, to understand the parameters of the point function in SciViz, you would use `help(sv.point)`.
`````

The arguments of each plot are presented in detail with examples in the following sections. However, here's an example of how to create the violin plot that we presented in the preface of this guide:

```python
sv.violin(data=iris, x='species', y='sepal_width', color='species', alpha=0.5, box=sv.box_parameters(), legend=None)
```

The arguments for the plot are intuitive: `data` is the dataset, `x` and `y` are the variables to plot, `color` determines the color of the violins, `alpha` sets their transparency, `box` adds boxplots inside the violins, and `legend` hides the legend as it's not needed in this case.

```{note}
Some plot parameters require functions as input, such as `box_parameters`. These functions are provided by SciViz to simplify customization. Detailed explanations and examples of these functions will be provided in the respective sections for each plot type. Additionally, {doc}`legend_parameters<legend>` will have its own dedicated section as it can be used in most of the plots.
```

### Customizing Aesthetics

Once you've selected your plot, you can customize its aesthetics using the {doc}`theme<aesthetics>` function. This function allows you to modify various aspects of your plot, including the axis lengths, labels, ticks, and more. Here's an example:

```python
ax = sv.theme(ax, xlab='Species', ylab='Sepal Width')
```

In this way, SciViz allows you to create beautiful and meaningful visualizations with just a few lines of code. Its minimalistic grammar of graphics makes it easy to learn and use, while still offering a high degree of customization.

Check the subsequent chapters to learn more about the available plot types and how to use them effectively in your data analysis workflow.