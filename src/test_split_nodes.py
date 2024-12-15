import unittest

from main import *
from htmlnode import *
from textnode import TextNode, TextType

class TestConvert_TextNode_to_HTMLNode_toHTML(unittest.TestCase):
    def test_split_old_nodes_without_delimiter_text(self):
        node = TextNode("This is text word", TextType.Normal_text)
        new_node_list = split_nodes_delimiter([node], "`", TextType.Code_text)
        expected = [TextNode("This is text word", TextType.Normal_text)]
        self.assertEqual(new_node_list, expected)

    def test_split_old_nodes_with_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.Normal_text)
        new_node_list = split_nodes_delimiter([node], "`", TextType.Code_text)
        expected = [TextNode("This is text with a ", TextType.Normal_text), TextNode("code block", TextType.Code_text), TextNode(" word", TextType.Normal_text)]
        self.assertEqual(new_node_list, expected)

    def test_split_old_nodes_with_incorrect_delimiter(self):
        with self.assertRaises(Exception) as context:
            node = TextNode("This is text with a `code block` word", TextType.Normal_text)
            split_nodes_delimiter([node], "1", TextType.Code_text)
       
        self.assertEqual(str(context.exception), "that's invalid Markdown syntax")