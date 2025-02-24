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
        l_node2 = LeafNode(None, "This is a leaf node", None)
        l_node3 = LeafNode("p", "This is a paragraph of text.", None)
        l_node4 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

        # Testing output of the value given that there is not a tag.
        l_node2_to_html = l_node2.to_html()
        expected2 = f"{l_node2.value}"
        self.assertEqual(l_node2_to_html, expected2)

        # Testing the proper html output of node3.
        l_node3_to_html = l_node3.to_html()
        expected3 = "<p>This is a paragraph of text.</p>"
        self.assertEqual(l_node3_to_html, expected3)
        
        # Testing the proper html output of node4
        l_node4_to_html = l_node4.to_html()
        expected4 = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(l_node4_to_html, expected4)


if __name__ == "__main__":
    unittest.main()
