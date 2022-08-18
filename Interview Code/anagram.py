# @author   Lucas Cardoso de Medeiros
# @since    06/06/2022
# @version  1.0

# ANAGRAM

# Rules:
# Strings s1 and s2 are anagrams if they're made with the same chars with the same frequency, just in different order
# Example:
# s1 = danger
# s2 = garden

# Solution 1: hashtable
# O(n) complexity
def hash_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        freq1 = {}
        freq2 = {}
        for ch in s1:
            if ch in freq1:
                freq1[ch] += 1
            else:
                freq1[ch] = 1
        for ch in s2:
            if ch in freq2:
                freq2[ch] += 1
            else:
                freq2[ch] = 1
        for key in freq1:
            if key not in freq2 or freq1[key] != freq2[key]:
                return False
        return True


# Solution 2: sort
# O(nlogn) complexity
def sort_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)


if __name__ == '__main__':
    s1 = "danger"
    s2 = "garden"
    if sort_anagrams(s1, s2):
        print('Yes')
    else:
        print('No')
