// Binary Tree Node
class TreeNode {
  constructor(val = 0, left = null, right = null) {
    this.val = val;
    this.left = left;
    this.right = right;
  }
}

// Binary Search Tree Insertion
function insert(root, val) {
  if (!root) {
    return new TreeNode(val);
  }
  if (val < root.val) {
    root.left = insert(root.left, val);
  } else {
    root.right = insert(root.right, val);
  }
  return root;
}

// Min Heap
class MinHeap {
  constructor() {
    this.heap = [];
  }

  parent(i) {
    return Math.floor((i - 1) / 2);
  }

  leftChild(i) {
    return 2 * i + 1;
  }

  rightChild(i) {
    return 2 * i + 2;
  }

  swap(i, j) {
    [this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]];
  }

  push(val) {
    this.heap.push(val);
    this._siftUp(this.heap.length - 1);
  }

  pop() {
    if (!this.heap.length) {
      return null;
    }
    this.swap(0, this.heap.length - 1);
    const val = this.heap.pop();
    this._siftDown(0);
    return val;
  }

  peek() {
    if (!this.heap.length) {
      return null;
    }
    return this.heap[0];
  }

  _siftUp(i) {
    while (i > 0 && this.heap[this.parent(i)] > this.heap[i]) {
      this.swap(i, this.parent(i));
      i = this.parent(i);
    }
  }

  _siftDown(i) {
    while (this.leftChild(i) < this.heap.length) {
      let minChild = this.leftChild(i);
      if (
        this.rightChild(i) < this.heap.length &&
        this.heap[this.rightChild(i)] < this.heap[minChild]
      ) {
        minChild = this.rightChild(i);
      }
      if (this.heap[i] > this.heap[minChild]) {
        this.swap(i, minChild);
        i = minChild;
      } else {
        break;
      }
    }
  }
}

class PriorityQueue {
  constructor() {
    this.heap = new MinHeap();
  }

  enqueue(val) {
    this.heap.push(val);
  }

  dequeue() {
    return this.heap.pop();
  }

  peek() {
    return this.heap.peek();
  }

  isEmpty() {
    return this.heap.heap.length === 0;
  }
}

// In-order Traversal
function inorderTraversal(root) {
  if (root) {
    inorderTraversal(root.left);
    console.log(root.val);
    inorderTraversal(root.right);
  }
}

// Pre-order Traversal
function preorderTraversal(root) {
  if (root) {
    console.log(root.val);
    preorderTraversal(root.left);
    preorderTraversal(root.right);
  }
}

// Post-order Traversal
function postorderTraversal(root) {
  if (root) {
    postorderTraversal(root.left);
    postorderTraversal(root.right);
    console.log(root.val);
  }
}

// Level-order Traversal
function levelOrderTraversal(root) {
  if (!root) {
    return;
  }
  const queue = [root];
  while (queue.length) {
    const node = queue.shift();
    console.log(node.val);
    if (node.left) {
      queue.push(node.left);
    }
    if (node.right) {
      queue.push(node.right);
    }
  }
}

// Heapify
function heapify(arr) {
  const heap = new MinHeap();
  for (const val of arr) {
    heap.push(val);
  }
  return heap;
}

// Find the height of a binary tree
function height(root) {
  if (!root) {
    return 0;
  }
  return 1 + Math.max(height(root.left), height(root.right));
}

// Check if a binary tree is a BST
function isBST(root, minVal = -Infinity, maxVal = Infinity) {
  if (!root) {
    return true;
  }
  if (root.val <= minVal || root.val >= maxVal) {
    return false;
  }
  return (
    isBST(root.left, minVal, root.val) && isBST(root.right, root.val, maxVal)
  );
}

// Heapsort
function swap(arr, i, j) {
  [arr[i], arr[j]] = [arr[j], arr[i]];
}

function heapifySort(arr, n, i) {
  let largest = i;
  let left = 2 * i + 1;
  let right = 2 * i + 2;

  if (left < n && arr[left] > arr[largest]) {
    largest = left;
  }

  if (right < n && arr[right] > arr[largest]) {
    largest = right;
  }

  if (largest !== i) {
    swap(arr, i, largest);
    heapifySort(arr, n, largest);
  }
}

function heapsort(arr) {
  const n = arr.length;

  // Build max heap
  for (let i = Math.floor(n / 2) - 1; i >= 0; i--) {
    heapifySort(arr, n, i);
  }

  // Extract elements from the heap one by one
  for (let i = n - 1; i > 0; i--) {
    swap(arr, 0, i);
    heapifySort(arr, i, 0);
  }

  return arr;
}

// Find the kth smallest element in a BST
function kthSmallest(root, k) {
  const stack = [];
  while (true) {
    while (root) {
      stack.push(root);
      root = root.left;
    }
    root = stack.pop();
    k--;
    if (!k) {
      return root.val;
    }
    root = root.right;
  }
}
