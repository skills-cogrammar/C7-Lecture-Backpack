from typing import Any, Optional

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
        self.left: Optional[BSTNode] = None
        self.right: Optional[BSTNode] = None
        self.val: Any = key
