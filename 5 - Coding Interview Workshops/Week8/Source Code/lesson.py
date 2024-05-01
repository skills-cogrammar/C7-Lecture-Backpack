class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_after(self, node, data):
        new_node = Node(data)
        new_node.next = node.next
        node.next = new_node

    def delete_at_beginning(self):
        if self.head is None:
            return
        self.head = self.head.next

    def delete_at_end(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def delete_node(self, node):
        if node is None or node.next is None:
            return
        node.data = node.next.data
        node.next = node.next.next

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next

class DoublyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = DoublyLinkedListNode(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = DoublyLinkedListNode(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def insert_after(self, node, data):
        new_node = DoublyLinkedListNode(data)
        new_node.next = node.next
        new_node.prev = node
        if node.next:
            node.next.prev = new_node
        else:
            self.tail = new_node
        node.next = new_node

    def delete_at_beginning(self):
        if self.head is None:
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None

    def delete_at_end(self):
        if self.tail is None:
            return
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None

    def delete_node(self, node):
        if node is None:
            return
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next

def reverse_linked_list(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def detect_loop(head):
    slow = head
    fast = head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

def find_middle(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow

import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        result = chardet.detect(file.read())
        return result['encoding']

def convert_encoding(text, from_encoding, to_encoding):
    return text.encode(from_encoding).decode(to_encoding)

import unicodedata

def normalize_unicode(text, form='NFC'):
    return unicodedata.normalize(form, text)

def case_fold(text):
    return text.casefold()

import re

def replace_unicode_characters(text, property, replacement):
    pattern = re.compile(f'\\p{{{property}}}')
    return pattern.sub(replacement, text)