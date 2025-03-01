import unittest
from misc_functions import text_node_to_html_node
from textnode import TextNode, TextType

class TestTextToHTML(unittest.TestCase):
    def test_text(self):
        tnode1 = TextNode("Practice Text", TextType.TEXT)


        test = text_node_to_html_node(tnode1)
        self.assertIsNone(test.tag)
        self.assertEqual(test.value, "Practice Text")
        self.assertEqual(test.props, {}) 


    def test_bold(self):
        tnode2 = TextNode("Practice Bolded", TextType.BOLD)
        test = text_node_to_html_node(tnode2)
        self.assertEqual(test.value, "Practice Bolded")
        self.assertEqual(test.tag, "b")
        self.assertEqual(test.props, {})

    def test_italic(self):
        tnode3 = TextNode("Practice Italicized", TextType.ITALIC)
        test = text_node_to_html_node(tnode3)
        self.assertEqual(test.tag, "i")
        self.assertEqual(test.value, "Practice Italicized")
        self.assertEqual(test.props, {})
    
    def test_code(self):
        tnode4 = TextNode("import numpy", TextType.CODE)
        test = text_node_to_html_node(tnode4)
        self.assertEqual(test.tag, "code")
        self.assertEqual(test.value, "import numpy")
        self.assertEqual(test.props, {})
    
    def test_link(self):
        tnode5 = TextNode("Practice Link", TextType.LINK, "www.google.com")
        test = text_node_to_html_node(tnode5)
        self.assertEqual(test.tag, "a")
        self.assertEqual(test.value, "Practice Link")
        self.assertEqual(test.props, {"href": "www.google.com"})
    
    def test_image(self):
        tnode6 = TextNode("This is a fake image", TextType.IMAGE, "www.google.com")
        test = text_node_to_html_node(tnode6)
        self.assertEqual(test.tag, "img")
        self.assertEqual(test.value, "")
        self.assertEqual(test.props, {"src": "www.google.com", "alt": "This is a fake image"})

    def test_exception(self):
        tnode7 = TextNode("This should fail", "not a valid type")
        with self.assertRaises(Exception):
            text_node_to_html_node(tnode7)
