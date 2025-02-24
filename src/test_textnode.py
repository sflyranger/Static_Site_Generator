import unittest

from textnode import TextType, TextNode

# First unit test to test if the TextNode class is working.
class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.Bold)
        node2 = TextNode("This is a text node", TextType.Bold)
        self.assertEqual(node, node2)

        node3 = TextNode("This is a text node", TextType.Italic, "www.wackwebsite.com")
        self.assertNotEqual(node, node3)

        node4 = TextNode("This is text node", TextType.Bold)
        self.assertNotEqual(node, node4)
if __name__ == "__main__":
    unittest.main()