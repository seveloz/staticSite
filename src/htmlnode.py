class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children or []
        self.props = props or {}

    def to_html(self):
        raise NotImplementedError("to_html() must be implemented by subclasses")
    

    def props_to_html(self):
        if not self.props:
            return ""
        return " " + " ".join(f'{key}="{value}"' for key, value in self.props.items())
    

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag is None:
            raise ValueError("ParentNode requires a tag.")
        if children is None or not isinstance(children, list):
            raise ValueError("ParentNode requires a list of children.")

        super().__init__(tag, None, children, props)


    def to_html(self):
        if not self.tag:
            raise ValueError("Cannot render ParentNode without a tag.")
        if self.children is None:
            raise ValueError("Cannot render ParentNode without children.")

        children_html = "".join(child.to_html() for child in self.children)
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
