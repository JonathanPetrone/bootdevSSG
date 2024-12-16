from textnode import *
from htmlnode import *
from split_nodes import *
from markdown_func import *

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

    text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    result = text_to_textnodes(text)
    print(result)

# Examine `resulting_nodes` to ensure it contains the expected TextNode objects
main()