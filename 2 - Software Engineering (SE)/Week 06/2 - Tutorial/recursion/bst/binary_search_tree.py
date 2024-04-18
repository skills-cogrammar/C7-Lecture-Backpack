from typing import List
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
        self.root = None

    def insert(self, key: int) -> None:
        """
        Inserts a key into the BST.

        Args:
            key (int): The value to insert into the BST.
        """
        pass

    def _insert_node(self, node, key: int) -> BSTNode:
        """
        Recursively inserts a key into the BST.

        Args:
            node (BSTNode or None): The current node being evaluated.
            key (int): The value to insert into the BST.

        Returns:
            BSTNode: The updated node.
        """
        pass

    def search(self, key: int):
        """
        Searches for a key in the BST.

        Args:
            key (int): The value to search for in the BST.

        Returns:
            Optional[BSTNode]: The node containing the key, or None if not found.
        """
        pass

    def _search_node(self, node, key: int):
        """
        Recursively searches for a key in the BST.

        Args:
            node (BSTNode or None): The current node being evaluated.
            key (int): The value to search for in the BST.

        Returns:
            Optional[BSTNode]: The node containing the key, or None if not found.
        """
        pass

    def iterative_inorder_traversal(self) -> List[int]:
        """
        Performs an iterative inorder traversal of the BST.

        Returns:
            List[int]: The list containing inorder traversal elements.
        """
        pass
    
    def recursive_inorder_traversal(self, node = None) -> None:
        """
        Recursively performs an inorder traversal of the BST.

        Args:
            node (BSTNode or None): The current node being evaluated. Defaults to None.
        """
        pass

    def recursive_preorder_traversal(self, node = None) -> None:
        """
        Recursively performs a preorder traversal of the BST.

        Args:
            node (BSTNode or None): The current node being evaluated. Defaults to None.
        """
        pass

    def recursive_postorder_traversal(self, node = None) -> None:
        """
        Recursively performs a postorder traversal of the BST.

        Args:
            node (BSTNode or None): The current node being evaluated. Defaults to None.
        """
        pass
