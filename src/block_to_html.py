from markdown_func import *
from htmlnode import *

def extract_code_snippet(code):
    start = code.find('```') + 3  # Find the first triple backtick and move 3 characters forward
    end = code.rfind('```')      # Find the last triple backtick
    return code[start:end]  # Extract and strip any surrounding whitespace

def check_heading_level(heading):
    if heading.startswith('# '):
        return 1
    elif heading.startswith('## '):
        return 2
    elif heading.startswith('### '):
        return 3
    elif heading.startswith('#### '):
        return 4
    elif heading.startswith('##### '):
        return 5
    elif heading.startswith('###### '):
        return 6

def make_list_items(ul):
    new_list = ul.split("\n")
    
    for i in range(len(new_list)):
        if new_list[i].startswith("* "):
            new_list[i] = new_list[i].replace("* ", "")
        if new_list[i].startswith("- "):
            new_list[i] = new_list[i].replace("- ", "")

    return new_list

def markdown_to_html_node(markdown):

    parent_node = HTMLNode(tag="div")

    blocks = markdown_to_blocks(markdown)

    '''
    quote
    paragraph
    '''

    for block in blocks:
        block_type = block_to_blocktype(block)
        # Example: if it's a heading
        if block_type == "heading":
            heading_node = HTMLNode(tag=f"h{check_heading_level(block)}")  # create the heading node
            parent_node.children.append(heading_node)
        if block_type == "code":
            code_node = HTMLNode(tag="code", value=f"{extract_code_snippet(block)}")  # create the code node
            parent_node.children.append(code_node)
        if block_type == "unordered_list":
            list_node = HTMLNode(tag="ul")  # create the list node
            for item in make_list_items(block):
                li_node = HTMLNode(tag="li", value=f"{item}")
                list_node.children.append(li_node)
            parent_node.children.append(list_node)
        if block_type == "ordered_list":
            list_node = HTMLNode(tag="ol")  # create the list node
            for item in make_list_items(block):
                li_node = HTMLNode(tag="li", value=f"{item}")
                list_node.children.append(li_node)
            parent_node.children.append(list_node)
        if block_type == "quote":
            list_node = HTMLNode(tag="blockquote")  # create the quote node
            for item in make_list_items(block):
                li_node = HTMLNode(tag="li", value=f"{item}")
                list_node.children.append(li_node)
            parent_node.children.append(list_node)

    
    return parent_node