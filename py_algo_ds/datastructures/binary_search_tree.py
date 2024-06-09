"""
Binary Search Tree
"""

from __future__ import annotations


class Node:
    """
    Represents a node in a binary tree.

    Attributes:
        val (int): The value of the node.
        left (Node | None): The left child of the node.
        right (Node | None): The right child of the node.

    Args:
        val (int): The value of the node.
        left (Node | None): The left child of the node. Defaults to None.
        right (Node | None): The right child of the node. Defaults to None.
    """

    def __init__(self, val: int, left: Node | None = None, right: Node | None = None):
        self.val = val
        self.left = left
        self.right = right


def in_order_traversal(root: Node | None):
    """
    Performs an in-order traversal of a binary tree and prints the value of each node.

    Args:
        root (Node | None): The root node of the binary tree.
    """
    if root is not None:
        in_order_traversal(root.left)
        print(root.val)
        in_order_traversal(root.right)


def pre_order_traversal(root: Node | None):
    """
    Performs a pre-order traversal of a binary tree and prints the value of each node.

    Args:
        root (Node | None): The root node of the binary tree.
    """
    if root is not None:
        print(root.val)
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)


def post_order_traversal(root: Node | None):
    """
    Performs a post-order traversal of a binary tree and prints the value of each node.

    Args:
        root (Node | None): The root node of the binary tree.
    """
    if root is not None:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.val)


def build_bst(values: list[str]) -> Node | None:
    """
    Builds a binary search tree (BST) from a list of values represented as strings.
    It builds the tree using pre-order traversal.
    The special string "x" represents a None node.

    Args:
        values (List[LiteralString]): A list of values represented as strings.

    Returns:
        Node | None: The root node of the constructed BST.
    """
    if not values:
        return None
    val = values.pop(0)
    if val == "x":
        return None
    node = Node(int(val))
    node.left = build_bst(values)
    node.right = build_bst(values)
    return node
