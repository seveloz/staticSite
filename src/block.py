from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block):
    lines = block.strip().split("\n")

    # Code block: starts and ends with ```
    if lines[0].strip().startswith("```") and lines[-1].strip().endswith("```"):
        return BlockType.CODE

    # Heading: starts with 1-6 # followed by a space
    if re.match(r"^#{1,6} ", lines[0]):
        return BlockType.HEADING

    # Quote: all lines start with >
    if all(line.strip().startswith(">") for line in lines):
        return BlockType.QUOTE

    # Unordered list: all lines start with "- "
    if all(line.strip().startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    # Ordered list: lines start with incrementing numbers like "1. ", "2. ", etc.
    ordered = True
    for i, line in enumerate(lines):
        expected_prefix = f"{i + 1}. "
        if not line.strip().startswith(expected_prefix):
            ordered = False
            break
    if ordered:
        return BlockType.ORDERED_LIST

    # Default: paragraph
    return BlockType.PARAGRAPH
