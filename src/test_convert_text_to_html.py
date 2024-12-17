import unittest

from main import *
from htmlnode import *
from textnode import TextNode, TextType
from block_to_html import *

normalTextNode = TextNode("this is normal text", TextType.Normal_text)
boldTextNode = TextNode("this is bold text", TextType.Bold_text)
italicTextNode = TextNode("this is italic text", TextType.Italic_text)
codeTextNode =  TextNode("this is code text", TextType.Code_text)
linkTextNode =  TextNode("this is a link text", TextType.Links, "www.link.com")
imageTextNode = TextNode("this is a text for the image", TextType.Images, "www.img.com")
brokenTextNode = TextNode("this is a text", "oops", "www.oops.com")

#LeafNode("b", "Bold text", {"color": "blue"}),

class TestConvert_TextNode_to_HTMLNode_toHTML(unittest.TestCase):
    def test_convert_normal_text_to_html(self):
        result = text_node_to_html_node(normalTextNode)
        result = result.to_html()
        expected = HTMLNode(None,"this is normal text",None).to_html()
        self.assertEqual(result, expected)

    def test_convert_bold_text_to_html(self):
        result = text_node_to_html_node(boldTextNode)
        result = result.to_html()
        expected = HTMLNode("b","this is bold text",None).to_html()
        self.assertEqual(result, expected)

    def test_convert_italic_text_to_html(self):
        result = text_node_to_html_node(italicTextNode)
        result = result.to_html()
        expected = HTMLNode("i","this is italic text",None).to_html()
        self.assertEqual(result, expected)

    def test_convert_code_text_to_html(self):
        result = text_node_to_html_node(codeTextNode)
        result = result.to_html()
        expected = HTMLNode("code","this is code text",None).to_html()
        self.assertEqual(result, expected)

    def test_convert_link_text_to_html(self):
        result = text_node_to_html_node(linkTextNode)
        result = result.to_html()
        expected = HTMLNode("a","this is a link text",{"href": "www.link.com"}).to_html()
        self.assertEqual(result, expected)

    def test_convert_image_text_to_html(self):
        result = text_node_to_html_node(imageTextNode)
        result = result.to_html()
        expected = HTMLNode("img", "",{"src": "www.img.com", "alt": "this is a text for the image"}).to_html()
        self.assertEqual(result, expected)

    def test_convert_broken_text_to_html(self):
        def test_convert_broken_text_to_html_raises_value_error(self):
            with self.assertRaises(ValueError) as context:
                brokenTextNode

            self.assertEqual(str(context.exception), "Props cannot be associated with an element without a tag.")
