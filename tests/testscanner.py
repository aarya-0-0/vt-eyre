import unittest
from vt_eyre.scanner import scan_url, scan_file

class TestScanner(unittest.TestCase):

    def test_invalid_url(self):
        result = scan_url("invalid-url.com")
        self.assertIsNotNone(result)

    def test_file_not_found(self):
        result = scan_file("nonexistent.txt")
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
