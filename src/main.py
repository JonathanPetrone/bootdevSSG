from textnode import *
from htmlnode import *
from split_nodes import *
from markdown_func import *
from block_to_html import *

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
    heading = '### This is a heading'
    heading_node = HTMLNode(tag=f"h{check_heading_level(heading)}")
    print(heading_node.tag)

    list = """1. This is the first list item in a list block
2. This is a list item
3. This is another list item"""

    print(markdown_to_html_node(list))
    

main()