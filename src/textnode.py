from enum import Enum

class TextType(Enum):
    Normal = "Normal"
    Bold = "Bold"
    Italic = "Italic"
    Code = "Code"
    Links = "Links"
    Images = "Images"

class TextNode():
    # Initialize text nodes with text, text_type and optional url inputs.
    def __init__(self, text: str, text_type: TextType, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    # Checking to see if two nodes have the same properties
    def __eq__(self, TextNode):
        
        if self.text == TextNode.text and self.text_type == TextNode.text_type and self.url == TextNode.url:
            return True
        else:
            return False

    # Function to print the string representation of the given Textnode object.    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
    


