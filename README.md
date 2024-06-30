# SciViz: Simplifying Plot Creation <img src="docs/logo.png" align="right" height="200" alt="" />

**SciViz** is a Python package designed to simplify the creation of statistical data analysis plots, optimized specifically for the needs of students and researchers. With SciViz, you can effortlessly generate aesthetically pleasing plots for your data visualization tasks using single function calls.

```{python}
import sciviz as sv

ax = sv.violin(iris, 'species', 'sepal_width', color='species', alpha=0.5, box=sv.box_parameters(), legend=None)
ax = sv.theme(ax, xlab='Species', ylab='Sepal Width')
```

<img src="docs/violin_plot.png" alt="" />

## Features

- **Simplicity**: Easy-to-use interface for creating aesthetics plots with minimal effort.
- **Flexibility**: Customizable plots with seaborn/matplotlib axis objects for further manipulation.

## Installation

You can install SciViz via pip:
```
pip install sciviz
```

## Documentation

For more in-depth documentation, including detailed usage examples refer to the [package vignette](https://sciviz.readthedocs.io/en/latest/preface.html).

## Contributing

Contributions are welcome! Please fork your contribution or reach out to discuss new ideas.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
