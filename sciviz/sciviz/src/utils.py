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