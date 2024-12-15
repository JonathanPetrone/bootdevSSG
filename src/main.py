from textnode import *
from htmlnode import *

def main():
    print("hello world")

    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text", {"color": "blue"}),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ], {"color": "red"}
    )

    print(node.to_html())
main()