#!/usr/bin/env python3
"""
Example usage of LZW compression library
"""

from lzw import compress, decompress, compress_to_binary, decompress_from_binary


def example_basic():
    """Basic compression and decompression example"""
    print("=" * 60)
    print("Example 1: Basic String Compression")
    print("=" * 60)
    
    original = "TOBEORNOTTOBEORTOBEORNOT"
    print(f"Original text: {original}")
    print(f"Original length: {len(original)} characters\n")
    
    # Compress
    compressed = compress(original)
    print(f"Compressed codes: {compressed}")
    print(f"Number of codes: {len(compressed)}\n")
    
    # Decompress
    decompressed = decompress(compressed)
    print(f"Decompressed text: {decompressed}")
    print(f"Match: {original == decompressed}")
    print()


def example_repeated_text():
    """Example with highly repetitive text"""
    print("=" * 60)
    print("Example 2: Highly Repetitive Text")
    print("=" * 60)
    
    original = "banana" * 50
    print(f"Original: '{original[:30]}...' (repeated)")
    print(f"Original length: {len(original)} characters\n")
    
    compressed = compress(original)
    print(f"Compressed codes: {len(compressed)} codes")
    print(f"Compression ratio: {len(original) / len(compressed):.2f}:1")
    
    decompressed = decompress(compressed)
    print(f"Decompression successful: {original == decompressed}")
    print()


def example_real_text():
    """Example with realistic text"""
    print("=" * 60)
    print("Example 3: Realistic Text")
    print("=" * 60)
    
    original = """The quick brown fox jumps over the lazy dog. 
The quick brown fox jumps over the lazy dog again.
The quick brown fox really likes jumping over dogs."""
    
    print(f"Original text:\n{original}\n")
    print(f"Original length: {len(original)} characters\n")
    
    # Binary compression
    binary = compress_to_binary(original)
    print(f"Binary compressed size: {len(binary)} bytes")
    print(f"Compression ratio: {len(original) / len(binary):.2f}:1")
    
    # Calculate space saved or expanded
    change = (1 - len(binary) / len(original)) * 100
    if change > 0:
        print(f"Space saved: {change:.1f}%")
    else:
        print(f"Space expanded: {-change:.1f}%")
    
    decompressed = decompress_from_binary(binary)
    print(f"Decompression successful: {original == decompressed}")
    print()


def example_worst_case():
    """Example showing worst case (random data)"""
    print("=" * 60)
    print("Example 4: Worst Case - Random Characters")
    print("=" * 60)
    
    # Random-looking data with no repetition
    original = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    print(f"Original: {original}")
    print(f"Original length: {len(original)} characters\n")
    
    compressed = compress(original)
    print(f"Compressed codes: {len(compressed)} codes")
    
    # In worst case, compression may not help
    if len(compressed) >= len(original):
        print("Note: No compression achieved (no repeated patterns)")
    else:
        print(f"Compression ratio: {len(original) / len(compressed):.2f}:1")
    
    print()


def example_dictionary_growth():
    """Show how the dictionary grows during compression"""
    print("=" * 60)
    print("Example 5: Dictionary Growth Visualization")
    print("=" * 60)
    
    original = "ABABABABAB"
    print(f"Original: {original}")
    print(f"Compressing step by step:\n")
    
    # Manual step-through to show dictionary growth
    dictionary = {chr(i): i for i in range(256)}
    dict_size = 256
    current_sequence = ""
    result = []
    
    for i, char in enumerate(original):
        new_sequence = current_sequence + char
        if new_sequence in dictionary:
            current_sequence = new_sequence
            print(f"Step {i+1}: Read '{char}' -> Current sequence: '{current_sequence}' (in dict)")
        else:
            print(f"Step {i+1}: Read '{char}' -> Output code for '{current_sequence}': {dictionary[current_sequence]}")
            print(f"        -> Add '{new_sequence}' to dictionary as code {dict_size}")
            result.append(dictionary[current_sequence])
            dictionary[new_sequence] = dict_size
            dict_size += 1
            current_sequence = char
    
    if current_sequence:
        print(f"Step {len(original)+1}: End of input -> Output code for '{current_sequence}': {dictionary[current_sequence]}")
        result.append(dictionary[current_sequence])
    
    print(f"\nFinal compressed codes: {result}")
    print(f"Compression: {len(original)} chars -> {len(result)} codes")
    print()


if __name__ == "__main__":
    example_basic()
    example_repeated_text()
    example_real_text()
    example_worst_case()
    example_dictionary_growth()
    
    print("=" * 60)
    print("All examples completed successfully!")
    print("=" * 60)
