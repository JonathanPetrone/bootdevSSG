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

markdown_1_expected = HTMLNode("div", None, [
    HTMLNode("h1", None, [
        HTMLNode(None, "This is a heading", [], None)
    ], None),
    HTMLNode("p", None, [
        HTMLNode(None, "This is a paragraph of text. It has some ", [], None),
        HTMLNode("b", "bold", [], None),
        HTMLNode(None, " and ", [], None),
        HTMLNode("i", "italic", [], None),
        HTMLNode(None, " words inside of it.", [], None)
    ], None),
    HTMLNode("ul", None, [
        HTMLNode("li", None, [HTMLNode(None, "This is the first list item in a list block", [], None)], None),
        HTMLNode("li", None, [HTMLNode(None, "This is a list item", [], None)], None),
        HTMLNode("li", None, [HTMLNode(None, "This is another list item", [], None)], None)
    ], None)
])

markdown_h3 = """### This is a heading"""
markdown_h3_expected = HTMLNode(
    "div",
    None,
    [
        HTMLNode(
            "h3", 
            None,
            [
                HTMLNode(None, "This is a heading", [], None)
            ],
            None
        )
    ],
    None
)

markdown_code = """``` def my_func ```"""
markdown_code_expected = HTMLNode(
    tag="div", children=[
        HTMLNode(
            tag="pre", children=[
                HTMLNode(tag="code", value=" def my_func ")
            ]   
        )
    ]
)

markdown_ul = """* This is the first list item in a list block
* This is a list item
* This is another list item"""
markdown_ul_expected = HTMLNode(
    "div",
    None,
    [
        HTMLNode("ul", None, [
            HTMLNode("li", None, [HTMLNode(None, "This is the first list item in a list block", [], None)], None),
            HTMLNode("li", None, [HTMLNode(None, "This is a list item", [], None)], None),
            HTMLNode("li", None, [HTMLNode(None, "This is another list item", [], None)], None)
        ], None)
    ],
    None
)

markdown_ol = """1. This is the first list item in a list block
2. This is a list item
3. This is another list item"""
markdown_ol_expected = HTMLNode(
    "div", 
    None, 
    [
        HTMLNode("ol", None, [
            HTMLNode("li", None, [HTMLNode(None, "This is the first list item in a list block", [], None)], None),
            HTMLNode("li", None, [HTMLNode(None, "This is a list item", [], None)], None),
            HTMLNode("li", None, [HTMLNode(None, "This is another list item", [], None)], None)
        ], None)
    ], 
    None
)

markdown_quote = """> 123
> 456"""

markdown_quote_expected = HTMLNode(
    "div",
    None,
    [
        HTMLNode("blockquote", None, [
            HTMLNode(None, "123 456", [], None)
        ], None)
    ],
    None
)

class Test_Block_to_HTML(unittest.TestCase):
    def test_block_to_HTML_h3(self):
        result = markdown_to_html_node(markdown_h3)
        expected = markdown_h3_expected
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

    def test_block_to_HTML_full(self):
        result = markdown_to_html_node(markdown_1)
        expected = markdown_1_expected
        self.assertEqual(result, expected)
