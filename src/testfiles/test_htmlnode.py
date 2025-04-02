import unittest 

from src.htmlnode import HTMLNode, LeafNode, ParentNode

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


    # Unit Test to make sure ParentNode class is working and displaying correctly.
    def test_parent(self):
        props = {"href": "https://www.google.com", "target": "blank"}
        pnode1 = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text", props),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text", props),
                LeafNode(None, "Normal text"),
                ],
            )
        
        # Testing to ensure the correct output.
        expected1 = '<p><b href="https://www.google.com" target="blank">Bold text</b>Normal text<i href="https://www.google.com" target="blank">italic text</i>Normal text</p>'
        pnode1_to_html = pnode1.to_html()
        self.assertEqual(pnode1_to_html, expected1)

        # Testing a parent inside of a parent.
        pnode2 = ParentNode("p", [pnode1])
        expected2 = '<p><p><b href="https://www.google.com" target="blank">Bold text</b>Normal text<i href="https://www.google.com" target="blank">italic text</i>Normal text</p></p>'
        pnode2_to_html = pnode2.to_html()
        self.assertEqual(expected2, pnode2_to_html)

        
        self.assertRaises(ValueError, ParentNode, None, [pnode2])
        self.assertRaises(ValueError, ParentNode, "p", None)






if __name__ == "__main__":
    unittest.main()
