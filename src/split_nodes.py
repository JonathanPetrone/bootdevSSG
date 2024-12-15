from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    if (delimiter != "`") and (delimiter != "*") and (delimiter != "**"):
        raise Exception("that's invalid Markdown syntax")

    for node in old_nodes:
        if node.text_type == TextType.Normal_text:
            parts = node.text.split(delimiter)

            if len(parts) % 2 == 0:
                raise Exception("Unmatched delimiter")
            
            for i, part in enumerate(parts):
                if i % 2 == 0:
                    # Even indexes get one type
                    node = TextNode(part, TextType.Normal_text)
                else:
                    # Odd indexes get another type
                    node = TextNode(part, text_type)
                new_nodes.append(node)
        else: new_nodes.append(node)

    return new_nodes
