import unittest
from extractor import extract_markdown_images, extract_markdown_links

class TestMarkdownExtraction(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "Text with ![img1](https://example.com/img1.png) and ![img2](https://example.com/img2.png)"
        )
        expected = [
            ("img1", "https://example.com/img1.png"),
            ("img2", "https://example.com/img2.png")
        ]
        self.assertListEqual(matches, expected)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "Text with [link1](https://example.com) and [link2](https://google.com)"
        )
        expected = [
            ("link1", "https://example.com"),
            ("link2", "https://google.com")
        ]
        self.assertListEqual(matches, expected)

if __name__ == "__main__":
    unittest.main()

