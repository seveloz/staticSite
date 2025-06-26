from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value == None:
            raise ValueError("LeafNode must have a value.")
        super().__init__(tag, value, None, props)


    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value to render HTML.")
        
        if self.tag is None:
            return self.value
        
        props_string = self.props_to_html()
        return f"<{self.tag}{props_string}>{self.value}</{self.tag}>"
