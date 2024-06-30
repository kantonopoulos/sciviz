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

# Theme

The `theme` function allows you to customize the appearance of your plot. You can change the seaborn 'theme', the the axis labels and limits, the axis ticks, and the plot title.

## Usage
```python
theme(ax, theme='ticks', title=None, xlab=None, ylab=None, xlim=None, ylim=None, xticks=None, 
      yticks=None, xticks_angle=0, yticks_angle=0, title_size=14, axislabel_size=12, 
      ticklabel_size=11)
```

## Arguments

- `ax`: This is likely the Axes object on which to apply the theme. This object represents a single plot.
- `theme`: This argument likely specifies the overall theme to apply to the plot. The value 'ticks' might refer to a specific predefined theme.
- `title`: This argument likely specifies the title of the plot. None means no title will be set.
- `xlab`, `ylab`: These arguments likely specify the labels for the x-axis and y-axis, respectively. None means no labels will be set.
- `xlim`, `ylim`: These arguments likely specify the limits for the x-axis and y-axis, respectively. None means the limits will be determined automatically.
- `xticks`, `yticks`: These arguments likely specify the tick locations on the x-axis and y-axis, respectively. None means the tick locations will be determined automatically.
- `xticks_angle`, `yticks_angle`: These arguments likely specify the rotation angles for the x-axis and y-axis tick labels, respectively. The values are in degrees.
- `title_size`, `axislabel_size`, `ticklabel_size`: These arguments likely specify the font sizes for the title, axis labels, and tick labels, respectively. The values are in points.

`````{admonition} Tip
:class: tip
For publication-ready plots, you can use either 'ticks' or 'classic' as `theme`.
`````
