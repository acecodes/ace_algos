# Time complexities

# Fetch an item from list


def fetch_item(item, lst):
    for element in lst:  # O(n)
        if element == item:  # O(1)
            return True  # O(1)
    return False  # O(1)

# O(n) + O(1) * O(1) * O(1)
# = O(n)

# Get pairs from a list


def get_pairs(lst):
    pair_list = []  # O(1)
    for i1 in lst:  # O(n)
        for i2 in lst:  # O(n)
            pair_list.append([i1, i2])  # O(1)
    return pair_list  # O(1)

# O(n) * O(n) + O(1) + O(1) + O(1)
# = O(n^2)
