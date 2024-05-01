import unittest
import random
from BST import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()
        self.values = random.sample(range(1, 1000), 100)  # 100 random values between 1 and 1000
        for value in self.values:
            self.bst.insert(value)

    def test_insert_and_search(self):
        for value in self.values:
            self.assertTrue(self.bst.search(value))
        self.assertFalse(self.bst.search(1001))  # This value was not inserted
        print("Insert and Search Test Passed")

    def test_in_order_traversal(self):
        self.assertEqual(self.bst.in_order_traversal(), sorted(self.values))
        print("In Order Traversal Test Passed")

    def test_find_min(self):
        self.assertEqual(self.bst.find_min(), min(self.values))
        print("Find Min Test Passed")

    def test_find_max(self):
        self.assertEqual(self.bst.find_max(), max(self.values))
        print("Find Max Test Passed")

    def test_serialize_and_deserialize(self):
        serialized = self.bst.serialize()
        self.bst.deserialize(serialized)
        self.assertEqual(self.bst.in_order_traversal(), sorted(self.values))
        print("Serialize and Deserialize Test Passed")

if __name__ == '__main__':
    unittest.main() 