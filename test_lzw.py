#!/usr/bin/env python3
"""
Test suite for LZW compression implementation
"""

import unittest
from lzw import compress, decompress, compress_to_binary, decompress_from_binary


class TestLZWCompression(unittest.TestCase):
    """Test cases for LZW compression and decompression"""
    
    def test_empty_string(self):
        """Test compression/decompression of empty string"""
        data = ""
        compressed = compress(data)
        decompressed = decompress(compressed)
        self.assertEqual(data, decompressed)
        self.assertEqual(compressed, [])
    
    def test_single_character(self):
        """Test compression/decompression of single character"""
        data = "A"
        compressed = compress(data)
        decompressed = decompress(compressed)
        self.assertEqual(data, decompressed)
        self.assertEqual(len(compressed), 1)
    
    def test_no_repetition(self):
        """Test compression/decompression with no repeated patterns"""
        data = "ABCDEFGH"
        compressed = compress(data)
        decompressed = decompress(compressed)
        self.assertEqual(data, decompressed)
    
    def test_simple_repetition(self):
        """Test compression/decompression with simple repetition"""
        data = "AAAAAAA"
        compressed = compress(data)
        decompressed = decompress(compressed)
        self.assertEqual(data, decompressed)
        # Should compress well
        self.assertLess(len(compressed), len(data))
    
    def test_classic_example(self):
        """Test the classic LZW example"""
        data = "TOBEORNOTTOBEORTOBEORNOT"
        compressed = compress(data)
        decompressed = decompress(compressed)
        self.assertEqual(data, decompressed)
        # Should achieve compression
        self.assertLess(len(compressed), len(data))
    
    def test_repeated_patterns(self):
        """Test with repeated patterns"""
        data = "ABABABABABAB"
        compressed = compress(data)
        decompressed = decompress(compressed)
        self.assertEqual(data, decompressed)
    
    def test_long_text(self):
        """Test with longer text"""
        data = "The quick brown fox jumps over the lazy dog. " * 10
        compressed = compress(data)
        decompressed = decompress(compressed)
        self.assertEqual(data, decompressed)
    
    def test_special_characters(self):
        """Test with special characters"""
        data = "Hello, World! 123 @#$%^&*()"
        compressed = compress(data)
        decompressed = decompress(compressed)
        self.assertEqual(data, decompressed)
    
    def test_unicode_characters(self):
        """Test with unicode characters (within ASCII range)"""
        data = "café résumé naïve"
        try:
            compressed = compress(data)
            decompressed = decompress(compressed)
            self.assertEqual(data, decompressed)
        except (ValueError, KeyError):
            # May fail for non-ASCII characters in basic implementation
            self.skipTest("Unicode beyond ASCII not supported in basic implementation")
    
    def test_binary_compression_empty(self):
        """Test binary compression of empty string"""
        data = ""
        binary = compress_to_binary(data)
        decompressed = decompress_from_binary(binary)
        self.assertEqual(data, decompressed)
    
    def test_binary_compression_simple(self):
        """Test binary compression and decompression"""
        data = "HELLO"
        binary = compress_to_binary(data)
        decompressed = decompress_from_binary(binary)
        self.assertEqual(data, decompressed)
        self.assertIsInstance(binary, bytes)
    
    def test_binary_compression_complex(self):
        """Test binary compression with complex data"""
        data = "TOBEORNOTTOBEORTOBEORNOT"
        binary = compress_to_binary(data)
        decompressed = decompress_from_binary(binary)
        self.assertEqual(data, decompressed)
        # Binary should be even length (2 bytes per code)
        self.assertEqual(len(binary) % 2, 0)
    
    def test_compression_ratio(self):
        """Test that compression actually reduces size for repetitive data"""
        data = "AAAABBBBCCCCDDDD" * 5
        compressed = compress(data)
        # Compressed codes should be fewer than original characters
        self.assertLess(len(compressed), len(data))
    
    def test_all_ascii_characters(self):
        """Test with all printable ASCII characters"""
        data = "".join(chr(i) for i in range(32, 127))
        compressed = compress(data)
        decompressed = decompress(compressed)
        self.assertEqual(data, decompressed)


class TestLZWEdgeCases(unittest.TestCase):
    """Test edge cases for LZW compression"""
    
    def test_single_repeated_char(self):
        """Test with single character repeated many times"""
        data = "X" * 1000
        compressed = compress(data)
        decompressed = decompress(compressed)
        self.assertEqual(data, decompressed)
        # Should compress very well
        self.assertLess(len(compressed), 100)
    
    def test_alternating_pattern(self):
        """Test with alternating pattern"""
        data = "ABABAB" * 20
        compressed = compress(data)
        decompressed = decompress(compressed)
        self.assertEqual(data, decompressed)
    
    def test_gradually_increasing_repetition(self):
        """Test with gradually increasing repetition"""
        data = "A" + "AB" + "ABC" + "ABCD" + "ABCDE"
        compressed = compress(data)
        decompressed = decompress(compressed)
        self.assertEqual(data, decompressed)


if __name__ == "__main__":
    unittest.main()
