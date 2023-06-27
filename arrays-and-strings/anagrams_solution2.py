# Python has a built in module that would actually make this super simple
from collections import Counter

def anagrams(s1, s2):
    return Counter(s1) == Counter(s2)

'''
`Counter` will take the given string and return a dictionary that counts
the frequency of each letter, exactly how the `count_char` method works in
solution 1.

Complexity remains the same:

    n = length of string 1
    m = length of string 2
    Time: O(n + m)
    Space: O(n + m)

'''