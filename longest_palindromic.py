"""
Write a function that finds the longest palindromic substring of a given string. Try to be as efficient as possible!

If you find more than one substring, you should return the one that’s closer to the beginning.

Input: A text as a string.

Output: The longest palindromic substring.
"""


def longest_palindromic(s):
    res = []
    while s:
        for i in range(len(s)):
            if s[:i + 1] == s[i::-1]:
                res.append(s[:i + 1])
        s = s[1:]
    return max(res, key=len)


if __name__ == '__main__':
    print("Example:")
    print(longest_palindromic('abc'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert longest_palindromic('abc') == 'a'
    assert longest_palindromic('abacada') == 'aba'
    assert longest_palindromic('artrartrt') == 'rtrartr'
    assert longest_palindromic('aaaaa') == 'aaaaa'
    print("Coding complete? Click 'Check' to earn cool rewards!")
