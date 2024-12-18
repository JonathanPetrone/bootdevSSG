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

class Test_split_nodes_images_links(unittest.TestCase):
    def test_split_old_nodes_with_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.Normal_text,
        )
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("This is text with a link ", TextType.Normal_text),
            TextNode("to boot dev", TextType.Links, "https://www.boot.dev"),
            TextNode(" and ", TextType.Normal_text),
            TextNode(
            "to youtube", TextType.Links, "https://www.youtube.com/@bootdotdev"
            ),
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_old_nodes_with_images(self):
        node = TextNode(
        "Multiple images ![first](1.png) between ![second](2.png) text",
        TextType.Normal_text
        )
        new_nodes = split_nodes_image([node])
        expected = [TextNode("Multiple images ", TextType.Normal_text),
            TextNode("first", TextType.Images, "1.png"),
            TextNode(" between ", TextType.Normal_text),
            TextNode("second", TextType.Images, "2.png"), 
            TextNode(" text", TextType.Normal_text)
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_old_nodes_with_images_no_image(self):
        node = TextNode("just plain text", TextType.Normal_text)
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("just plain text", TextType.Normal_text)
        ]
        self.assertEqual(new_nodes, expected)

class Test_text_to_textnodes(unittest.TestCase):
    def test_example_text_to_textnode(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.Normal_text),
            TextNode("text", TextType.Bold_text),
            TextNode(" with an ", TextType.Normal_text),
            TextNode("italic", TextType.Italic_text),
            TextNode(" word and a ", TextType.Normal_text),
            TextNode("code block", TextType.Code_text),
            TextNode(" and an ", TextType.Normal_text),
            TextNode("obi wan image", TextType.Images, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.Normal_text),
            TextNode("link", TextType.Links, "https://boot.dev"),
        ]

        self.assertEqual(result, expected)

    def test_empty_text_to_textnode(self):
        text = ""
        result = text_to_textnodes(text)
        expected = []

        self.assertEqual(result, expected)

