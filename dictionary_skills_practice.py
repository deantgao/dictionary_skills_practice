"""Dictionaries Practice

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""


def without_duplicates(words):
    """Given a list of words, return list with duplicates removed.

    For example::

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

        An empty list should return an empty list::

        >>> sorted(without_duplicates(
        ...     []))
        []

    The function should work for a list containing integers::

        >>> sorted(without_duplicates([111111, 2, 33333, 2]))
        [2, 33333, 111111]
    """
    word_count = {} # this initializes an empty dictionary
    unique_words = [] # this initializes an empty list

    for word in words: # this iterates over every word in the list of words
        word_count[word] = word_count.get(word, 0) + 1 # this adds each word into the
        # dictionary and sets its value to either 1 or 1 + the value that already
        # exists for that word

    for item in word_count: # this iterates over every item in the dictionary "word count"
        unique_words.append(item) # this appends each item in the dictionary to a list
            
    return sorted(unique_words) # this returns a sorted copy of the unique_words list


def find_unique_common_items(items1, items2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items
    shared between the lists.

    **IMPORTANT**: you may not use `'if ___ in ___``
    or the method `list.index()`.

    This should find [1, 2]::

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists,
    don't show more than 1 or 2 once::

        >>> sorted(find_unique_common_items([3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    The elements should not be treated as duplicates if they are
    different data types::

        >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
        [2]
    """
    unique_words = {} # initializes an empty dictionary to use later to count unique words
    unique_items1 = [] # initializes an empty list to store items1 without duplicates
    unique_items2 = [] # initializes an empty list to store items2 without duplicates
    common_words = [] # initializes an empty list to store unique words in common from items1 and items2
    sorted_items1 = sorted(items1) # creates a sorted copy of items1
    sorted_items2 = sorted(items2) # creates a sorted copy of items2

    for i in range(len(sorted_items1)): # iterates over each index for the length of list
        if sorted_items1[i] != sorted_items1[i-1]: # checks for condition that if word at index i
        # does not equal word at index before it:
            unique_items1.append(sorted_items1[i]) # adds the word to list unique_items1
    for i in range(len(sorted_items2)): # repeats the above on sorted_items2
        if sorted_items2[i] != sorted_items2[i-1]:
            unique_items2.append(sorted_items2[i])
    new_words = unique_items1 + unique_items2 # creates new list that is the sum of two

    for word in new_words: # iterates over each word in new list
        unique_words[word] = unique_words.get(word, 0) + 1 # adds word into dictionary
        # and starts count at 1 and increases to 2 if word appears again
    for key in unique_words: # iterates over each key in dictionary
        if unique_words[key] == 2: # creates condition that if value at key == 2
            common_words.append(key) # add that key word to a new list 

    return sorted(common_words) # returns a sorted list of unique words in common


def get_sum_zero_pairs(numbers):
    """Given list of numbers, return list of pairs summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

    For example::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself)::

        >>> sort_pairs( get_sum_zero_pairs([1, 3, -1, 1, 1, 0]) )
        [[-1, 1], [0, 0]]
    """

    return []


def top_chars(phrase):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most in the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example::

        >>> top_chars("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example::

        >>> top_chars("Shake it off, shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """

    return []

#####################################################################
# You can ignore everything below this.


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
