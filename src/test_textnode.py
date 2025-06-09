import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        node_one = TextNode("Hola mundo", TextType.TEXT)
        node_two = TextNode("Hola mundos", TextType.ITALIC)
        self.assertNotEqual(node_one, node_two)

    def test_url(self):
        url_test =TextNode("Prueba url", TextType.LINK)
        self.assertEqual(url_test.url, None)


if __name__ == "__main__":
    unittest.main()
