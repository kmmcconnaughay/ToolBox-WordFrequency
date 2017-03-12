""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg """

import string


def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    # This open the file and makes the text lowercase
    text = open(file_name, 'r')
    # splits the lines into words
    split_words = []
    for string in text:
        split = string.split()
        split_words.extend(split)
    # strips the words of punctuation and whitespace
    stripped_words = []
    for word in split_words:
        word = word.lower()
        word = word.strip("/.,?!':;[]\")(%\r\n")
        stripped_words.append(word)
    return stripped_words


def get_top_n_words(stripped_words, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequently occurring.
    """
    d = {}
    for word in stripped_words:
        d[word] = d.get(word, 0) + 1
    ordered_words = sorted(d, key=d.get, reverse=True)
    top_frequencies = ordered_words[:n]
    for word in top_frequencies:
        punctuation = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
        for ch in word:
            if ch in punctuation: top_frequencies.remove(word)
    print(top_frequencies)
    return top_frequencies

if __name__ == "__main__":
    print('Running WordFrequency Toolbox')
    stripped_words = get_word_list('wizard.txt')
    get_top_n_words(stripped_words, 100)
