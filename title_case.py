"""
A string is considered to be in title case if each word in the string is either
(a) capitalised (that is, only the first letter of the word is in upper case)
or (b) considered to be an exception and put entirely into lower case unless
it is the first word, which is always capitalised.

Write a function that will convert a string into title case, given an optional
list of exceptions (minor words). The list of minor words will be given as a
string with each word separated by a space. Your function should ignore the
case of the minor words string -- it should behave in the same way even if the
case of the minor word string is changed.

###Arguments

    First argument (required): the original string to be converted.
    Second argument (optional): space-delimited list of minor words that must
    always be lowercase except for the first word in the string.
"""


def title_case(title, minor_words=''):
    title = title.title().split()
    minor_words = minor_words.lower().split()
    for i in range(1, len(title)):
        if title[i].lower() in minor_words:
            title[i] = title[i].lower()
    return ' '.join(title)


assert title_case('') == ''
assert title_case('a clash of KINGS', 'a an the of') == 'A Clash of Kings'
assert title_case('THE WIND IN THE WILLOWS', 'The In') == 'The Wind in the Willows'
assert title_case('the quick brown fox') == 'The Quick Brown Fox'
