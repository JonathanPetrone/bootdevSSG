from textnode import *

def main():
    print("hello world")

    testNode = TextNode("hej", TextType.Normal_text, "www.sf.se")
    testNode2 = TextNode("hej", TextType.Normal_text, "www.sf.se")
    testNode3 = TextNode("hej2", TextType.Bold_text)

    print(testNode == testNode3)

    print(testNode, testNode2, testNode3)
main()