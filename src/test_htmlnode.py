import unittest 

from htmlnode import HTMLNode, LeafNode

# Second unit test to check and make sure the HTMLNode is working properly.
class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        # Test props
        props = {"href": "https://www.google.com", "target": "blank"}

        # Test nodes
        node = HTMLNode("p", "Sample Text", None, props)
        node2 = HTMLNode("p", "Sample Text", [node], props)

        expected = ' href="https://www.google.com" target="blank"'
        self.assertEqual(node.props_to_html(), expected)

        expected1 = "HTMLNode(p, Sample Text, None, {'href': 'https://www.google.com', 'target': 'blank'})"

        expected2 = "HTMLNode(p, Sample Text, [HTMLNode(p, Sample Text, None, {'href': 'https://www.google.com', 'target': 'blank'})], {'href': 'https://www.google.com', 'target': 'blank'})"

        self.assertEqual(node2.__repr__(), expected2)
        self.assertEqual(node.__repr__(), expected1)

    # Unit test to check to make sure leaf node is functioning properly
    def test_leaf(self):
        l_node = LeafNode("p", "This is a paragraph of text.")
        

if __name__ == "__main__":
    unittest.main()
