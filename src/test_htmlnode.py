import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_props_to_string(self):
        HTMLnode = HTMLNode("h1", "Header",["p"], {"style": "text-align:center", "color": "blue"} )
        str_props = HTMLnode.props_to_html()
        correct_str = 'style="text-align:center" color="blue"'
        self.assertEqual(str_props, correct_str)
    
    def test_props_to_string_empty(self):
        HTMLnode = HTMLNode("h1", "Header",["p"], {} )
        str_props = HTMLnode.props_to_html()
        correct_str = ''
        self.assertEqual(str_props, correct_str)

    def test_props_to_string_noneValue(self):
        HTMLnode = HTMLNode("h1", "Header",["p"], {"style": None} )
        str_props = HTMLnode.props_to_html()
        correct_str = 'style="None"'
        self.assertEqual(str_props, correct_str)

class TestLeafNode(unittest.TestCase):
    def test_leaf_node(self):
        Leafnode = LeafNode("p", "this is a paragraph")
        str_html = Leafnode.to_html()
        correct_str = '<p>this is a paragraph</p>'
        self.assertEqual(str_html, correct_str)
    
    def test_leaf_node_prop(self):
        Leafnode = LeafNode("a", "click me", {"href": "https://www.google.com"})
        str_html = Leafnode.to_html()
        correct_str = '<a href="https://www.google.com">click me</a>'
        self.assertEqual(str_html, correct_str)
    
    def test_leaf_node_minimum(self):
        Leafnode = LeafNode(None, "click me")
        str_html = Leafnode.to_html()
        correct_str = 'click me'
        self.assertEqual(str_html, correct_str)

class TestParentNode(unittest.TestCase):
    def test_parent_node(self):
        node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )
        str_html = node.to_html()
        correct_str = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(str_html, correct_str)
    
    def test_parent_node_nested_parent(self):
        node = ParentNode(
        "div",
        [
            ParentNode("p", [
                LeafNode("b", "Bold text", {"color": "blue"}),
                LeafNode(None, "Normal text")
            ]),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )
        str_html = node.to_html()
        correct_str = '<div><p><b color="blue">Bold text</b>Normal text</p><i>italic text</i>Normal text</div>'
        self.assertEqual(str_html, correct_str)
    
    def test_parent_node_no_tag_with_props(self):
        def test_no_tag_with_props_raises_value_error(self):
            with self.assertRaises(ValueError) as context:
                LeafNode(None, "Some value", {"color": "red"})

            self.assertEqual(str(context.exception), "Props cannot be associated with an element without a tag.")

if __name__ == "__main__":
    unittest.main()