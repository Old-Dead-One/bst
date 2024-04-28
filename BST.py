class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree():
    def __init__(self):
        self.root = None

    def insert(self, value) -> None:  
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return

        current_node = self.root

        while True:
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = new_node
                    return
                current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = new_node
                    return
                current_node = current_node.right
     
    def search(self, value) -> bool:
        current_node = self.root

        while current_node is not None:
            if current_node.value == value:
                return True
            elif value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False
                
    def in_order_traversal(self) -> list[int]:
        def recursive_in_order(node):
            result = []
            if node is not None:
                result += recursive_in_order(node.left)
                result.append(node.value)
                result += recursive_in_order(node.right)
            return result
        
        return recursive_in_order(self.root)

    def find_min(self) ->int:
        if self.root is None:
            return 0
        current_node = self.root
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value
    
    def find_max(self) ->int:
        if self.root is None:
            return 0
        current_node = self.root
        while current_node.right is not None:
            current_node = current_node.right
        return current_node.value

    def height(self) -> int:
        def calc_height(node):
            if node is None:
                return 0
            left_height = calc_height(node.left)
            right_height = calc_height(node.right)
            return 1 + max(left_height, right_height)

        return calc_height(self.root)

    def count_leaves(self) -> int:
        def count_leaf_nodes(node):
            if node is None:
                return 0
            if node.left is None and node.right is None:
                return 1
            return count_leaf_nodes(node.left) + count_leaf_nodes(node.right)

        return count_leaf_nodes(self.root)

    def serialize(self) -> list:
        def recursive_serialize(node):
            if node is None:
                return ['None']
            return [str(node.value)] + recursive_serialize(node.left) + recursive_serialize(node.right)
        
        return recursive_serialize(self.root)
        
    def deserialize(self, tree_list: list) -> None:
        self.root = None
        for value_str in tree_list:
            if value_str == 'None':
                continue
            value = int(value_str)
            self.insert(value)
