#!/usr/bin/env python3
"""
LZW Compression Implementation

This module implements the Lempel-Ziv-Welch (LZW) compression algorithm.
LZW is a universal lossless data compression algorithm that builds a dictionary
of input sequences on the fly during compression.
"""


def compress(data):
    """
    Compress data using LZW algorithm.
    
    Args:
        data (str): The string data to compress
        
    Returns:
        list: A list of integer codes representing the compressed data
    """
    if not data:
        return []
    
    # Initialize dictionary with single character strings
    dictionary = {chr(i): i for i in range(256)}
    dict_size = 256
    
    result = []
    current_sequence = ""
    
    for char in data:
        new_sequence = current_sequence + char
        if new_sequence in dictionary:
            current_sequence = new_sequence
        else:
            # Output the code for current_sequence
            result.append(dictionary[current_sequence])
            # Add new sequence to dictionary
            dictionary[new_sequence] = dict_size
            dict_size += 1
            current_sequence = char
    
    # Output the code for the last sequence
    if current_sequence:
        result.append(dictionary[current_sequence])
    
    return result


def decompress(compressed_data):
    """
    Decompress LZW compressed data.
    
    Args:
        compressed_data (list): A list of integer codes from compression
        
    Returns:
        str: The decompressed string data
    """
    if not compressed_data:
        return ""
    
    # Initialize dictionary with single character strings
    dictionary = {i: chr(i) for i in range(256)}
    dict_size = 256
    
    # Get first code and output its string
    code = compressed_data[0]
    current_sequence = dictionary[code]
    result = [current_sequence]
    
    for code in compressed_data[1:]:
        if code in dictionary:
            entry = dictionary[code]
        elif code == dict_size:
            # Special case: code not in dictionary yet
            entry = current_sequence + current_sequence[0]
        else:
            raise ValueError(f"Invalid compressed code: {code}")
        
        result.append(entry)
        
        # Add new sequence to dictionary
        dictionary[dict_size] = current_sequence + entry[0]
        dict_size += 1
        
        current_sequence = entry
    
    return "".join(result)


def compress_to_binary(data):
    """
    Compress data and convert to binary format for storage.
    
    Args:
        data (str): The string data to compress
        
    Returns:
        bytes: Binary representation of compressed data
    """
    compressed = compress(data)
    # Convert list of integers to bytes
    # Using variable-length encoding for efficiency
    result = []
    for code in compressed:
        # Simple encoding: use 2 bytes per code (supports up to 65536 codes)
        result.append((code >> 8) & 0xFF)
        result.append(code & 0xFF)
    return bytes(result)


def decompress_from_binary(binary_data):
    """
    Decompress binary data back to original string.
    
    Args:
        binary_data (bytes): Binary compressed data
        
    Returns:
        str: The decompressed string data
    """
    if not binary_data:
        return ""
    
    # Convert bytes back to list of integers
    compressed = []
    for i in range(0, len(binary_data), 2):
        code = (binary_data[i] << 8) | binary_data[i + 1]
        compressed.append(code)
    
    return decompress(compressed)


if __name__ == "__main__":
    # Example usage
    original = "TOBEORNOTTOBEORTOBEORNOT"
    print(f"Original: {original}")
    print(f"Original length: {len(original)} characters")
    
    # Compress
    compressed = compress(original)
    print(f"\nCompressed: {compressed}")
    print(f"Compressed length: {len(compressed)} codes")
    
    # Decompress
    decompressed = decompress(compressed)
    print(f"\nDecompressed: {decompressed}")
    print(f"Match: {original == decompressed}")
    
    # Binary compression
    binary = compress_to_binary(original)
    print(f"\nBinary compressed size: {len(binary)} bytes")
    print(f"Compression ratio: {len(original) / len(binary):.2f}:1")
    
    # Binary decompression
    decompressed_from_binary = decompress_from_binary(binary)
    print(f"Binary decompression match: {original == decompressed_from_binary}")
