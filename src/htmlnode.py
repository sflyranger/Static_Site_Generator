import logging 
logging.basicConfig(level=logging.DEBUG)

class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    # Method designed to be overriden by children of the class
    def to_html(self):
        raise NotImplementedError
    
    # Method to convert the props to html format
    def props_to_html(self):

        if self.props == None:
            raise Exception("Props not populated.")
        else:
            prop_list = []
            for key, value in self.props.items():
                prop_list.append(f' {key}="{value}"')
            
            prop_str = "".join(prop_list)

            return prop_str
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

# Creating the LeafNode class that inherits from the HTMLNode class
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props={}):
        super().__init__(tag, value, None, props)
    
    def to_html(self):

        if self.tag != "img" and self.value is None:
            print(f"Error Empty value in LeafNode with tag={self.tag}, props={self.props}")
            raise ValueError("A value is required for a LeafNode")
        
        if not self.tag:
            return self.value
        
        if self.tag == "img":
            return f"<{self.tag}{self.props_to_html()} />"
        
        else:
            if self.props:
                return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
            else:
                return f"<{self.tag}>{self.value}</{self.tag}>"
    
        

# Creating the ParentNode class for HTMLNodes that have children
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)
        self.children = children

        if not tag:
            raise ValueError("A tag is required for a ParentNode")
        elif not children:
            raise ValueError("Children are required for ParentNodes")
        
    def to_html(self):
        base_str = f"<{self.tag}>"
            
        for child in self.children:
            base_str = base_str + child.to_html()
            
            
        end_str = f"</{self.tag}>"
        final_str = base_str + end_str

        return final_str



        

