class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        pass
    
    def props_to_html(self):
        if self.props == None:
            return ""
        props = self.props.copy()
        str_props = " ".join([f'{key}="{value}"' for key, value in props.items()])

        return str_props
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag=tag, props=props)
        self.value = value
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if not self.tag and self.props:
            raise ValueError("Props cannot be associated with an element without a tag.")

    def to_html(self):
        if self.tag is None:
            return self.value
        
        if self.props is not None:
            return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"

        return f"<{self.tag}>{self.value}</{self.tag}>"
        
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag=tag, props=props)
        if self.tag is None:
            raise ValueError("All parent nodes must have a tag")
        
        if not isinstance(children, list) or len(children) == 0:
            raise ValueError("ParentNode requires a non-empty list of children")
        
        if not self.tag and self.props:
            raise ValueError("Props cannot be associated with an element without a tag.")
        self.children = children
    
    def to_html(self):
        str_child = ""
        ## för varje child till parent, om den har children så är den en parent och behöver exekveras igen
        for child in self.children:
            str_child += child.to_html()
        
        return f"<{self.tag} {self.props_to_html()}>{str_child}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})" 
