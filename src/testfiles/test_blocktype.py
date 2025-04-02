import unittest

from blocktype import BlockType, block_to_block_type
from misc_functions import markdown_to_blocks

# Unit test class to test the BlockType functionality.
class TestBlockType(unittest.TestCase):
    def test_block_to_block_type(self):
        md = """
# This is a practice starter heading for the markdown

## This is a secondary heading

### Otra vez

### Otra vez, again

#### Otra vez, again, again

##### Almost there

###### Second before what should be a paragraph

####### This is the last, should return paragraph BlockType

``` This is a code block ```

``` This should be a paragraph``

`` This should be a paragraph ``

> This is a quote block

> Another, just to make sure

- Part one of an unordered list
- Part two
- Part three

-This should be a paragraph

1. Part one of an ordered list
2. Part two
3. Part three
4. You get the picture
5. Just to make sure

1.This should be a paragraph

This is a paragraph.

     """
        
        blocks = markdown_to_blocks(md)

        expected_response = [
            BlockType.HEADING,
            BlockType.HEADING,
            BlockType.HEADING,
            BlockType.HEADING,
            BlockType.HEADING,
            BlockType.HEADING,
            BlockType.HEADING,
            BlockType.PARAGRAPH,
            BlockType.CODE,
            BlockType.PARAGRAPH,
            BlockType.PARAGRAPH,
            BlockType.QUOTE,
            BlockType.QUOTE,
            BlockType.UNORDERED_LIST,
            BlockType.PARAGRAPH,
            BlockType.ORDERED_LIST,
            BlockType.PARAGRAPH,
            BlockType.PARAGRAPH
        ]

        actual_response = []

        for block in blocks:
            actual_response.append(block_to_block_type(block))

        
        self.assertListEqual(expected_response, actual_response)

if __name__ == "__main__":
    unittest.main()
