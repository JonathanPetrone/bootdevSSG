from enum import Enum

class TextType(Enum):
    Normal_text = "normal"
    Bold_text = "bold"
    Italic_text = "italic"
    Code_text = "code"
    Links = "link"
    Images = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, target):
        if (self.text == target.text and self.text_type == target.text_type and self.url == target.url):
            return True
        
        return False

    def __repr__(self):
        if self.url is None:
            return f"TextNode({self.text}, {self.text_type})"
        return f"TextNode({self.text}, {self.text_type}, {self.url})"