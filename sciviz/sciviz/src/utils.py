from itertools import chain, combinations
from matplotlib.colors import to_rgba


def format_string(input_string):
    """Format a string by replacing underscores with spaces and capitalizing the first letter of each word.

    Args:
        input_string (string): The string to format.

    Returns:
        string: The formatted string.
    """
    formatted_string = input_string.replace("_", " ")
    formatted_string = ' '.join(word.capitalize() if not word.isupper() else word for word in formatted_string.split())

    return formatted_string


def set_alpha(ax, alpha):
    """Change the transparency of the patches in a plot.

    Args:
        ax (matplotlib.axes._subplots.AxesSubplot): The axis to modify.
        alpha (float): The transparency value.

    Returns:
        matplotlib.axes._subplots.AxesSubplot: The modified axis.
    """
    # Update the face colors of the patches
    for patch in ax.patches:
            r, g, b, a = patch.get_facecolor()
            patch.set_facecolor((r, g, b, alpha))

    legend = ax.get_legend()
    if legend:
        handles = legend.legend_handles
        # Update the face colors of the legend handles
        for handle in handles:
            r, g, b, a = handle.get_facecolor()
            handle.set_facecolor((r, g, b, alpha))

    return ax


def create_single_color_palette(data, color, palette, single_color='black'):
    """Create a single color palette.

    Args:
        data (pandas.DataFrame): The data.
        color (str): The column name for the color attribute.
        palette (str): The name of the palette or a list of colors.
        single_color (str): The single color to use.

    Returns:
        list: The single color palette.
    """
    if color:
        if single_color is not None:
            ncolors = len(data[color].unique())
            palette = [single_color] * ncolors
        else:
            if palette:
                palette = palette
            else:
                raise ValueError('No `palette` or `points_color` is defined.')
    else:
        palette = None
        
    return palette


def reformat_ticks_labels(ax, orient):
    new_ticks = []
    new_ticks_labels = []
    if orient == 'v':
        for tick, tick_label in zip(ax.get_xticks(), ax.get_xticklabels()):
            new_ticks.append(tick)
            new_ticks_labels.append(format_string(tick_label.get_text()))
        ax.set_xticks(new_ticks)
        ax.set_xticklabels(new_ticks_labels)
    else:
        for tick, tick_label in zip(ax.get_yticks(), ax.get_yticklabels()):
            new_ticks.append(tick)
            new_ticks_labels.append(format_string(tick_label.get_text()))
        ax.set_yticks(new_ticks)
        ax.set_yticklabels(new_ticks_labels)

    return ax
     

def prepare_sets(data, group_col, var_col):
    """Prepare data for a Venn diagram from a DataFrame.
    
    Args:
        df (pd.DataFrame): DataFrame containing the data.
        group (str): Column name of the group variable.
        var (str): Column name of the variable to compare.
        
    Returns:
        list: Labels for the sets.
        dict: Dictionary containing the counts for each subset.
    """
        # Get unique groups
    groups = data[group_col].unique()
    
    # Prepare the sets
    sets = [set(data[data[group_col] == group][var_col]) for group in groups]
    set_labels = list(map(str, groups))
    
    # Generate all possible combinations of group memberships, prioritizing larger intersections
    n = len(sets)
    all_combinations = sorted(
        chain.from_iterable(combinations(range(n), r) for r in range(1, n + 1)),
        key=lambda x: -len(x)  # Sort by length of combination, descending
    )

    # Prepare the subset labels with counts
    subset_labels = {}
    used_elements = set()

    for combo in all_combinations:
        # Create a tuple indicating the membership of each set
        membership = [1 if i in combo else 0 for i in range(n)]
        
        # Find intersection of all sets in the combination, excluding already counted elements
        intersection = set.intersection(*[sets[i] for i in combo]) - used_elements
        
        # Count the elements in the intersection
        if intersection:
            count = len(intersection)
            subset_labels[tuple(membership)] = count
            
            # Mark these elements as used
            used_elements.update(intersection)

    return set_labels, subset_labels


def blend_colors(color1, color2):
    """
    Blends two colors by averaging their RGBA values.
    
    Parameters:
        color1 (str): The first color (e.g., 'red').
        color2 (str): The second color (e.g., 'blue').
    
    Returns:
        blended_color (tuple): The blended color as an RGBA tuple.
    """
    rgba1 = to_rgba(color1)
    rgba2 = to_rgba(color2)
    
    # Average the RGBA values
    blended_color = tuple((a + b) / 2 for a, b in zip(rgba1, rgba2))
    
    return blended_color


def calculate_colors(subset_labels, palette):
    """
    Calculates the color for each subset based on the palette and intersections.
    
    Parameters:
        subset_labels (dict): Dictionary mapping subsets to their counts.
        palette (list): List of colors to be used for the individual sets.
    
    Returns:
        color_map (dict): Dictionary mapping subsets to colors.
    """
    n_sets = len(palette)
    
    # Initialize the color_map
    color_map = {}
    
    # Add colors for individual sets
    for idx in range(n_sets):
        color_map[tuple([1 if i == idx else 0 for i in range(n_sets)])] = palette[idx]
    
    # Add colors for intersections
    for subset in subset_labels.keys():
        if sum(subset) > 1:  # Skip individual sets
            involved_colors = [palette[i] for i, bit in enumerate(subset) if bit == 1]
            if involved_colors:
                # Blend colors for intersections
                blended_color = involved_colors[0]
                for color in involved_colors[1:]:
                    blended_color = blend_colors(blended_color, color)
                color_map[subset] = blended_color
    
    return color_map