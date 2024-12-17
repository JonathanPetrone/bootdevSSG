from textnode import *
from htmlnode import *
from split_nodes import *
from markdown_func import *
from block_to_html import *

def main():
    

    markdown_quote = """### heading *fd*"""
    print(markdown_to_html_node(markdown_quote))

    
    

main()