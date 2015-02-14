# Compatability imports that allow usage in Python 2 & 3
from __future__ import print_function
from timeit import Timer


class Exceptions:

    class Empty(Exception):
        pass


class Algorithms:

    @classmethod
    def test(cls, algo):
        being_tested = Timer('{0}'.format(algo))
        return being_tested.timeit(algo)


class Recursion(Algorithms):

    @staticmethod
    def recur_reverse(s):
        """Recursively reverse a string"""
        if len(s) <= 1:
            return s
        return Recursion.recur_reverse(s[-1]) + Recursion.recur_reverse(s[:-1])

    @staticmethod
    def recur_palindrome(s):
        """Recursively check if string is palindrome"""

        def remove_white(s):
            """Remove white spaces"""
            return ''.join([x for x in s if x is not ' '])

        s = remove_white(s.lower())

        if len(s) <= 1:
            return True
        if s[0] != s[-1]:
            return False
        else:
            return True
        return Recursion.isPal(s[0]) + Recursion.isPal(s[:1])


class Hash(Algorithms):

    """Hashing algorithms"""

    @staticmethod
    def ord_hash(str1, table_size):
        """Hash strings using ordinals"""
        total = 0
        for pos in range(len(str1)):
            total = total + ord(str1[pos])

        return total % table_size


