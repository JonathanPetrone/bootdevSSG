from markdown_func import *
from htmlnode import *
from split_nodes import *

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.Normal_text:
            return HTMLNode(None, text_node.text)
        case TextType.Bold_text:
            return HTMLNode("b", text_node.text)
        case TextType.Italic_text:
            return HTMLNode("i", text_node.text)
        case TextType.Code_text:
            return HTMLNode("code", text_node.text)
        case TextType.Links:
            return HTMLNode("a", text_node.text, None, {"href": text_node.url})
        case TextType.Images:
            return HTMLNode("img", "", None, {"src":text_node.url, "alt":text_node.text})
        case _:
            raise Exception("Text node is not ok")
        
def extract_code_snippet(code):
    start = code.find('```') + 3  # Find the first triple backtick and move 3 characters forward
    end = code.rfind('```')      # Find the last triple backtick
    return code[start:end]  

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

def make_list_items(l):
    new_list = l.split("\n")
    
    for i in range(len(new_list)):
        if new_list[i].startswith("* "):
            new_list[i] = new_list[i].replace("* ", "")
        if new_list[i].startswith("- "):
            new_list[i] = new_list[i].replace("- ", "")
        if re.match(r"^\d+\.\s", new_list[i]):
            new_list[i] = re.sub(r"^\d+\.\s", "", new_list[i])

    return new_list

def make_blockquote(quote):
    cleaned_lines = [line.lstrip().lstrip('> ').strip() for line in quote.splitlines()]

    # Combine all lines into a single string separated by a space
    result = ' '.join(cleaned_lines)
    
    return result

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        if html_node.value or html_node.tag:
            html_nodes.append(html_node)
    return html_nodes

def extract_heading_content(heading):
    first_space = heading.find(' ')
    return heading[first_space:].strip()

def markdown_to_html_node(markdown):

    parent_node = HTMLNode(tag="div")

    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        block_type = block_to_blocktype(block)
        # Example: if it's a heading
        if block_type == "heading":
            heading_level = check_heading_level(block)
            heading_text = extract_heading_content(block)
            heading_node = HTMLNode(tag=f"h{heading_level}", children=text_to_children(heading_text))  # create the heading node
            parent_node.children.append(heading_node)
        if block_type == "code":
            code_node = HTMLNode(tag="code", value=f"{extract_code_snippet(block)}")  # create the code node
            pre_node = HTMLNode(tag="pre", children=[code_node])
            parent_node.children.append(pre_node)
        if block_type == "unordered_list":
            list_node = HTMLNode(tag="ul")  # create the list node
            for item in make_list_items(block):
                li_node = HTMLNode(tag="li", children=text_to_children(item))
                list_node.children.append(li_node)
            parent_node.children.append(list_node)
        if block_type == "ordered_list":
            list_node = HTMLNode(tag="ol")  # create the list node
            for item in make_list_items(block):
                li_node = HTMLNode(tag="li", children=text_to_children(item))
                list_node.children.append(li_node)
            parent_node.children.append(list_node)
        if block_type == "quote":
            quote_content = make_blockquote(block)
            quote_node = HTMLNode(
                tag="blockquote", 
                children=text_to_children(quote_content)
            )
            parent_node.children.append(quote_node)
        if block_type == "paragraph":
            paragraph_node = HTMLNode(tag="p", children=text_to_children(block))  # create the p node
            parent_node.children.append(paragraph_node)
    
    return parent_node