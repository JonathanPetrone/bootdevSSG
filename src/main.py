from textnode import *
from htmlnode import *
from split_nodes import *
from markdown_func import *
from block_to_html import *
import os
import shutil
from pathlib import Path

def copy_from_folder_to_folder(source, destination):
    if not os.path.exists(source):
        raise Exception(f"source: '{source}' doesn't exist")

    if os.path.exists(destination):
        shutil.rmtree(destination)
        os.mkdir(destination)
    else:
        os.mkdir(destination)

    for item in os.listdir(source):
        if item.startswith('.'):  # Skip hidden files
            continue
        source_path = os.path.join(source, item)
        destination_path = os.path.join(destination, item)

        if os.path.isfile(source_path):
            shutil.copy(source_path, destination_path)
        else:
            os.mkdir(destination_path)
            copy_from_folder_to_folder(source_path, destination_path)

    return "ok"

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, 'r') as file:
        contents_md = file.read()
    
    with open(template_path, 'r') as file:
        contents_template = file.read()
    
    title = extract_title(contents_md)
    print(f"Title extracted: '{title}'")  # Added print
    
    html = markdown_to_html_node(contents_md).to_html()
    print(f"HTML generated: '{html[:100]}...'")  # Added print
    
    final_html = contents_template.replace("{{ Title }}", title).replace("{{ Content }}", html)

    with open(dest_path, 'w') as file:
        file.write(final_html)

    return "done"

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    '''
    Crawl every entry in the content directory
    For each markdown file found, generate a new .html file using the same template.html. 
    The generated pages should be written to the public directory in the same directory structure.
    '''
    entries = os.listdir(dir_path_content)
    for entry in entries:
        full_path = os.path.join(dir_path_content, entry)
        if os.path.isfile(full_path):
            if full_path.endswith('.md'):
                output_path = full_path.replace(dir_path_content, dest_dir_path)
                output_path = output_path.replace('.md', '.html')
                generate_page(full_path, template_path, output_path)
        else:
            new_content_path = os.path.join(dir_path_content, entry)
            new_dest_path = os.path.join(dest_dir_path, entry)
            os.makedirs(new_dest_path, exist_ok=True)
            generate_pages_recursive(new_content_path, template_path, new_dest_path)

    return "done"

def main():
    print(copy_from_folder_to_folder("static", "public"))

    generate_pages_recursive(
        dir_path_content="content",
        template_path="template.html",
        dest_dir_path="public"
    )

main()