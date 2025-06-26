import unittest
from generator import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_valid_title(self):
        md = "# Welcome to My Page"
        self.assertEqual(extract_title(md), "Welcome to My Page")

    def test_whitespace(self):
        md = "#   Hello World   "
        self.assertEqual(extract_title(md), "Hello World")

    def test_missing_title(self):
        with self.assertRaises(Exception):
            extract_title("## Subtitle\nContent here")

if __name__ == "__main__":
    unittest.main()
