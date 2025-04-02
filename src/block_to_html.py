from src.misc_functions import markdown_to_blocks
from src.blocktype import block_to_block_type, BlockType
from src.htmlnode import HTMLNode, ParentNode, LeafNode


def extract_text_from_markdown_block(block):
    



# Function to take markdown and convert it to html with full tagging.
def markdown_to_html(markdown):
    # Convert the markdown to markdown blocks.
    blocks = markdown_to_blocks(markdown)

    # Creating a list to store all of the block HTML nodes.
    block_nodes = []
    for block in blocks:
        # Getting the blocktype for each block.
        block_type = block_to_block_type(block)
        
        # Condition to create the paragraph HTMLNode.
        if block_type == BlockType.PARAGRAPH:
            node = HTMLNode("p", )




