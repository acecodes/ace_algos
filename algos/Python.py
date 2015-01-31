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
            return self.items[len(self.items)-1]

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


class Search(Algorithms):
    # Linear search

    @staticmethod
    def linear_search(values, target):
        i = 0
        for item in values:
            if values[i] == target:
                return item
            else:
                i += 1
        return -1

    @staticmethod
    # Binary search
    def binary_search(data, target, low, high):

        if low > high:
            return False

        else:
            mid = (low + high) // 2
            if target == data[mid]:  # Found match
                return True
            elif target < data[mid]:
                # Recur on the left side of the array
                return binary_search(data, target, low, mid - 1)
            else:
                # Recur on the right side of the array
                return binary_search(data, target, mid + 1, high)

    @staticmethod
    # Binary search with iteration
    def binary_search_iter(data, target):
        """Return True if target is found in the given list"""
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
    # Euclid's algorithm
    # Finds the greatest common factor (GCF) between two numbers

    @staticmethod
    def Euclid(p, q):
        if q == 0:
            return p
        r = p % q
        return Euclid(q, r)

    # Factorial (n!) - recursive
    @staticmethod
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        return n * Math.factorial(n - 1)

    # Factorial (n!) - iterative
    @staticmethod
    def factorial_i(n):
        result = 1
        while n > 1:
            result = result * n
            n -= 1
        return result

    # Fibonacci (runs in quadratic time)
    @staticmethod
    def Fibonacci(n):
        if n <= 1:
            return n
        return Fibonacci(n - 1) + Fibonacci(n - 2)

    # Fibonacci (runs in linear time)
    @staticmethod
    def Fibonacci_improved(n):
        if n <= 1:
            return (n, 0)
        else:
            (a, b) = Fibonacci_improved(n - 1)
            return (a + b, a)

    @staticmethod
    def sum_of_nums_from_string(string):
        return sum([float(x) for x in string.split(',')])

    # Recursively sum up a list of numbers
    @staticmethod
    def listsum(lst):
        # Define a base case
        if len(lst) == 1:
            return lst[0]
        # Move through the list recursively
        else:
            return lst[0] + listsum(lst[1:])


class Sorting(Algorithms):
    # Merge sort

    @staticmethod
    def merge_sort(array):
        if len(array) == 1 or len(array) == 0:
            return array
        midpoint = len(array) / 2
        left_side = array[:midpoint]
        right_side = array[midpoint:]

        merge_sort(left_side)
        merge_sort(right_side)

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

    # A simple insertion sort (O(n^2)) algorithm
    @staticmethod
    def insertion_sort(q):
        for i in range(1, len(q)):
            current = q[i]
            j = i
            while j > 0 and q[j - 1] > current:
                q[j] = q[j - 1]
                j -= 1
            q[j] = current


class Generation(Algorithms):
    # Luhn's algorith, for generating and validating number sequences
    # AKA mod 10 algorithm

    # Generate a proper sum for a given sequence

    @staticmethod
    def Luhn(digits):
        # Ensure that the data entered can become a list
        if type(digits) != 'str':
            digits = str(digits)

        # Convert data entered
        digits = [int(x) for x in digits]

        # Run heart of the algorithm, a description of which can be found on Wikipedia:
        # https://en.wikipedia.org/wiki/Luhn_algorithm

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

    # Generate a check digit
    @staticmethod
    def Luhn_digit(digits):
        return str(Generation.Luhn(digits) * 9)[-1]

    # See if a sequence of digits and a key match up
    @staticmethod
    def Luhn_check(digits, check):
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


if __name__ == '__main__':
    print(Math.test(Math.factorial(10)))  # Test speed of factorial function
    # Generate a valid key sum for a check digit
    print(Generation.Luhn_digit(7992739871))
    # Check a valid digit and key - should return True
    print(Generation.Luhn_check(7992739871, 3))
    # Check an invalid digit and key - should return False
    print(Generation.Luhn_check(7992739871, 2))

    """Testing out the Caesar cipher"""
    CC = Crypto.CaesarCipher(5)
    test_message = 'The proof is in the pudding'
    encrypted_message = CC.encrypt(test_message)
    print(encrypted_message)
    decrypted_message = CC.decrypt(encrypted_message)
    print(decrypted_message)
    print(CC.encrypt('Hello world'))

    """Using my stack"""
    stack1 = DataStructures.ArrayStack()
    stack1.push('abc')
    print(stack1.pop())

    """Using improved stack"""
    stack2 = DataStructures.Stack()
    stack2.push('abc')
    print(stack2.pop())

    """Reverse string using stack"""
    stack3 = DataStructures.Stack()
    print(stack3.reverse_string('ABC'))

    """Convert decimal numbers to binary"""
    stack4 = DataStructures.Stack()
    print(stack4.decimal2binary(5))

    """Convert decimal numbers to other bases"""
    stack5 = DataStructures.Stack()
    print(stack5.base_convert(25, 8))
    print(stack5.base_convert(256, 16))
    print(stack5.base_convert(26, 26))

    """Take my queue data structure for a spin"""
    queue1 = DataStructures.Queue()
    queue1.enqueue(5)
    queue1.enqueue(True)
    queue1.enqueue('Boomshakala!')
    queue1.dequeue()
    print(queue1)

    """Operating on the front and rear of a deque"""
    deque1 = DataStructures.Deque()
    print(deque1.is_empty())
    deque1.add_rear(8)
    deque1.add_rear('Airplane')
    deque1.add_front(False)
    deque1.add_front(4)
    print(deque1.size())
    print(deque1)
    deque1.add_rear(3.14)
    print(deque1)
    deque1.remove_rear()
    deque1.remove_front()
    print(deque1)

    """Palindrome check using deque"""
    deque2 = DataStructures.Deque()
    print(deque2.palindrome_checker('radar'))
    print(deque2.palindrome_checker('steve'))