class DataStructures(Algorithms):

    class ArrayStack:

        """LIFO stack implementation with Python lists"""

        def __init__(self):
            self._data = []  # Private list

        def __len__(self):
            return len(self._data)

        def is_empty(self):
            return len(self._data) == 0

        def push(self, e):
            self._data.append(e)

        def top(self):
            # Last item in stack
            if self.is_empty():
                raise Exceptions.Empty('Stack is empty')
            return self._data[-1]

        def pop(self):
            """Remove and return element at the top (LIFO)"""
            if self.is_empty():
                raise Exceptions.Empty('Stack is empty')
            return self._data.pop()

    class LinearDataStructure:

        """Base class to be used by stacks, queues and deques"""

        def __init__(self):
            self.items = []

        def is_empty(self):
            return self.items == []

        def __str__(self):
            return str(self.items)

        def size(self):
            return len(self.items)

    class Stack(LinearDataStructure):

        """Improved stack data structure"""

        def clear(self):
            self.items = []

        def push(self, item):
            return self.items.append(item)

        def pop(self):
            return self.items.pop()

        def peek(self):
            return self.items[len(self.items) - 1]

        def reverse_string(self, string):
            """Reverse a string"""
            string = list(string)
            for char in string[::-1]:
                self.push(char)
            return ''.join(self.items)

        def decimal2binary(self, number):
            """Convert decimal number to binary"""
            while number > 0:
                remainder = number % 2
                self.push(remainder)
                number = number // 2

            binary_string = ""
            while not self.is_empty():
                binary_string = binary_string + str(self.pop())

            return binary_string

        def base_convert(self, number, base):
            """Convert decimal number to any base, not just base-2"""
            digits = "0123456789ABCDEF"

            while number > 0:
                remainder = number % base
                self.push(remainder)
                number = number // base

            new_string = ""
            while not self.is_empty():
                new_string = new_string + digits[self.pop()]

            return new_string

    class Queue(LinearDataStructure):

        """FIFO Queue data structure"""

        def enqueue(self, item):
            return self.items.insert(0, item)

        def dequeue(self):
            return self.items.pop()

    class Deque(LinearDataStructure):

        """Deque (double-ended queue)"""

        def add_front(self, item):
            self.items.append(item)

        def add_rear(self, item):
            self.items.insert(0, item)

        def remove_front(self):
            return self.items.pop()

        def remove_rear(self):
            return self.items.pop(0)

        def palindrome_checker(self, string):
            for i in string:
                self.add_rear(i)

            still_equal = True

            while self.size() > 1 and still_equal:
                first = self.remove_front()
                last = self.remove_rear()
                if first != last:
                    still_equal = False

            return still_equal

    class Node:

        """Node for linked list implementation"""

        def __init__(self, init_data):
            self.data = init_data
            self.next = None

        def get_data(self):
            return self.data

        def get_next(self):
            return self.next

        def set_data(self, new_data):
            self.data = new_data

        def set_next(self, new_next):
            self.next = new_next

    class UnorderedList:

        """Unordered (linked) list"""

        def __init__(self):
            self.head = None

        def is_empty(self):
            return self.head is None

        def add(self, item):
            node = DataStructures.Node(item)
            node.set_next(self.head)
            self.head = node

        def size(self):
            current = self.head
            count = 0
            while current is not None:
                count = count + 1
                current = current.get_next()

            return count

        def search(self, item):
            current = self.head
            found = False
            while current is not None and not found:
                if current.get_data() == item:
                    found = True
                else:
                    current = current.get_next()

            return found

        def remove(self, item):
            current = self.head
            previous = None
            found = False
            while not found:
                if current.get_data() == item:
                    found = True
                else:
                    previous = current
                    current = current.get_next()

            if previous is None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())

    class OrderedList:

        """Ordered list"""

        def __init__(self):
            self.head = None

        def search(self, item):
            current = self.head
            found = False
            stop = False

            while current is not None and not found and not stop:
                if current.get_data() == item:
                    found = True
                else:
                    if current.get_data() > item:
                        stop = True
                    else:
                        current = current.get_next()

            return found

        def add(self, item):
            current = self.head
            previous = None
            stop = False

            while current is not None and not stop:
                if current.get_data() > item:
                    stop = True
                else:
                    previous = current
                    current = current.get_next()

            temp = DataStructures.Node(item)
            if previous is None:
                temp.set_next(self.head)
                self.head = temp
            else:
                temp.set_next(current)
                previous.set_next(temp)

    class HashTable:

        """Hash table implementation"""

        def __init__(self):
            self.size = 11
            self.slots = [None] * self.size
            self.data = [None] * self.size

        def put(self, key, data):
            hashvalue = self.hashfunction(key, len(self.slots))

            if self.slots[hashvalue] == None:
                self.slots[hashvalue] = key
                self.data[hashvalue] = data

            else:
                if self.slots[hashvalue] == key:
                    self.data[hashvalue] = data  # Replace
                else:
                    next_slot = self.rehash(hashvalue, len(self.slots))
                    while self.slots[next_slot] != None and \
                            self.slots[next_slot] != key:
                        next_slot = self.rehash(next_slot, len(self.slots))
                    if self.slots[next_slot] == None:
                        self.slots[next_slot] = key
                        self.data[next_slot] = data
                    else:
                        self.data[next_slot] = data  # Replace

        def get(self, key):
            start_slot = self.hashfunction(key, len(self.slots))

            data = None
            stop = False
            found = False
            position = start_slot
            while self.slots[position] != None and \
                    not found and not stop:
                if self.slots[position] == key:
                    found = True
                    data = self.data[position]
                else:
                    position = self.rehash(position, len(self.slots))
                    if position == start_slot:
                        stop = True

            return data

        def __getitem__(self, key):
            return self.get(key)

        def __setitem__(self, key, data):
            self.put(key, data)

        def hashfunction(self, key, size):
            return key % size

        def rehash(self, oldhash, size):
            return (oldhash + 1) % size

    class BinaryTree:
        """Binary tree"""
        def __init__(self, root_obj):
            self.key = root_obj
            self.left_child = None
            self.right_child = None

        def insert_left(self, new_node):
            """Insert into left side of binary tree"""
            if self.left_child is None:
                self.left_child = DataStructures.BinaryTree(new_node)
            else:
                tree = DataStructures.BinaryTree(new_node)
                tree.left_child = self.left_child
                self.left_child = tree

        def insert_right(self, new_node):
            """Insert into right side of binary tree"""
            if self.right_child is None:
                self.right_child = DataStructures.BinaryTree(new_node)
            else:
                tree = DataStructures.BinaryTree(new_node)
                tree.right_child = self.right_child
                self.right_child = tree

        def get_right_child(self):
            """Return right child of binary tree"""
            return self.right_child

        def get_left_child(self):
            """Return left child of binary tree"""
            return self.left_child

        def set_root(self, new_root):
            """Set new root node for binary tree"""
            self.key = new_root

        def get_root(self):
            """Return root node for binary tree"""
            return self.key

        def __str__(self):
            return str([self.key, [self.left_child],
                       [self.right_child]])


