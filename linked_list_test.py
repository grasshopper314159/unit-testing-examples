import unittest
from linked_list import Node

class TestNodeAppend(unittest.TestCase):
    def test_for_single_node(self):
        node = Node(1)
        self.assertIsNone(node.next())
        node.append(2)
        self.assertIsNotNone(node.next(), None)
        self.assertEqual(node.next().value(), 2)

    def test_for_multiple_nodes(self):
        node2 = Node(2)
        node1 = Node(1, node2)
        self.assertIsNone(node2.next())
        node1.append(3)
        self.assertIsNotNone(node2.next(), None)
        self.assertEqual(node2.next().value(), 3)

class TestNodeContains(unittest.TestCase):
    def test_for_single_node(self):
        node = Node(1)
        self.assertTrue(node.contains(1))
        self.assertFalse(node.contains(2))

    def test_for_multiple_nodes(self):
        node = Node(1, Node(2))
        self.assertTrue(node.contains(1))
        self.assertTrue(node.contains(2))
        self.assertFalse(node.contains(3))

class TestNodeInsert(unittest.TestCase):
    def test_before_single_node(self):
        node = Node(1)
        node = node.insert(2, 0)
        self.assertEqual(node.value(), 2)
        self.assertEqual(node.next().value(), 1)
    
    def test_after_single_node(self):
        node = Node(1)
        node = node.insert(2, 1)
        self.assertEqual(node.value(), 1)
        self.assertEqual(node.next().value(), 2)
    
    def test_between_two_nodes(self):
        pass

    def test_after_two_nodes(self):
        pass
    
    def test_with_too_large_index(self):
        pass
    
    def test_negative_index(self):
        pass
    