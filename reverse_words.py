"""
Complete the function that accepts a string parameter, and reverses each word in the string.
All spaces in the string should be retained.
Examples

"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
"""


def reverse_words(text):
    return ' '.join(x[::-1] for x in text.split(' '))


# tests
assert reverse_words('The quick brown fox jumps over the lazy dog.') == 'ehT kciuq nworb xof spmuj revo eht yzal .god'
assert reverse_words('apple') == 'elppa'
assert reverse_words('a b c d') == 'a b c d'
assert reverse_words('double  spaced  words') == 'elbuod  decaps  sdrow'
