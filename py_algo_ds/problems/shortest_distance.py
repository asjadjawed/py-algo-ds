"""
Find the shortest distance between two words in a list of words.
"""


def shortest_distance(words, word1, word2):
    """
    Find the shortest distance between two words in a list of words.
    Both the words are always present.

    Args:
    words (list of str): The list of words.
    word1 (str): The first word.
    word2 (str): The second word.

    Returns:
    int: The shortest distance between word1 and word2 in the list.

    Examples:
    >>> shortest_distance(["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], "fox", "dog")
    5

    >>> shortest_distance(["a", "b", "c", "d", "a", "b"], "a", "b")
    1

    >>> shortest_distance(["a", "c", "d", "b", "a"], "a", "b")
    1

    >>> shortest_distance(["a", "b", "c", "d", "e"], "a", "e")
    4
    """
    pointer_1 = -1
    pointer_2 = -1
    min_dist = len(words)

    for i, word in enumerate(words):
        if word == word1:
            pointer_1 = i
        if word == word2:
            pointer_2 = i
        if pointer_1 != -1 and pointer_2 != -1:
            min_dist = min(min_dist, abs(pointer_2 - pointer_1))

    return min_dist
