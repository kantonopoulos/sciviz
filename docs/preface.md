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

# SciViz - Preface

Welcome to **SciViz**! It is a visualization package that's all about getting you from data to insights, fast and efficiently. Built on the solid foundations of matplotlib and seaborn, SciViz offers a simplified interface for creating clean, beautiful plots with ease.

Our aim with SciViz? To make your life easier. We've set up smart defaults so you can create stunning visuals without the hassle. Perfect for students, researchers, and data analysts who need to create impressive visuals quickly for their reports and presentations.

Inspired by R's ggplot2, we've incorporated some of its grammar of graphics into our package. This means you can create meaningful visualizations with minimal code, and go from this:

```{code-cell}
:tags: ["remove-cell"]
import warnings
warnings.filterwarnings('ignore')
import seaborn as sns
iris = sns.load_dataset('iris')
```
```{code-cell}
import matplotlib.pyplot as plt
import seaborn as sns

fig, ax = plt.subplots(figsize=(6, 6))
ax = sns.violinplot(data=iris, x='species', y='sepal_width', hue='species', ax=ax)
plt.xlabel('Species', fontsize=12)
plt.ylabel('Sepal Width', fontsize=12)
plt.show()
```

To this:

```{code-cell}
import sciviz as sv

ax = sv.violin(iris, 'species', 'sepal_width', color='species', alpha=0.5, box=sv.box_parameters(), legend=None)
ax = sv.theme(ax, xlab='Species', ylab='Sepal Width')
```

But let's be clear - SciViz is not for those seeking highly complex visualizations or extreme customization. We've prioritized simplicity and ease of use over flexibility. But for most of your plotting needs, SciViz is ready to deliver.

Ready to get started? Let's dive into the world of SciViz and make your data shine!