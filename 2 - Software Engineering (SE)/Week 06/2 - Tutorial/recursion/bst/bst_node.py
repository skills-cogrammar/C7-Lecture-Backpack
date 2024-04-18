from typing import Any

class BSTNode:
    """A node in a Binary Search Tree (BST).

    Attributes:
        left (Optional[BSTNode]): The left child node.
        right (Optional[BSTNode]): The right child node.
        val: The value stored in the node.
    """

    def __init__(self, key: Any) -> None:
        """Initialize a BSTNode with the given value.

        Args:
            key: The value to be stored in the node.
        """
        self.left = None
        self.right = None
        self.val = key
