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


    
