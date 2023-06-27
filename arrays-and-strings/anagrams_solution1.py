def anagrams(s1, s2):
    # Comparing dictionaries directly will check that each key:value pair is compared
    return char_count(s1) == char_count(s2)


# Create a dictionary counting the character frequency.
# ie. 'hello' --> {'h': 1, 'e': 1, 'l': 2, 'o': 1}
def char_count(s):
    count = {}
    for char in s:            # We pay for the O(n) complexity here
        if char not in count:
            count[char] += 0  # Init the key in the dict
        count[char] += 1      # Increment the count of the char by one
    return count

'''
Since there is O(n) complexity at the for loop, and we have two inputs (s1 and s2),
this has a compelxity of O(n+m):

    n = length of string 1
    m = length of string 2
    Time: O(n + m)
    Space: O(n + m)
'''