import unittest

from main import *
from htmlnode import *
from textnode import TextNode, TextType
from markdown_func import *
from block_to_html import *

class Test_extract_from_markdown(unittest.TestCase):
    def test_extract_from_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(text)
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(result, expected)

    def test_extract_from_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result = extract_markdown_links(text)
        expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(result, expected)
    
    def test_extract_no_match(self):
        text = "This is text with a link?"
        result = extract_markdown_links(text)
        expected = []
        self.assertEqual(result, expected)

class Test_split_blocks(unittest.TestCase):
    def test_split_blocks(self):
        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.





* This is the first list item in a list block
* This is a list item
* This is another list item"""
        result = markdown_to_blocks(markdown)
        expected = ['# This is a heading', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', '* This is the first list item in a list block\n* This is a list item\n* This is another list item']
        
        self.assertEqual(result, expected)

    def test_split_blocks_no_text(self):
        markdown = ""
        result = markdown_to_blocks(markdown)
        expected = []
        
        self.assertEqual(result, expected)

class Test_block_types(unittest.TestCase):
    def test_block_types_headings(self):
        block = "## Heading 2"
        result = block_to_blocktype(block)
        expected = "heading"
        self.assertEqual(result, expected)

    def test_block_types_heading7(self):
        block = "####### Heading 7?"
        result = block_to_blocktype(block)
        expected = "paragraph"
        self.assertEqual(result, expected)
    
    def test_block_types_code(self):
        block = "``` def my_func ```"
        result = block_to_blocktype(block)
        expected = "code"
        self.assertEqual(result, expected)
    
    def test_block_types_quote(self):
        block = """> 1
> 2"""
        result = block_to_blocktype(block)
        expected = "quote"
        self.assertEqual(result, expected)
    
    def test_block_types_quote_bad(self):
        block = """> 1
    > 2
    d1"""
        result = block_to_blocktype(block)
        expected = "paragraph"
        self.assertEqual(result, expected)
    
    def test_block_types_unordered_list(self):
        block = """- 1
- 2"""
        result = block_to_blocktype(block)
        expected = "unordered_list"
        self.assertEqual(result, expected)
    
    def test_block_types_unordered_list2(self):
        block = """* 1
* 2"""
        result = block_to_blocktype(block)
        expected = "unordered_list"
        self.assertEqual(result, expected)
    
    def test_block_types_unordered_list_bad(self):
        block = """* 1
1* 2"""
        result = block_to_blocktype(block)
        expected = "paragraph"
        self.assertEqual(result, expected)
    
    def test_block_types_ordered_list(self):
        block = """1. a
2. b"""
        result = block_to_blocktype(block)
        expected = "ordered_list"
        self.assertEqual(result, expected)

    def test_block_types_ordered_list_bad(self):
        block = """1. a
3. b"""
        result = block_to_blocktype(block)
        expected = "paragraph"
        self.assertEqual(result, expected)

class Test_extract_title(unittest.TestCase):
    def test_extract_title(self):
        md_str = "# Hello"
        result = extract_title(md_str)
        expected = "Hello"
        self.assertEqual(result, expected)
    def test_extract_title_longer(self):
        md_str = "131231\n   # Hello"
        result = extract_title(md_str)
        expected = "Hello"
        self.assertEqual(result, expected)
