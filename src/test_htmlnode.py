from htmlnode import HTMLNode

def test_props_to_html_empty():
    node = HTMLNode("a", "link text")
    assert node.props_to_html() == ""

def test_props_to_html_single():
    node = HTMLNode("a", "link text", props={"href": "https://google.com"})
    assert node.props_to_html() == ' href="https://google.com"'

def test_props_to_html_multiple():
    node = HTMLNode("a", "link text", props={"href": "https://google.com", "target": "_blank"})
    expected = ' href="https://google.com" target="_blank"'
    assert node.props_to_html() == expected
