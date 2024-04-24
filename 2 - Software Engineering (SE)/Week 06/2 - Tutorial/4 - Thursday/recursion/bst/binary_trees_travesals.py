from binary_search_tree import BinarySearchTree

bst = BinarySearchTree()
bst.insert(15)
bst.insert(9)
bst.insert(20)
bst.insert(3)
bst.insert(10)
bst.insert(19)
bst.insert(30)

print("Found" if bst.search(7) else "Not Found")
# Found

print("Inorder Traversal: ")
bst.recursive_inorder_traversal(bst.root)

print(" ")

print("Preorder Traversal: ")
bst.recursive_preorder_traversal(bst.root)

print(" ")

print("Postorder Traversal: ")
bst.recursive_postorder_traversal(bst.root)
