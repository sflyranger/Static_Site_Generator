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
    
    def test_codeblock(self):
        md = """
```
This is a text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(md)
        
        html = node.to_html()

        expected = "<div><pre><code>This is a text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>"

        self.assertEqual(html, expected)
    
    def test_headingblock(self):
        self.maxDiff = None

        md = """
# This is a heading block with _italic_, **bolded** and `code` built in it.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = "<div><h1>This is a heading block with <i>italic</i>, <b>bolded</b> and <code>code</code> built in it.</h1></div>"

        self.assertEqual(html, expected)

        md2 = """
## This is a second heading block with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)
"""
        node2 = markdown_to_html_node(md2)
        html2 = node2.to_html()
        expected2 = '<div><h2>This is a second heading block with a link <a href="https://www.boot.dev">to boot dev</a> and <a href="https://www.youtube.com/@bootdotdev">to youtube</a></h2></div>'

        self.assertEqual(html2, expected2)

        md3 = """
### This is a third heading with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)
"""

        node3 = markdown_to_html_node(md3)
        html3 = node3.to_html()
        expected3 = '<div><h3>This is a third heading with a <img src="https://i.imgur.com/aKaOqIh.gif" alt="rick roll" /> and <img src="https://i.imgur.com/fJRm4Vk.jpeg" alt="obi wan" /></h3></div>'

        self.assertEqual(html3, expected3)

    
    def test_orderedlist_block(self):
        self.maxDiff = None 
        md = """
1. This is an ordered list with _italic_ text
2. **Bold** text
3. An ![image](https://i.imgur.com/aKaOqIh.gif)
4. And a link [to boot dev](https://www.boot.dev)
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = '<div><ol><li>This is an ordered list with <i>italic</i> text</li><li><b>Bold</b> text</li><li>An <img src="https://i.imgur.com/aKaOqIh.gif" alt="image" /></li><li>And a link <a href="https://www.boot.dev">to boot dev</a></li></ol></div>'

        self.assertEqual(html, expected)
