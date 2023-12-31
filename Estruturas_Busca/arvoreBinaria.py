class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(value, self.root)

    def _insert_recursive(self, value, current_node):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(value, current_node.left)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(value, current_node.right)

    def search(self, value):
        return self._search_recursive(value, self.root)

    def _search_recursive(self, value, current_node):
        if current_node is None or current_node.value == value:
            return current_node
        if value < current_node.value:
            return self._search_recursive(value, current_node.left)
        return self._search_recursive(value, current_node.right)
    
bst = BinarySearchTree()

def createBinaryTree(list):
    global bst
    for num in list:
        bst.insert(num)

def searchBinaryTree(value):
    global bst
    result = bst.search(value)
    if result:
        print(f'O valor {value} foi encontrado na árvore.')
    else:
        print(f'O valor {value} não foi encontrado na árvore.')