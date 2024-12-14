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



if __name__ == "__main__":
    unittest.main()