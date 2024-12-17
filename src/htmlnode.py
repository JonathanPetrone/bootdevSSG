class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props

    def to_html(self):
        if self.children:
            for child in self.children:
                if not isinstance(child, HTMLNode):
                    print(f"Warning: child is not HTMLNode but {type(child)}: {child}")
                    
        value = "" if self.value is None else self.value
        
        if self.children == []:
            if self.tag is None:
                return value
            
            if self.props is not None:
                return f"<{self.tag}{self.props_to_html()}>{value}</{self.tag}>"
            return f"<{self.tag}>{value}</{self.tag}>"
        else:
            str_child = ""
            for child in self.children:
                str_child += child.to_html()
            
            if self.props is None:
                return f"<{self.tag}>{str_child}</{self.tag}>"
            return f"<{self.tag}{self.props_to_html()}>{str_child}</{self.tag}>"

    
    def props_to_html(self):
        if not self.props:  # Handles None or empty dict
            return ""
        
        props_strings = []
        for key, value in self.props.items():
            props_strings.append(f'{key}="{value}"')
        
        return " " + " ".join(props_strings)
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    def __eq__(self, other):
        return (
            self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
            self.props == other.props
        )


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
        return f"LeafNode({self.tag},{self.value},{self.props})"
    
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
        
        if self.props is None:
            return f"<{self.tag}>{str_child}</{self.tag}>"
        if self.props is not None:
            return f"<{self.tag} {self.props_to_html()}>{str_child}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})" 
