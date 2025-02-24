

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
    def __init__(self, tag, value, props):
        super().__init__(tag, value, props)

    
    def to_html(self):

        if not self.value:
            raise ValueError("A value is required for a LeafNode")
        
        if not self.tag:
            return self.value
        
        else:
            if self.props:
                return f"<{self.tag}{self.props_to_html}>{self.value}</{self.tag}>"
            else:
                return f"<{self.tag}>{self.value}</{self.tag}>"
        





        

