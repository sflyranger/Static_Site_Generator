import unittest

from textnode import TextType, TextNode
from misc_functions import split_nodes_delimiter, split_nodes_link, split_nodes_image, text_to_textnodes, markdown_to_blocks

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

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )   
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [url](www.google.com) and another [url](www.github.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT), 
                TextNode("url", TextType.LINK, "www.google.com"), 
                TextNode(" and another ", TextType.TEXT), 
                TextNode("url", TextType.LINK, "www.github.com")
            ], 
            new_nodes, 
        )

    def test_text_to_testnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

        new_nodes = text_to_textnodes(text)

        self.assertListEqual([
        TextNode("This is ", TextType.TEXT),
        TextNode("text", TextType.BOLD),
        TextNode(" with an ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" word and a ", TextType.TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" and an ", TextType.TEXT),
        TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
        TextNode(" and a ", TextType.TEXT),
        TextNode("link", TextType.LINK, "https://boot.dev"),
        ], new_nodes, 
        )

    def test_markdown_to_blocks(self):
            md = """
        This is **bolded** paragraph

        This is another paragraph with _italic_ text and `code` here
        This is the same paragraph on a new line

        - This is a list
        - with items
        """
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [   
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )

            md2 = """
        This is **bolded** paragraph

        

        This is another paragraph with _italic_ text and `code` here
        This is the same paragraph on a new line

        

        - This is a list
        - with items
        - please clean and make blocks
        """
            blocks = markdown_to_blocks(md2)
            self.assertEqual(
                blocks,
                [   
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items\n- please clean and make blocks",
                ],
            )
        
if __name__ == "__main__":
    unittest.main()