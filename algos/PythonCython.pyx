"""
Using Cython to speed up some algorithms
"""

def recur_reverse(str s):
    """Recursively reverse a string"""
    if len(s) <= 1:
        return s
    return recur_reverse(s[-1]) + recur_reverse(s[:-1])
