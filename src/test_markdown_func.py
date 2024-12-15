import unittest

from main import *
from htmlnode import *
from textnode import TextNode, TextType
from markdown_func import *

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
    
        