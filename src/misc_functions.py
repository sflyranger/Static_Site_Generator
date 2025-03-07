from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode
import re



# Function to convert a TextNode to an HTMLNode
def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src":text_node.url, "alt":text_node.text})
    else:
        raise Exception("Given text_type is not in the Enum construct for TextType")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    # Setting up list to add in delimited nodes.
    new_nodes = []
    for node in old_nodes:
        # If the node is not a TEXT type append it to the new_nodes and move to the next node.
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        # If the delimeter is not found append it to the new_nodes and continue to the next node.
        if delimiter not in node.text:
            new_nodes.append(node)
            continue

        # Set up an empty list to add the new nodes to be created and added to new_nodes
        list_of_split_nodes = []
        parts = node.text.split(delimiter)

        if len(parts) % 2 == 0:
            raise Exception(f"Delimiters not properly matched for: {node.text}")
        
        for i, part in enumerate(parts):
            if i % 2 == 0: # Checking only even indicies - the regular text.
                if part: # These are the non-empty parts, we skip the indices that are even and contain empty text strings from the split.
                    list_of_split_nodes.append(TextNode(part, TextType.TEXT))
            # Making the odd indicies into the input text_type TextNode.
            else:
                list_of_split_nodes.append(TextNode(part, text_type))

        new_nodes.extend(list_of_split_nodes)
    
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

    return matches







