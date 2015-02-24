# Compatability imports that allow usage in Python 2 & 3
from __future__ import print_function
from timeit import Timer
import string
import operator


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

        @staticmethod
        def build_parse_tree(fp_exp):
            """Use Stack and BinaryTree data structures to parse equations"""
            symbols = ['+', '-', '*', '/', ')']
            fp_list = fp_exp.split()
            p_stack = DataStructures.Stack()
            e_tree = DataStructures.BinaryTree('')
            p_stack.push(e_tree)
            current_tree = e_tree
            for i in fp_list:
                if i == '(':
                    current_tree.insert_left('')
                    p_stack.push(current_tree)
                    current_tree = current_tree.get_left_child()
                elif i not in symbols:
                    current_tree.set_root(int(i))
                    parent = p_stack.pop()
                    current_tree = parent
                elif i in symbols[:-1]:
                    current_tree.set_root(i)
                    current_tree.insert_right('')
                    p_stack.push(current_tree)
                    current_tree = current_tree.get_right_child()
                elif i == ')':
                    current_tree = p_stack.pop()
                else:
                    raise ValueError
            return e_tree

        @staticmethod
        def evaluate(parse_tree):
            """Recursively evaluate parse tree"""
            opers = {
                '+': operator.add,
                '-': operator.sub,
                '*': operator.mul,
                '/': operator.truediv,
            }

            left_child = parse_tree.get_left_child()
            right_child = parse_tree.get_right_child()

            if left_child and right_child:
                fn = opers[parse_tree.get_root()]
                return fn(DataStructures.BinaryTree.evaluate(left_child),
                          DataStructures.BinaryTree.evaluate(right_child))
            else:
                return parse_tree.get_root()

    class BinHeap:
        """Binary min heap data structure"""

        def __init__(self):
            self.heap_list = [0]
            self.current_size = 0

        def build_heap(self, a_list):
            """Build a heap from a list"""
            item = len(a_list) // 2
            self.current_size = len(a_list)
            self.heap_list = [0] + a_list[:]
            while (item > 0):
                self.move_down(item)
                item = item - 1

        def move_up(self, item):
            """Move a node up the heap"""
            while item // 2 > 0:
                if self.heap_list[item] < self.heap_list[item // 2]:
                    temp = self.heap_list[item // 2]
                    self.heap_list[item // 2] = self.heap_list[item]
                    self.heap_list[item] = temp
                item = item // 2

        def move_down(self, item):
            """Move a node down the heap"""
            while (item * 2) <= self.current_size:
                min_child = self.min_child(item)
                if self.heap_list[item] > self.heap_list[min_child]:
                    temp = self.heap_list[item]
                    self.heap_list[item] = self.heap_list[min_child]
                    self.heap_list[min_child] = temp
                item = min_child

        def min_child(self, item):
            """Get the smallest value in the heap"""
            if item * 2 + 1 > self.current_size:
                return item * 2
            else:
                if self.heap_list[item*2] < self.heap_list[item*2 + 1]:
                    return item * 2
                else:
                    return item * 2 + 1

        def insert(self, item):
            """Insert an element and maintain (min) heap property"""
            self.heap_list.append(item)
            self.current_size = self.current_size + 1
            self.move_up(self.current_size)

        def del_min(self):
            """Remove the smallest value in the heap"""
            return_value = self.heap_list[1]
            self.heap_list[1] = self.heap_list[self.current_size]
            self.current_size = self.current_size - 1
            self.heap_list.pop()
            self.move_down(1)
            return return_value

    class TreeNode:
        """Node for binary search tree"""

        def __init__(self, key, value,
                     left=None, right=None, parent=None):

            self.key = key
            self.payload = value
            self.left_child = left
            self.right_child = right
            self.parent = parent
            self.balance_factor = 0

        def __iter__(self):
            if self:
                if self.has_left_child():
                    for element in self.left_child:
                        yield element
                yield self.key
                if self.has_right_child():
                    for element in self.right_child:
                        yield element

        def has_left_child(self):
            return self.left_child

        def has_right_child(self):
            return self.right_child

        def is_left_child(self):
            return self.parent and self.parent.left_child == self

        def is_right_child(self):
            return self.parent and self.parent.right_child == self

        def is_root(self):
            return not self.parent

        def is_leaf(self):
            return not (self.right_child or self.left_child)

        def has_any_children(self):
            return self.right_child or self.left_child

        def has_both_children(self):
            return self.right_child and self.left_child

        def replace_node_data(self, key, value, left_child, right_child):
            self.key = key
            self.payload = value
            self.left_child = left_child
            self.right_child = right_child
            if self.has_left_child():
                self.left_child.parent = self
            if self.has_right_child():
                self.right_child.parent = self

    class BinarySearchTree:
        """Binary search tree - methods with single underscores are helpers"""

        def __init__(self):
            self.root = None
            self.size = 0

        def length(self):
            return self.size

        def __len__(self):
            return self.size

        def __iter__(self):
            return self.root.__iter__()

        def __setitem__(self, key, value):
            """
            Enables adding via dictionary syntax:
            my_tree['boom'] = 5
            """
            self.put(key, value)

        def __getitem__(self, key):
            """
            Enables dictionary lookup syntax:
            my_tree['boom']
            """
            return self.get(key)

        def __contains__(self, key):
            """
            Enables in calls:
            if 'boom' in my_tree: ...
            """
            if self._get(key, self.root):
                return True
            else:
                return False

        def __delitem__(self, key):
            """
            Enables use of 'del' keyword:
            del my_tree['boom']
            """
            self.delete(key)

        def put(self, key, value):
            if self.root:
                self._put(key, value, self.root)
            else:
                self.root = DataStructures.TreeNode(key, value)
            self.size = self.size + 1

        def _put(self, key, value, current_node):
            if key < current_node.key:
                if current_node.has_left_child():
                    self._put(key, value, current_node.left_child)
                else:
                    current_node.left_child = DataStructures.TreeNode(
                                              key, value, parent=current_node)
            else:
                if current_node.has_right_child():
                    self._put(key, value, current_node.right_child)
                else:
                    current_node.right_child = DataStructures.TreeNode(
                                               key, value, parent=current_node)

        def get(self, key):
            if self.root:
                res = self._get(key, self.root)
                if res:
                    return res.payload
                else:
                    return None

            else:
                return None

        def _get(self, key, current_node):
            if not current_node:
                return None
            elif current_node.key == key:
                return current_node
            elif key < current_node.key:
                return self._get(key, current_node.left_child)
            else:
                return self._get(key, current_node.right_child)

        def delete(self, key):
            if self.size > 1:
                node_to_remove = self._get(key, self.root)
                if node_to_remove:
                    self.remove(node_to_remove)
                    self.size = self.size - 1
                else:
                    raise KeyError('Key not in tree')
            elif self.size == 1 and self.root.key == key:
                self.root = None
                self.size = self.size - 1
            else:
                raise KeyError('Key not in tree')

        def find_successor(self):
            successor = None
            if self.has_right_child():
                successor = self.right_child.find_min()
            else:
                if self.parent:
                    if self.is_left_child():
                        successor = self.parent
                    else:
                        self.parent.right_child = None
                        successor = self.parent.find_successor()
                        self.parent.right_child = self

            return successor

        def find_min(self):
            current = self
            while current.has_left_child():
                current = current.left_child
            return current

        def splice_out(self):
            if self.is_leaf():
                if self.is_left_child():
                    self.parent.left_child = None
                else:
                    self.parent.right_child = None
            elif self.has_any_children():
                if self.has_left_child():
                    if self.is_left_child():
                        self.parent.left_child = self.left_child
                    else:
                        self.parent.right_child = self.left_child
                    self.left_child.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child
                self.right_child.parent = self.parent

        def remove(self, current_node):
            if current_node.is_leaf():
                """Node is a leaf (childless)"""
                if current_node == current_node.parent.left_child:
                    current_node.parent.left_child = None
                else:
                    current_node.parent.right_child = None
            elif current_node.has_both_children():
                sucessor = current_node.find_successor()
                sucessor.splice_out()
                current_node.key = sucessor.key
                current_node.payload = sucessor.payload

            else:
                """Node has one child"""
                if current_node.has_left_child():
                    if current_node.is_left_child():
                        current_node.left_child.parent = current_node.parent
                        current_node.parent.left_child = current_node.left_child
                    elif current_node.is_right_child():
                        current_node.left_child.parent = current_node.parent
                        current_node.parent.right_child = current_node.left_child
                    else:
                        current_node.replace_node_data(
                            current_node.left_child.key,
                            current_node.left_child.payload,
                            current_node.left_child.left_child,
                            current_node.left_child.right_child
                            )
                else:
                    if current_node.is_left_child():
                        current_node.right_child.parent = current_node.parent
                        current_node.parent.left_child = current_node.right_child
                    elif current_node.is_right_child():
                        current_node.right_child.parent = current_node.parent
                        current_node.parent.right_child = current_node.right_child
                    else:
                        current_node.replace_node_data(
                            current_node.right_child.key,
                            current_node.right_child.payload,
                            current_node.right_child.left_child,
                            current_node.right_child.right_child,
                            )

    class AVLTree(BinarySearchTree):
        """AVL (self-balancing) binary search tree"""

        def _put(self, key, value, current_node):
            if key < current_node.key:
                if current_node.has_left_child():
                    self._put(key, value, current_node.left_child)
                else:
                    current_node.left_child = DataStructures.TreeNode(
                        key, value, parent=current_node)
                    self.update_balance(current_node.left_child)
            else:
                if current_node.has_right_child():
                    self._put(key, value, current_node.right_child)
                else:
                    current_node.right_child = DataStructures.TreeNode(
                        key, value, parent=current_node)
                    self.update_balance(current_node.right_child)

        def update_balance(self, node):
            """Check and update balance factor for a node"""
            if node.balance_factor > 1 or node.balance_factor < -1:
                self.rebalance(node)
                return
            if node.parent is not None:
                if node.is_left_child():
                    node.parent.balance_factor += 1
                elif node.is_right_child():
                    node.parent.balance_factor -= 1

                if node.parent.balance_factor != 0:
                    self.update_balance(node.parent)

        def rotate_left(self, rotate_root):
            """Rotate tree to the left"""
            new_root = rotate_root.right_child
            rotate_root.right_child = new_root.left_child
            if new_root.left_child is not None:
                new_root.left_child.parent = rotate_root
            new_root.parent = rotate_root.parent
            if rotate_root.is_root():
                self.root = new_root
            else:
                if rotate_root.is_left_child():
                    rotate_root.parent.left_child = new_root
                else:
                    rotate_root.parent.right_child = new_root

            new_root.left_child = rotate_root
            rotate_root.parent = new_root
            rotate_root.balance_factor = rotate_root.balance_factor + 1 - min(new_root.balance_factor, 0)
            new_root.balance_factor = new_root.balance_factor + 1 + max(rotate_root.balance_factor, 0)

        def rotate_right(self, rotate_root):
            """Rotate tree to the right"""
            new_root = rotate_root.left_child
            rotate_root.left_child = new_root.right_child
            if new_root.right_child is not None:
                new_root.right_child.parent = rotate_root
            new_root.parent = rotate_root.parent
            if rotate_root.is_root():
                self.root = new_root
            else:
                if rotate_root.is_right_child():
                    rotate_root.parent.right_child = new_root
                else:
                    rotate_root.parent.left_child = new_root

            new_root.left_child = rotate_root
            rotate_root.parent = new_root
            rotate_root.balance_factor = rotate_root.balance_factor + 1 - min(new_root.balance_factor, 0)
            new_root.balance_factor = new_root.balance_factor + 1 + max(rotate_root.balance_factor, 0)

        def rebalance(self, node):
            if node.balance_factor < 0:
                if node.right_child.balance_factor > 0:
                    self.rotate_right(node.right_child)
                    self.rotate_left(node)
                else:
                    self.rotate_left(node)
            elif node.balance_factor > 0:
                if node.left_child.balance_factor < 0:
                    self.rotate_left(node.left_child)
                    self.rotate_right(node)
                else:
                    self.rotate_right(node)

    class Vertex:
        """Vertex for graphs"""

        def __init__(self, key):
            self.id = key
            self.connected_to = {}

        def add_neighbor(self, neighbor, weight=0):
            self.connected_to[neighbor] = weight

        def __str__(self):
            return str(self.id) + ' connected to: ' + str([x.id for x in self.connected_to])

        def get_connections(self):
            return self.connected_to.keys()

        def get_id(self):
            return self.id

        def get_weight(self, neighbor):
            return self.connected_to[neighbor]

    class Graph:
        """Graph data structure"""

        def __init__(self):
            self.vertices_list = {}
            self.number_of_vertices = 0

        def __iter__(self):
            return iter(self.vertices_list.values())

        def __contains__(self, node):
            return node in self.vertices_list

        def add_vertex(self, key):
            self.number_of_vertices = self.number_of_vertices + 1
            new_vertex = DataStructures.Vertex(key)
            self.vertices_list[key] = new_vertex
            return new_vertex

        def get_vertex(self, node):
            if node in self.vertices_list:
                return self.vertices_list
            else:
                return None

        def add_edge(self, f, t, weight=0):
            if f not in self.vertices_list:
                nv = self.add_vertex(f)
            if t not in self.vertices_list:
                nv = self.add_vertex(t)
            self.vertices_list[f].add_neighbor(self.vertices_list[t], weight)

        def get_vertices(self):
            return self.vertices_list.keys()


class Search(Algorithms):

    class DFSGraph(DataStructures.Graph):
        """Depth-first search of a graph"""

        def __init__(self):
            super().__init__()
            self.time = 0

        def dfs(self):
            for node in self:
                node.set_color('white')
                node.set_pred(-1)
            for node in self:
                if node.get_color() == 'white':
                    self.dfs_visit(node)

        def dfs_visit(self, start_node):
            start_node.set_color('gray')
            self.time += 1
            start_node.set_discovery(self.time)
            for next_node in start_node.get_connections():
                if next_node.get_color() == 'white':
                    next_node.set_pred(start_node)
                    self.dfs_visit(next_node)
            start_node.set_color('black')
            self.time += 1
            start_node.set_finish(self.time)

    @staticmethod
    def knights_tour(tree_depth, visited_nodes, current_node, limit):
        """Knight's tour algorithm - relies on Graph and Vertex"""
        current_node.set_color('gray')
        visited_nodes.append(current_node)
        if tree_depth < limit:
            number_list = list(current_node.get_connections())
            i = 0
            done = False
            while i < len(number_list) and not done:
                if number_list[i].get_color() == 'white':
                    done = Search.knights_tour(
                        tree_depth + 1, visited_nodes, number_list[i], limit
                        )
                i = i + 1
            if not done:
                """Get ready to backtrack"""
                visited_nodes.pop()
                current_node.set_color('white')
        else:
            done = True
        return done


    @staticmethod
    def pos_to_node_id(row, column, board_size):
        """Convert position on chess board to node number"""
        board = [[(x + (y * 5)) for x in range(5)] for y in range(5)]
        return board[row][column]

    @staticmethod
    def knight_graph(board_size):
        """Knight's tour graph"""
        graph = DataStructures.Graph()
        for row in range(board_size):
            """Note to self: build the pos_to_node_id function"""
            for column in range(board_size):
                node_id = Search.pos_to_node_id(row, column, board_size)
                new_positions = Search.gen_legal_moves(row, column, board_size)
                for e in new_positions:
                    n_id = Search.pos_to_node_id(e[0], e[1], board_size)
                    graph.add_edge(node_id, n_id)
        return graph

    @staticmethod
    def gen_legal_moves(x, y, board_size):
        new_moves = []
        move_offsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
                        (1, -2), (1, 2), (2, -1), (2, 1)]
        for i in move_offsets:
            new_x = x + i[0]
            new_y = y + i[1]
            if Search.legal_coordinates(new_x, board_size) and \
               Search.legal_coordinates(new_y, board_size):
                new_moves.append((new_x, new_y))
        return new_moves

    @staticmethod
    def legal_coordinates(x, board_size):
        if x >= 0 and x < board_size:
            return True
        else:
            return False

    @staticmethod
    def bfs(graph, start):
        """Breadth first search (BFS) for graphs"""
        start.set_distance(0)
        start.set_pred(None)
        node_queue = DataStructures.Queue()
        node_queue.enqueue(start)
        while (node_queue.size() > 0):
            current_node = node_queue.deque()
            for neighbor in current_node.get_connections():
                if (neighbor.get_color() == 'white'):
                    neighbor.set_color('gray')
                    neighbor.set_distance(current_node.get_distance() + 1)
                    neighbor.set_pred(current_node)
                    node_queue.enqueue(neighbor)
            current_node.set_color('black')

    @staticmethod
    def preorder(tree):
        """Pre-order tree traversal"""
        if tree:
            print(tree.get_root())
            Search.preorder(tree.get_left_child())
            Search.preorder(tree.get_right_child())

    @staticmethod
    def postorder(tree):
        """Post-order tree traversal"""
        if tree is not None:
            Search.postorder(tree.get_left_child())
            Search.postorder(tree.get_right_child())
            print(tree.get_root())

    @staticmethod
    def inorder(tree):
        """In-order tree traversal"""
        if tree is not None:
            Search.inorder(tree.get_left_child())
            print(tree.get_root())
            Search.inorder(tree.get_right_child())

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

    class TuringCipher:
        """Simple cipher based on Alan Turing's initial work in number theory"""

        def __init__(self, key):
            """Key must be prime"""
            self.key = key
            self.alphabet = {v: k for (k, v) in enumerate(string.ascii_letters)}

        def encode(self, message):
            """Encodes a message using the Turing cipher"""
            encoded = []
            for i in message:
                if i in self.alphabet.keys():
                    encoded.append(self.alphabet[i])
            return int(''.join(["%d" % x for x in encoded])) * self.key

        def decode(self, message):
            """Gives you the original number"""
            return message // self.key

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


class Build(Algorithms):

    @staticmethod
    def build_ladder_graph(word_file):
        dic = {}
        graph = DataStructures.Graph()
        w_file = open(word_file, 'r')
        """Create buckets of words that are off by one letter"""
        for line in w_file:
            word = line[:-1]
            for i in range(len(word)):
                bucket = word[:i] + '_' + word[i+1:]
                if bucket in dic:
                    dic[bucket].append(word)
                else:
                    dic[bucket] = [word]

        """Add nodes and edges for words in the same bucket"""
        for bucket in dic.keys():
            for word1 in dic[bucket]:
                for word2 in dic[bucket]:
                    if word1 != word2:
                        graph.add_edge(word1, word2)

        return graph


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

    # """Binary tree"""
    # tree = DataStructures.BinaryTree('a')
    # print("Root of binary tree:", tree.get_root())
    # tree.insert_left('b')
    # tree.insert_left('f')
    # tree.insert_right('c')
    # tree.insert_right('e')
    # print("Left child:", tree.get_left_child())
    # print("Right child:", tree.get_right_child())
    # Search.inorder(tree)


    # """Build a parse tree, then evaluate it"""
    # parse_tree1 = DataStructures.BinaryTree.build_parse_tree("( ( 10 + 5 ) * 3 )")
    # print(DataStructures.BinaryTree.evaluate(parse_tree1))  # 45

    # """Binary min heap"""
    # min_heap = DataStructures.BinHeap()
    # min_heap.build_heap([5, 8, 2, 4, 9, 12])
    # print(min_heap.heap_list)

    # """Binary search tree"""
    # bst = DataStructures.BinarySearchTree()
    # bst[3] = "Zebra"
    # bst[4] = "Cat"
    # bst[6] = "Antelope"

    # print(bst[3])
    # print(bst[4])
    # print(bst[6])

    # """AVL tree"""
    # avl = DataStructures.AVLTree()
    # avl[3] = "F/A-18"
    # avl[4] = "F-117"
    # avl[6] = "C-17"

    # print(avl[3])
    # print(avl[4])
    # print(avl[6])

    # """Graph"""
    # graph = DataStructures.Graph()
    # for i in range(5):
    #     graph.add_vertex(i)
    # graph.add_edge(0, 4, 1)
    # graph.add_edge(0, 1, 7)
    # graph.add_edge(1, 0, 4)
    # graph.add_edge(2, 1, 5)
    # print(graph.vertices_list)

    # for nodes in graph:
    #     for weights in nodes.get_connections():
    #         print("{}, {}".format(nodes.get_id(), weights.get_id()))

    """Knight's tour"""
    Search.knight_graph(5)