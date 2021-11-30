"""
Unsure if I'm going to add more functions here so todo on this docstring
"""


def word_is_palindrome(word) -> bool:
    """
    returns True if a word is a palindrome.

    ignores case
    assumes words only include english ascii letters
    """
    word = word.lower()
    return word == word[::-1]
