# Working with SciViz

This chapter serves as an introduction to the dataset and tools used in the book, as well as providing guidance on maximizing the potential of SciViz. It sets the stage for the upcoming example cases for the plots.

## Dataset

The primary dataset used throughout this book is the well-known [Iris dataset](https://en.wikipedia.org/wiki/Iris_flower_data_set). We have modified this dataset by introducing an additional column named 'size'. This new attribute categorizes the Iris flowers into *big* and *small* groups, determined by their 'sepal_length' values. This dataset will be imported using the seaborn library and will be modified with the following commands:

```python
import seaborn as sns
iris = sns.load_dataset('iris')
iris['size'] = iris['sepal_length'].apply(lambda x: 'big' if x > 5.5 else 'small')
```

For the sake of brevity, this commands will not be repeated in every example.

## Tools & Compatibility

All plots generated in this book are matplotlib objects, making them compatible with numerous matplotlib functions.

```{note}
While using SciViz does not require knowledge of any other Python visualization package, familiarity with matplotlib can provide additional flexibility not directly available through the SciViz interface.
```

SciViz is optimized to work with pandas DataFrames. Therefore, having some experience with pandas will allow you to leverage the full potential of SciViz.