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

# Legend

The `legend_parameters` function allows you to customize the legend of your plot. You can change the orientation, the position, the title, the font size, and the font color of the legend. 

## Usage
```python
legend_parameters(orient='v', posx=1, posy=0.5, title=True, title_size=12, title_bold=False, label_size=11)
```

## Arguments

- `orient`: This argument specifies the orientation of the legend. 'v' likely stands for vertical, meaning the legend items will be stacked vertically.
- `posx`: This argument specifies the x-position of the legend on the plot. The value of 1 likely places the legend at the far right of the plot.
- `posy`: This argument specifies the y-position of the legend on the plot. The value of 0.5 likely places the legend in the middle of the plot vertically.
- `title`: This argument specifies whether the legend should have a title. True means a title will be included.
- `title_size`: This argument specifies the font size of the legend's title. The value of 12 likely represents the font size in points.
- `title_bold`: This argument specifies whether the legend's title should be bold. False means the title will not be bold.
- `label_size`: This argument specifies the font size of the legend's labels. The value of 11 likely represents the font size in points.

```{note}
If you change the orientation of the legend don't forget to adjust the position as well.
```