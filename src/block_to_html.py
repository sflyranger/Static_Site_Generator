import re 

from src.misc_functions import markdown_to_blocks, text_to_textnodes, text_node_to_html_node
from src.blocktype import block_to_block_type, BlockType
from src.htmlnode import HTMLNode, ParentNode, LeafNode
from src.textnode import TextNode, TextType

# Function to convert the code block to an html code block.
def code_block_to_html(block):
    # Removing backticks from the code block.
    lines = block.splitlines()

    if len(lines) >=2:
        lines = lines[1:-1] # Removing the first and last lines with the backticks
    
    # Rejoin the content.
    content = "\n".join(lines) + "\n"

    # No splitting into other text nodes here, so we just create a TextNode that's a code text_type.
    text_node = TextNode(content, TextType.CODE)

    child_node = text_node_to_html_node(text_node)
    # Convert this text node into an HTML node with the appropriate tag, and nested tag.
    html_node = ParentNode("pre", [child_node])

    return html_node



# Function to return an html_node for the heading block.
def heading_block_to_html(block):
    # Set up a counter for the hash_count.
    hash_count = 0

    # Increasing the hashcount based on the number of hashes.
    for char in block:
        if char == "#":
            hash_count+=1
        else:
            break
    # Stripping the block of its "#" values.
    block = block[hash_count:].lstrip()

    # Getting the children nodes by mapping the text_node_to_html_node function to the text_nodes from the block.
    children = list(map(text_node_to_html_node, text_to_textnodes(block)))
    
    # Creating the final node with the appropriate tag.
    html_node = ParentNode(f"h{hash_count}", children)

    return html_node 

# Function to convert ordered list blocks to html.
def ordered_list_block_to_html(block):
    # Splitting the block based on breaks.
    lines = block.splitlines()
    # Empty list to store child nodes, (each list item is a child).
    children = []

    # Looping through each line, creating a parent node that houses the other html nodes.
    for line in lines:
        line = re.sub(r'^\d+\.\s*', '', line)
        l_html_node = ParentNode("li",
                                  list(map(text_node_to_html_node,
                                                       text_to_textnodes(line)
                                                    )
                                                )
        )
        children.append(l_html_node)
    
    # Creating the final node with the appropriate tag.
    html_node = ParentNode("ol", children)

    return html_node

# Function to convert unordered list blocks to html.
def unordered_list_block_to_html(block):
    # Splitting the lines based on the breaks.
    lines = block.splitlines()

    # Empty list to store child nodes, (each list item is a child)
    children = []

    # Looping through each line, creating an parent node that houses the other html nodes.
    for line in lines:
        line = line.replace("- ", "")

        l_html_node = ParentNode("li", list(map(text_node_to_html_node, text_to_textnodes(line)))
        )
        children.append(l_html_node)

    # Creating the final node with the appropriate tag.
    html_node = ParentNode("ul", children)

    return html_node 

def quote_block_to_html(block):
    lines = [line.lstrip("> ") for line in block.splitlines()]

    content = "\n".join(lines)

    children = list(map(text_node_to_html_node, text_to_textnodes(content)))

    html_node = ParentNode("blockquote", children)

    return html_node


def paragraph_block_to_html(block):
    # Replacing newlines with spaces in a paragraph.
    new_block = block.replace("\n", " ")

    children = list(map(text_node_to_html_node, text_to_textnodes(new_block)))

    html_node = ParentNode("p", children)

    return html_node




# Function to take each block and convert it to text nodes
def block_to_html(block, block_type):
    try:

        # Special case if the block_type is CODE
        if block_type == BlockType.CODE:
            return code_block_to_html(block)

        elif block_type == BlockType.HEADING:
            return heading_block_to_html(block)
    
        elif block_type == BlockType.ORDERED_LIST:
            return ordered_list_block_to_html(block)
    
        elif block_type == BlockType.UNORDERED_LIST:
            return unordered_list_block_to_html(block)
        
        elif block_type == BlockType.QUOTE:
            return quote_block_to_html(block)
        
        else:
            return paragraph_block_to_html(block)
    
    except:
        raise Exception("Block type unknown or unrecognized.")
    

        

# Function to take markdown and convert it to html with full tagging.
def markdown_to_html_node(markdown):
    # Convert the markdown to markdown blocks.
    blocks = markdown_to_blocks(markdown)

    # Creating a list to store all of the block HTML nodes.
    children = []

    # Looping through the blocks and creating different child nodes for each block.
    for block in blocks:
        block_type = block_to_block_type(block)

        child_node = block_to_html(block, block_type)
        children.append(child_node)

    final_html_node = ParentNode("div", children)

    return final_html_node

    






