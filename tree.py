class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    """Tree data structure is a binary tree.
    The left subtree of a node contains only nodes with keys lesser than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    """
    def __init__(self):
        """
        Initialize the tree
        """
        self.root = None

    def insert(self, data):
        """
        Insert a node into the tree. Checks if tree has a root node
        """
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        """
        Insert a node into the tree. Inserts into either left or right child"""
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.insert_node(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self.insert_node(data, node.right)

    def print_tree(self):
        """
        Print the tree from the root node"""
        if self.root is not None:
            self.print_node(self.root)

    def print_node(self, node):
        """
        Print node from tree inorder"""
        if node is not None:
            self.print_node(node.left)
            print(str(node.data) + " ")
            self.print_node(node.right)
    
    def search(self, data):
        """
        Search for a node in the tree"""
        if self.root is not None:
            return self.search_node(data, self.root)
        else:
            return None
    
    def search_node(self, data, node):
        """
        Search for a node in the tree"""
        if node is None:
            return None
        if data == node.data:
            return node
        elif data < node.data:
            return self.search_node(data, node.left)
        else:
            return self.search_node(data, node.right)
    
    def delete(self, data):
        """
        Main method to delete node from tree"""
        if self.root is not None:
            self.root = self.delete_node(data, self.root)
    
    def delete_node(self, data, node):
        """
        Delete a node from the tree"""
        if node is None:
            return node
        if data < node.data:
            node.left = self.delete_node(data, node.left)
        elif data > node.data:
            node.right = self.delete_node(data, node.right)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            temp = self.min_node(node.right)
            node.data = temp.data
            node.right = self.delete_node(temp.data, node.right)
        return node
    
    def min_node(self, node):
        """
        Find the minimum value in the tree"""
        if node.left is None:
            return node
        else:
            return self.min_node(node.left)
    
    def max_node(self, node):
        """
        Find the maximum value in the tree"""
        if node.right is None:
            return node
        else:
            return self.max_node(node.right)
    
    def print_tree_in_order(self):
        """
        Print the tree in order"""
        if self.root is not None:
            self.print_tree_in_order_node(self.root)
    
    def print_tree_in_order_node(self, node):
        """
        Print the tree in order
        """
        if node is not None:
            self.print_tree_in_order_node(node.left)
            print(str(node.data) + " ")
            self.print_tree_in_order_node(node.right)
    
    def print_tree_pre_order(self):
        """"
        Print the tree in pre order"""
        if self.root is not None:
            self.print_tree_pre_order_node(self.root)
    
    def print_tree_pre_order_node(self, node):
        """
        Print the tree in pre order"""
        if node is not None:
            print(str(node.data) + " ")
            self.print_tree_pre_order_node(node.left)
            self.print_tree_pre_order_node(node.right)
    

if __name__ == "__main__":
    pass