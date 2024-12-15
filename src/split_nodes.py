from textnode import *
from markdown_func import *

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

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.Normal_text:
            new_nodes.append(node)
            continue
            
        # Get list of images
        images = extract_markdown_images(node.text)
        if not images:
            new_nodes.append(node)
            continue
            
        # Process just the first image
        alt_text, image_url = images[0]
        sections = node.text.split(f"![{alt_text}]({image_url})", 1)
        
        # Add text before image
        if sections[0]:
            new_nodes.append(TextNode(sections[0], TextType.Normal_text))
            
        # Add the image node
        new_nodes.append(TextNode(alt_text, TextType.Images, image_url))
        
        # Process remaining text recursively
        if len(sections) > 1 and sections[1]:
            remaining_node = TextNode(sections[1], TextType.Normal_text)
            new_nodes.extend(split_nodes_image([remaining_node]))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.Normal_text:
            new_nodes.append(node)
            continue
            
        links = extract_markdown_links(node.text)
        if not links:
            new_nodes.append(node)
            continue

        # Get just the first link
        link_text, link_url = links[0]
        # Split on just this one link
        sections = node.text.split(f"[{link_text}]({link_url})", 1)
        
        # Add the text that comes before the link
        if sections[0]:
            new_nodes.append(TextNode(sections[0], TextType.Normal_text))
            
        # Add the link itself
        new_nodes.append(TextNode(link_text, TextType.Links, link_url))
        
        # If there's text after the link, we need to process it for more links
        if len(sections) > 1 and sections[1]:
            remaining_node = TextNode(sections[1], TextType.Normal_text)
            new_nodes.extend(split_nodes_link([remaining_node]))

    return new_nodes