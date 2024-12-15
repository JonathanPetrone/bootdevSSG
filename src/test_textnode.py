import unittest

from textnode import TextNode, TextType



class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.Bold_text)
        node2 = TextNode("This is a text node", TextType.Bold_text)
        self.assertEqual(node, node2)
    
    def test_eq_diff_url(self):
        node = TextNode("This is a text node", TextType.Bold_text)
        node2 = TextNode("This is a text node", TextType.Bold_text, "www.boot.dev")
        self.assertNotEqual(node, node2)
    
    def test_eq_diff_text(self):
        node = TextNode("This is a text node", TextType.Bold_text)
        node2 = TextNode("This is a text node haha", TextType.Bold_text)
        self.assertNotEqual(node, node2)

    def test_eq_diff_text_type(self):
        node = TextNode("This is a text node", TextType.Bold_text)
        node2 = TextNode("This is a text node", TextType.Normal_text)
        self.assertNotEqual(node, node2)   


if __name__ == "__main__":
    unittest.main()
