import unittest

from src.block_to_html import markdown_to_html_node

class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is a **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        # Transform the markdown to paragraph html node
        node = markdown_to_html_node(md)

        # This is the display format.
        html = node.to_html()

        # This is what it should look like.
        expected = "<div><p>This is a <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>"
        
        # Checking for equality
        self.assertEqual(html, expected)

