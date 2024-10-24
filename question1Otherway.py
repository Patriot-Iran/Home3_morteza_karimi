from words2num import words2num

def words_to_numbers(text):
    """
    Converts all number-related words in the input text to their corresponding numeric representations.

    This function takes a string of text, splits it into words, and attempts to convert each word that
    represents a number into its numeric form using the `words2num` library. Words that cannot be 
    converted to numbers are left unchanged.

    Args:
        text (str): The input string containing number words.

    Returns:
        str: The input text with words representing numbers replaced by their numeric equivalents.

    Example:
        >>> words_to_numbers("I have three apples and two oranges.")
        'I have 3 apples and 2 oranges.'
    
    Note:
        This function processes each word separately, so multi-word number phrases (e.g., "one hundred twenty-three") 
        may not be handled correctly unless pre-processed differently.
    """

    text_list = text.split()
    convert = text
    for word in text_list:
        try:
            # Try converting word to number, if possible
            number = words2num(word)
            convert = convert.replace(word, str(number))
        except ValueError:
            # If the word is not a valid number, skip it
            continue
    return convert

path_ = "zen.txt"

# Open the input file for reading
with open(path_, "r") as f:
    text_ = f.read()

# Replace words with corresponding numbers
text_ = words_to_numbers(text_)

# Open the output file for writing
with open(path_, "w") as f:
    f.write(text_)
