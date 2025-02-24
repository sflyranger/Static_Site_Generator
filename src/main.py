from textnode import TextNode, TextType
from enum import Enum

def __main__():
    dummy_node = TextNode("dummy text", TextType.Normal, "www.boot.dev")
    print(dummy_node)

__main__()