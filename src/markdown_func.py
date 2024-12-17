import re

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def markdown_to_blocks(markdown):
    if markdown == "":
        return []

    # Split markdown by two consecutive newlines to get the blocks
    blocks = markdown.split("\n\n")
    new_list = []

    for block in blocks:
        if block.strip() != "":
            # Split block into lines
            lines = block.split("\n")
            # Strip each line of leading/trailing spaces, then join them back with newline
            processed_block = "\n".join(line.strip() for line in lines)
            new_list.append(processed_block)
    
    return new_list

def check_is_heading(block):
    if block.startswith('# '):
        return True
    elif block.startswith('## '):
        return True
    elif block.startswith('### '):
        return True
    elif block.startswith('#### '):
        return True
    elif block.startswith('##### '):
        return True
    elif block.startswith('###### '):
        return True
    else:
        return False

def check_is_code(block):
    return block.startswith('```') and block.endswith('```')

def check_is_quote_block(block):
    list_of_lines = block.splitlines()

    for line in list_of_lines:
        if not line.startswith('>'):
            return False
    
    return True

def check_is_ul(block):
    list_of_lines = block.splitlines()

    for line in list_of_lines:
        if not (line.startswith('- ') or line.startswith('* ')):
            return False
    
    return True

def check_is_ol(block):
    list_of_lines = block.splitlines()
    num = 1

    for line in list_of_lines:
        if not line.startswith(f'{num}. '):
            return False
        num +=1
    
    return True
    
    
def block_to_blocktype(block):
    '''
    If none of the above conditions are met, the block is a normal paragraph.
    '''
    if check_is_heading(block):
        return "heading"
    if check_is_code(block):
        return "code"
    if check_is_quote_block(block):
        return "quote"
    if check_is_ul(block):
        return "unordered_list"
    if check_is_ol(block):
        return "ordered_list"

    return "paragraph"

def extract_heading_content_from_md(heading):
    first_space = heading.find(' ')
    return heading[first_space:].strip()

def extract_title(markdown):
    lines = markdown.splitlines()
    for line in lines:
        line = line.strip()  # This will remove leading/trailing whitespace
        if line.startswith("# "):
            return extract_heading_content_from_md(line)
    
    raise Exception("no h1 header")