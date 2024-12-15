from textnode import *
from htmlnode import *
from split_nodes import *

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.Normal_text:
            return LeafNode(None, text_node.text)
        case TextType.Bold_text:
            return LeafNode("b", text_node.text)
        case TextType.Italic_text:
            return LeafNode("i", text_node.text)
        case TextType.Code_text:
            return LeafNode("code", text_node.text)
        case TextType.Links:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.Images:
            return LeafNode("img", "", {"src":text_node.url, "alt":text_node.text})
        case _:
            raise Exception("Text node is not ok")

def main():
    print("hello world")

    node = TextNode("This is text with a `code block` word", TextType.Normal_text)
    new_nodes = split_nodes_delimiter([node], "`", TextType.Code_text)
    print(new_nodes)
main()