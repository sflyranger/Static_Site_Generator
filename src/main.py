from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from enum import Enum

def __main__():
    dummy_text_node = TextNode("dummy text", TextType.Normal, "www.boot.dev")
    print(dummy_text_node)

    test_props = {"href": "https://www.google.com", "target": "blank"}
    dummy_html_node = HTMLNode("p", "This is my first html value", None, test_props)
    print(dummy_html_node)
    props_to_html = dummy_html_node.props_to_html()

    print(props_to_html)
    dummy_html_node2 = HTMLNode("p", "Sample Text", [dummy_html_node], test_props)
    print(dummy_html_node2)

    pnode1 = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text", test_props),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text", test_props),
                LeafNode(None, "Normal text"),
                ],
            )
    pnode2 = ParentNode("p", [pnode1])

    print(pnode1.to_html())

    print(pnode2.to_html())

__main__()