class Search(Algorithms):

    @staticmethod
    def linear_search(values, target):
        """Linear search - O(n)"""
        i = 0
        for item in values:
            if values[i] == target:
                return item
            else:
                i += 1
        return -1

    @staticmethod
    def binary_search(data, target, low, high):
        """Binary search - Recursive, O(log n)"""

        if low > high:
            return False

        else:
            mid = (low + high) // 2
            if target == data[mid]:  # Found match
                return True
            elif target < data[mid]:
                # Recur on the left side of the array
                return Search.binary_search(data, target, low, mid - 1)
            else:
                # Recur on the right side of the array
                return Search.binary_search(data, target, mid + 1, high)

    @staticmethod
    def binary_search_iter(data, target):
        """Binary search - Iterative, O(log n)"""
        low = 0
        high = len(data) - 1
        while low <= high:
            mid = (low + high) // 2
            if target == data[mid]:
                return True
            elif target < data[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return False


class Math(Algorithms):

    @staticmethod
    def Euclid(p, q):
        """Euclidean algorithm - Finds GCF between two numbers"""
        if q == 0:
            return p
        r = p % q
        return Math.Euclid(q, r)

    @staticmethod
    def factorial(n):
        """Factorial - Recursive"""
        if n == 0 or n == 1:
            return 1
        return n * Math.factorial(n - 1)

    @staticmethod
    def factorial_i(n):
        """Factorial - Iterative"""
        result = 1
        while n > 1:
            result = result * n
            n -= 1
        return result

    @staticmethod
    def Fibonacci(n):
        """Fibonacci - O(n^2)"""
        if n <= 1:
            return n
        return Math.Fibonacci(n - 1) + Math.Fibonacci(n - 2)

    @staticmethod
    def Fibonacci_improved(n):
        """Fibonacci - O(n)"""
        if n <= 1:
            return (n, 0)
        else:
            (a, b) = Math.Fibonacci_improved(n - 1)
            return (a + b, a)

    @staticmethod
    def sum_of_nums_from_string(string):
        return sum([float(x) for x in string.split(',')])

    @staticmethod
    def listsum(lst):
        """Recrusive list summing"""
        # Define a base case
        if len(lst) == 1:
            return lst[0]
        # Move through the list recursively
        else:
            return lst[0] + Math.listsum(lst[1:])


class Sorting(Algorithms):

    @staticmethod
    def merge_sort(array):
        """Merge sort - Recursive, O(n log n)"""
        if len(array) <= 1:
            return array
        midpoint = len(array) / 2
        left_side = array[:midpoint]
        right_side = array[midpoint:]

        Sorting.merge_sort(left_side)
        Sorting.merge_sort(right_side)

        left_count = 0
        right_count = 0
        sorted_count = 0

        while left_count < len(left_side) and right_count < len(right_side):
            if left_side[left_count] < right_side[right_count]:
                array[sorted_count] = left_side[left_count]
                left_count += 1
            else:
                array[sorted_count] = right_side[right_count]
                right_count += 1
            sorted_count += 1

        while left_count < len(left_side):
            array[sorted_count] = left_side[left_count]
            left_count += 1
            sorted_count += 1

        while right_count < len(right_side):
            array[sorted_count] = right_side[right_count]
            right_count += 1
            sorted_count += 1

        return array

    @staticmethod
    def insertion_sort(q):
        """Insertion sort - O(n^2)"""
        for i in range(1, len(q)):
            current = q[i]
            j = i
            while j > 0 and q[j - 1] > current:
                q[j] = q[j - 1]
                j -= 1
            q[j] = current

    @staticmethod
    def bubble_sort(a_list):
        """Bubble sort - O(n^2)"""
        for i in range(len(a_list) - 1, 0, -1):
            for j in range(i):
                if a_list[j] > a_list[j + 1]:
                    temp = a_list[j]
                    a_list[j] = a_list[j + 1]
                    a_list[j + 1] = temp

    @staticmethod
    def selection_sort(a_list):
        """Selection sort - O(n^2)"""
        for i in range(len(a_list) - 1, 0, -1):
            max_position = 0
            for j in range(1, i + 1):
                if a_list[j] > a_list[max_position]:
                    max_position = j
            temp = a_list[i]
            a_list[i] = a_list[max_position]
            a_list[max_position] = temp

    @staticmethod
    def quicksort(a_list):
        """Quicksort - Amortized: O(n log n), Worst: O(n^2)"""
        Sorting.quicksort_helper(a_list, 0, len(a_list) - 1)

    @staticmethod
    def quicksort_helper(a_list, first, last):
        if first < last:
            split_point = Sorting.partition(a_list, first, last)

            Sorting.quicksort_helper(a_list, first, split_point - 1)
            Sorting.quicksort_helper(a_list, split_point + 1, last)

    @staticmethod
    def partition(a_list, first, last):
        pivot_value = a_list[first]

        left_mark = first + 1
        right_mark = last

        done = False
        while not done:

            while left_mark <= right_mark and \
                    a_list[left_mark] <= pivot_value:
                left_mark = left_mark + 1

            while a_list[right_mark] >= pivot_value and \
                    right_mark >= left_mark:
                right_mark = right_mark - 1

            if right_mark < left_mark:
                done = True

            else:
                temp = a_list[left_mark]
                a_list[left_mark] = a_list[right_mark]
                a_list[right_mark] = temp

        temp = a_list[first]
        a_list[first] = a_list[right_mark]
        a_list[right_mark] = temp

        return right_mark


class Generation(Algorithms):
    """Luhn's algorith, for generating and validating number sequences
    AKA mod 10 algorithm"""

    @staticmethod
    def Luhn(digits):
        """Generate a proper sum for a given sequence"""
        # Ensure that the data entered can become a list
        if type(digits) != 'str':
            digits = str(digits)

        # Convert data entered
        digits = [int(x) for x in digits]
        """
        Run heart of the algorithm, a description of which can be
        found on Wikipedia:

        https://en.wikipedia.org/wiki/Luhn_algorithm
        """
        for chars in digits[-1::-2]:
            if chars * 2 > 9:
                subscript = digits.index(chars)
                chars = chars * 2
                chars = int(int(str(chars)[0]) + int(str(chars)[1]))
                digits[subscript] = chars
            else:
                subscript = digits.index(chars)
                chars = chars * 2
                digits[subscript] = chars

        return sum(digits)

    @staticmethod
    def Luhn_digit(digits):
        """Generate a check digit"""
        return str(Generation.Luhn(digits) * 9)[-1]

    @staticmethod
    def Luhn_check(digits, check):
        """See if a sequence of digits and a key match up"""
        return (Generation.Luhn(digits) + check) % 10 == 0

    @staticmethod
    def combos(n, permutations):
        """Return combinations from a set of numbers up to n"""
        from itertools import combinations
        return list(combinations(range(n), permutations))

    @staticmethod
    def reverse(s):
        """Iteratively reverse items in sequence s"""
        start, stop = 0, len(s)
        while start < stop - 1:
            s[start], s[stop - 1] = s[stop - 1], s[start]
            start, stop = start + 1, stop - 1
        return s


class Crypto(Algorithms):

    class CaesarCipher:

        """Encrypt and decrypt using the ancient Caesar cipher"""

        def __init__(self, shift):
            """Define the cipher"""
            encoder = [None] * 26
            decoder = [None] * 26
            for k in range(26):
                encoder[k] = chr((k + shift) % 26 + ord('A'))
                decoder[k] = chr((k - shift) % 26 + ord('A'))
            self._forward = ''.join(encoder)
            self._backward = ''.join(decoder)

        def encrypt(self, message):
            return self._transform(message, self._forward)

        def decrypt(self, message):
            return self._transform(message, self._backward)

        def _transform(self, original, code):
            msg = list(original.upper())
            for k in range(len(msg)):
                if msg[k].isupper():
                    j = ord(msg[k]) - ord('A')
                    msg[k] = code[j]
            return ''.join(msg)


def measure_dynamic_array(n):
    """Measure the number of bytes a dynamic array up to size n-1
    takes up in memory"""
    import sys
    data = []
    for k in range(n):
        a = len(data)
        b = sys.getsizeof(data)
        print("Length: {0:3d}; Size in bytes: {1:4d}".format(a, b))
        data.append(None)



"""Experimentation area - uncomment areas of interest"""
if __name__ == '__main__':
    # print(Math.test(Math.factorial(10)))  # Test speed of factorial function
    # Generate a valid key sum for a check digit
    # print(Generation.Luhn_digit(7992739871))
    # Check a valid digit and key - should return True
    # print(Generation.Luhn_check(7992739871, 3))
    # Check an invalid digit and key - should return False
    # print(Generation.Luhn_check(7992739871, 2))

    # """Testing out the Caesar cipher"""
    # CC = Crypto.CaesarCipher(5)
    # test_message = 'The proof is in the pudding'
    # encrypted_message = CC.encrypt(test_message)
    # print(encrypted_message)
    # decrypted_message = CC.decrypt(encrypted_message)
    # print(decrypted_message)
    # print(CC.encrypt('Hello world'))

    # """Using my stack"""
    # stack1 = DataStructures.ArrayStack()
    # stack1.push('abc')
    # print(stack1.pop())

    # """Using improved stack"""
    # stack2 = DataStructures.Stack()
    # stack2.push('abc')
    # print(stack2.pop())

    # """Reverse string using stack"""
    # stack3 = DataStructures.Stack()
    # print(stack3.reverse_string('ABC'))

    # """Convert decimal numbers to binary"""
    # stack4 = DataStructures.Stack()
    # print(stack4.decimal2binary(5))

    # """Convert decimal numbers to other bases"""
    # stack5 = DataStructures.Stack()
    # print(stack5.base_convert(25, 8))
    # print(stack5.base_convert(256, 16))
    # print(stack5.base_convert(26, 26))

    # """Take my queue data structure for a spin"""
    # queue1 = DataStructures.Queue()
    # queue1.enqueue(5)
    # queue1.enqueue(True)
    # queue1.enqueue('Boomshakala!')
    # queue1.dequeue()
    # print(queue1)

    # """Operating on the front and rear of a deque"""
    # deque1 = DataStructures.Deque()
    # print(deque1.is_empty())
    # deque1.add_rear(8)
    # deque1.add_rear('Airplane')
    # deque1.add_front(False)
    # deque1.add_front(4)
    # print(deque1.size())
    # print(deque1)
    # deque1.add_rear(3.14)
    # print(deque1)
    # deque1.remove_rear()
    # deque1.remove_front()
    # print(deque1)

    # """Palindrome check using deque"""
    # deque2 = DataStructures.Deque()
    # print(deque2.palindrome_checker('radar'))
    # print(deque2.palindrome_checker('steve'))

    # """Linked list"""
    # linked1 = DataStructures.UnorderedList()
    # linked1.add(15)
    # linked1.add(22)
    # print(linked1.size())
    # print(linked1.search(22))
    # print(linked1.search(2))
    # linked1.remove(15)
    # print(linked1.size())

    # """Ordered list"""
    # ordered1 = DataStructures.OrderedList()
    # ordered1.add(10)
    # ordered1.add(25)
    # ordered1.add(12)
    # ordered1.add(5)
    # print(ordered1.search(5))

    # """Recursively reverse string"""
    # print(Recursion.recur_reverse('Hello'))
    # print(Recursion.recur_reverse('Sandwich'))

    # """Recursively check if string is palindrome"""
    # print(Recursion.recur_palindrome('Hello'))
    # print(Recursion.recur_palindrome('Bob'))
    # print(Recursion.recur_palindrome('B o b'))

    # """Hashing algorithms and data structures"""
    # print(Hash.ord_hash('a', 10))
    # HT = DataStructures.HashTable()
    # HT[10] = 'Cow'
    # HT[5] = 'Table'
    # HT[7] = 'Moose'
    # HT[34] = 'Airplane'
    # HT[83] = 'Nose'
    # print(HT.slots)
    # print(HT.data)
    # HT[10] = 'Bull'
    # HT[7] = 'Elk'
    # print(HT.data)

    # """Bubble sort"""
    # test_list = [4, 2, 5, 6, 20, 18, 30, 28, 50]
    # Sorting.bubble_sort(test_list)
    # print(test_list)

    # """Selection sort"""
    # test_list = [4, 2, 5, 6, 20, 18, 30, 28, 50]
    # Sorting.selection_sort(test_list)
    # print(test_list)

    # """Quicksort"""
    # test_list = [4, 2, 5, 6, 20, 18, 30, 28, 50]
    # Sorting.quicksort(test_list)
    # print(test_list)

    """Binary tree"""
    tree = DataStructures.BinaryTree('a')
    print("Root of binary tree:", tree.get_root())
    tree.insert_left('b')
    tree.insert_right('c')
    print("Left child:", tree.get_left_child())
    print("Right child:", tree.get_right_child())
