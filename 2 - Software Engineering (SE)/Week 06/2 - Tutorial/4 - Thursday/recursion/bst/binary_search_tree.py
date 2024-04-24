from typing import Optional, List
from bst_node import BSTNode

class BinarySearchTree:
    """
    Represents a Binary Search Tree (BST).

    Attributes:
        root (BSTNode): The root node of the BST.
    """

    def __init__(self) -> None:
        """
        Initializes an empty Binary Search Tree.
        """
        self.root: Optional[BSTNode] = None

    def insert(self, key: int) -> None:
        """
        Inserts a key into the BST.

        Args:
            key (int): The value to insert into the BST.
        """
        self.root = self._insert_node(self.root, key)

    def _insert_node(self, node: Optional[BSTNode], key: int) -> BSTNode:
        """
        Recursively inserts a key into the BST.

        Args:
            node (BSTNode or None): The current node being evaluated.
            key (int): The value to insert into the BST.

        Returns:
            BSTNode: The updated node.
        """
        if node is None:
            return BSTNode(key)
        if key < node.val:
            node.left = self._insert_node(node.left, key)
        else:
            node.right = self._insert_node(node.right, key)
        return node

    def search(self, key: int) -> Optional[BSTNode]:
        """
        Searches for a key in the BST.

        Args:
            key (int): The value to search for in the BST.

        Returns:
            Optional[BSTNode]: The node containing the key, or None if not found.
        """
        return self._search_node(self.root, key)

    def _search_node(self, node: Optional[BSTNode], key: int) -> Optional[BSTNode]:
        """
        Recursively searches for a key in the BST.

        Args:
            node (BSTNode or None): The current node being evaluated.
            key (int): The value to search for in the BST.

        Returns:
            Optional[BSTNode]: The node containing the key, or None if not found.
        """
        if node is None or node.val == key:
            return node
        if key < node.val:
            return self._search_node(node.left, key)
        return self._search_node(node.right, key)

    def iterative_inorder_traversal(self) -> List[int]:
        """
        Performs an iterative inorder traversal of the BST.

        Returns:
            List[int]: The list containing inorder traversal elements.
        """
        stack, result = [], []
        current = self.root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right
        return result
    
    def recursive_inorder_traversal(self, node: Optional[BSTNode] = None) -> None:
        """
        Recursively performs an inorder traversal of the BST.

        Args:
            node (BSTNode or None): The current node being evaluated. Defaults to None.
        """
        if node is not None:
            self.recursive_inorder_traversal(node.left)
            print(node.val, end=" ")
            self.recursive_inorder_traversal(node.right)

    def recursive_preorder_traversal(self, node: Optional[BSTNode] = None) -> None:
        """
        Recursively performs a preorder traversal of the BST.

        Args:
            node (BSTNode or None): The current node being evaluated. Defaults to None.
        """
        if node is not None:
            print(node.val, end=" ")
            self.recursive_preorder_traversal(node.left)
            self.recursive_preorder_traversal(node.right)

    def recursive_postorder_traversal(self, node: Optional[BSTNode] = None) -> None:
        """
        Recursively performs a postorder traversal of the BST.

        Args:
            node (BSTNode or None): The current node being evaluated. Defaults to None.
        """
        if node is not None:
            self.recursive_postorder_traversal(node.left)
            self.recursive_postorder_traversal(node.right)
            print(node.val, end=" ")
