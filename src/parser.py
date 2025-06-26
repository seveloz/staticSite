from textnode import TextNode, TextType
from converter import text_node_to_html_node
from splitter import (
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
)

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    
    # 1. Imágenes
    nodes = split_nodes_image(nodes)

    # 2. Links
    nodes = split_nodes_link(nodes)

    # 3. Código inline con backticks
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

    # 4. Bold con **
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)

    # 5. Italic con _
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)

    return nodes


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(n) for n in text_nodes]
