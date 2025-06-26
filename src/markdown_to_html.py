from htmlnode import ParentNode
from block import block_to_block_type, BlockType
from markdown import markdown_to_blocks
from parser import text_to_children
from converter import text_node_to_html_node
from leafnode import LeafNode
from textnode import TextNode, TextType

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            cleaned_block = block.replace("\n", " ")
            children.append(
                ParentNode("p", text_to_children(cleaned_block))
            )
        elif block_type == BlockType.HEADING:
            level = block.count("#", 0, block.find(" "))
            content = block[level + 1:].strip()
            children.append(
                ParentNode(f"h{level}", text_to_children(content))
            )
        elif block_type == BlockType.CODE:
            content = "\n".join(block.split("\n")[1:-1]) + "\n"
            text_node = text_node_to_html_node(TextNode(content, TextType.TEXT))
            children.append(
                ParentNode("pre", [ParentNode("code", [text_node])])
            )
        elif block_type == BlockType.QUOTE:
            cleaned = "\n".join([line.lstrip("> ").strip() for line in block.split("\n")])
            children.append(
                ParentNode("blockquote", text_to_children(cleaned))
            )
        elif block_type == BlockType.UNORDERED_LIST:
            items = [line.lstrip("- ").strip() for line in block.split("\n")]
            li_nodes = [ParentNode("li", text_to_children(item)) for item in items]
            children.append(
                ParentNode("ul", li_nodes)
            )
        elif block_type == BlockType.ORDERED_LIST:
            items = [line[line.find(". ") + 2:].strip() for line in block.split("\n")]
            li_nodes = [ParentNode("li", text_to_children(item)) for item in items]
            children.append(
                ParentNode("ol", li_nodes)
            )

    return ParentNode("div", children)
