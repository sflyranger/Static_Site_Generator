from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def is_heading(block):
    # Checking if the block starts with a hash
    if not block.startswith("#"):
        return False

    # Getting the hash count to make sure it's a heading.
    hash_count = 0

    for char in block:
        if char == "#":
            hash_count+=1

        else:
            break
    # Checking to make sure the hash_count is between 1 and 6 and is followed by a whitespace
    if 1 <= hash_count <= 6 and block[hash_count] == ' ':
        return True
    return False

def is_code(block):
    return block.startswith("```") and block.endswith("```")


def is_quote(block):
    lines = block.splitlines()

    if not lines:
        return False
    
    for line in lines:
        if not line.startwith(">"):
            return False
    
    return True

def is_unordered_list(block):
    lines = block.splitlines()

    if not lines:
        return False
    
    for line in lines:
        if not line.startswith("- "):
            return False

    return True
        
def is_ordered_list(block):
    lines = block.splitlines()

    if not lines:
        return False
    
    expected_number = 1
    for line in lines:
        expected_prefix = f"{expected_number}. "

        if not line.startswith(expected_prefix):
            return False
        
        expected_number+=1
    
    return True

def block_to_block_type(block):
    if is_heading(block):
        return BlockType.HEADING
    elif is_code(block):
        return BlockType.CODE
    elif is_quote(block):
        return BlockType.QUOTE
    elif is_unordered_list(block):
        return BlockType.UNORDERED_LIST
    elif is_ordered_list(block):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH