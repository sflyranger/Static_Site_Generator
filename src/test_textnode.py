import unittest

from textnode import TextType, TextNode
from misc_functions import split_nodes_delimiter

# First unit test to test if the TextNode class is working.
class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

        node3 = TextNode("This is a text node", TextType.ITALIC, "www.wackwebsite.com")
        self.assertNotEqual(node, node3)

        node4 = TextNode("This is text node", TextType.BOLD)
        self.assertNotEqual(node, node4)
    
    def test_split_nodes_delimiter(self):
        node = TextNode("This is a test `code block` node.", TextType.TEXT)
        node2 = TextNode("This is a test **bold block** node.", TextType.TEXT)
        node3 = TextNode("This is a test _italic block_ node.", TextType.TEXT)
        node4 = TextNode("`Alt Code block` node.", TextType.TEXT)
        node5 = TextNode("Secondary **Alt bold block node**", TextType.TEXT)

        list_of_code_nodes = [node, node4]
        list_of_bold_nodes = [node2, node5]

        # Split the nodes using the split_nodes_delimiter function.
        split_code_nodes = split_nodes_delimiter(list_of_code_nodes, "`", TextType.CODE)
        split_bold_nodes = split_nodes_delimiter(list_of_bold_nodes, "**", TextType.BOLD)
        split_italic_nodes = split_nodes_delimiter([node3], "_", TextType.ITALIC)
        # New list of the repr for each node in the split.
        repr_code_nodes  = [node.__repr__() for node in split_code_nodes]
        repr_bold_nodes = [node.__repr__() for node in split_bold_nodes]
        repr_italic_nodes = [node.__repr__() for node in split_italic_nodes]


        expected_c = [
            'TextNode(This is a test , text, None)',
            'TextNode(code block, code, None)', 
            'TextNode( node., text, None)', 
            'TextNode(Alt Code block, code, None)', 
            'TextNode( node., text, None)'
        ]

        expected_b = [
            'TextNode(This is a test , text, None)', 
            'TextNode(bold block, bold, None)', 
            'TextNode( node., text, None)', 
            'TextNode(Secondary , text, None)', 
            'TextNode(Alt bold block node, bold, None)'
        ]

        expected_i = [
            'TextNode(This is a test , text, None)', 
            'TextNode(italic block, italic, None)', 
            'TextNode( node., text, None)'
        ]

        self.assertEqual(expected_c, repr_code_nodes)
        self.assertEqual(expected_b, repr_bold_nodes)
        self.assertEqual(expected_i, repr_italic_nodes)
        

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )



if __name__ == "__main__":
    unittest.main()