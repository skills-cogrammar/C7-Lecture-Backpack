# Binary Tree Node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Binary Search Tree Insertion
def insert(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def push(self, val):
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None
        self.swap(0, len(self.heap) - 1)
        val = self.heap.pop()
        self._sift_down(0)
        return val

    def peek(self):
        if not self.heap:
            return None
        return self.heap[0]

    def _sift_up(self, i):
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def _sift_down(self, i):
        while self.left_child(i) < len(self.heap):
            min_child = self.left_child(i)
            if self.right_child(i) < len(self.heap) and self.heap[self.right_child(i)] < self.heap[min_child]:
                min_child = self.right_child(i)
            if self.heap[i] > self.heap[min_child]:
                self.swap(i, min_child)
                i = min_child
            else:
                break

class PriorityQueue:
    def __init__(self):
        self.heap = MinHeap()

    def enqueue(self, val):
        self.heap.push(val)

    def dequeue(self):
        return self.heap.pop()

    def peek(self):
        return self.heap.peek()

    def is_empty(self):
        return len(self.heap.heap) == 0


# In-order Traversal
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val)
        inorder_traversal(root.right)

# Pre-order Traversal
def preorder_traversal(root):
    if root:
        print(root.val)
        preorder_traversal(root.left)
        preorder_traversal(root.right)

# Post-order Traversal
def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.val)

# Level-order Traversal
from collections import deque

def level_order_traversal(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Heapify
def heapify(arr):
    heap = MinHeap()
    for val in arr:
        heap.push(val)
    return heap

# Heapsort
def heapsort(arr):
    def sift_down(start, end):
        root = start
        while root * 2 + 1 <= end:
            child = root * 2 + 1
            if child + 1 <= end and arr[child] < arr[child + 1]:
                child += 1
            if arr[root] < arr[child]:
                arr[root], arr[child] = arr[child], arr[root]
                root = child
            else:
                break

    # Build max-heap
    for start in range(len(arr) // 2 - 1, -1, -1):
        sift_down(start, len(arr) - 1)

    # Heap sort
    for end in range(len(arr) - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        sift_down(0, end - 1)
    return arr

# Find the height of a binary tree
def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))

# Check if a binary tree is a BST
def is_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if not root:
        return True
    if root.val <= min_val or root.val >= max_val:
        return False
    return is_bst(root.left, min_val, root.val) and is_bst(root.right, root.val, max_val)

# Find the kth smallest element in a BST
def kth_smallest(root, k):
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if not k:
            return root.val
        root = root.right
