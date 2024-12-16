import unittest

from main import *
from htmlnode import *
from textnode import TextNode, TextType
from block_to_html import *

markdown_1 = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.





* This is the first list item in a list block
* This is a list item
* This is another list item"""

markdown_1_expected = HTMLNode(
    tag="div",
    children=[
        HTMLNode(
            tag="h1",
            children=[
                HTMLNode(value="This is a heading")
            ]
        ),
        HTMLNode(
            tag="p",
            children=[
                HTMLNode(value="This is a paragraph of text. It has some "),
                HTMLNode(tag="b", children=[HTMLNode(value="bold")]),
                HTMLNode(value=" and "),
                HTMLNode(tag="i", children=[HTMLNode(value="italic")]),
                HTMLNode(value=" words inside of it.")
            ]
        ),
        HTMLNode(
            tag="ul",
            children=[
                HTMLNode(
                    tag="li",
                    children=[HTMLNode(value="This is the first list item in a list block")]
                ),
                HTMLNode(
                    tag="li",
                    children=[HTMLNode(value="This is a list item")]
                ),
                HTMLNode(
                    tag="li",
                    children=[HTMLNode(value="This is another list item")]
                )
            ]
        )
    ]
)

markdown_h1 = """# This is a heading"""
markdown_h1_expected = HTMLNode(
    tag="div", children=[
        HTMLNode(
            tag="h1",  
        )
    ]
)

markdown_code = """``` def my_func ```"""
markdown_code_expected = HTMLNode(
    tag="div", children=[
        HTMLNode(
            tag="code", value=" def my_func "  
        )
    ]
)

markdown_ul = """* This is the first list item in a list block
* This is a list item
* This is another list item"""
markdown_ul_expected = HTMLNode(
    tag="div", children=[
        HTMLNode(
            tag="ul", children=[
                HTMLNode(
                    tag="li", value="This is the first list item in a list block"  
                ),
                HTMLNode(
                    tag="li", value="This is a list item"  
                ),
                HTMLNode(
                    tag="li", value="This is another list item"  
                ),
            ]
        )
    ]
)

markdown_ol = """1. This is the first list item in a list block
2. This is a list item
3. This is another list item"""
markdown_ol_expected = HTMLNode(
    tag="div", children=[
        HTMLNode(
            tag="ol", children=[
                HTMLNode(
                    tag="li", value="1. This is the first list item in a list block"  
                ),
                HTMLNode(
                    tag="li", value="2. This is a list item"  
                ),
                HTMLNode(
                    tag="li", value="3. This is another list item"  
                ),
            ]
        )
    ]
)

markdown_quote = """> 123
> 456"""

markdown_quote_expected = HTMLNode(
    tag="div", children=[
        HTMLNode(
            tag="ol", children=[
                HTMLNode(
                    tag="li", value="1. This is the first list item in a list block"  
                ),
                HTMLNode(
                    tag="li", value="2. This is a list item"  
                ),
                HTMLNode(
                    tag="li", value="3. This is another list item"  
                ),
            ]
        )
    ]
)

class Test_Block_to_HTML(unittest.TestCase):
    def test_block_to_HTML_h1(self):
        result = markdown_to_html_node(markdown_h1)
        expected = markdown_h1_expected
        self.assertEqual(result, expected)

    def test_block_to_HTML_code(self):
        result = markdown_to_html_node(markdown_code)
        expected = markdown_code_expected
        self.assertEqual(result, expected)

    def test_block_to_HTML_ul(self):
        result = markdown_to_html_node(markdown_ul)
        expected = markdown_ul_expected
        self.assertEqual(result, expected)
    
    def test_block_to_HTML_ol(self):
        result = markdown_to_html_node(markdown_ol)
        expected = markdown_ol_expected
        self.assertEqual(result, expected)
    
    def test_block_to_HTML_quote(self):
        result = markdown_to_html_node(markdown_quote)
        expected = markdown_quote_expected
        self.assertEqual(result, expected)
