# LZW Compression

A Python implementation of the Lempel-Ziv-Welch (LZW) compression algorithm. This is an isolated experimental project designed to implement LZW compression for integration into larger projects.

## Overview

LZW is a universal lossless data compression algorithm created by Abraham Lempel, Jacob Ziv, and Terry Welch. It works by building a dictionary of repeated patterns in the data as it processes the input, replacing these patterns with shorter codes.

## Features

- **Pure Python implementation** - No external dependencies required
- **Simple API** - Easy to integrate into other projects
- **Command-line interface** - Compress and decompress files directly
- **Comprehensive test suite** - 17 test cases covering various scenarios
- **Binary compression support** - Save compressed data to files

## Installation

No installation required! Just clone the repository:

```bash
git clone https://github.com/WEREMSOFT/lzw-compression.git
cd lzw-compression
```

## Usage

### As a Python Module

```python
from lzw import compress, decompress, compress_to_binary, decompress_from_binary

# Compress a string
original = "TOBEORNOTTOBEORTOBEORNOT"
compressed = compress(original)
print(f"Compressed: {compressed}")

# Decompress back to original
decompressed = decompress(compressed)
print(f"Decompressed: {decompressed}")
assert original == decompressed

# Binary compression for file storage
binary_data = compress_to_binary(original)
with open("compressed.lzw", "wb") as f:
    f.write(binary_data)

# Binary decompression
with open("compressed.lzw", "rb") as f:
    binary_data = f.read()
restored = decompress_from_binary(binary_data)
assert original == restored
```

### Command-Line Interface

Compress a file:
```bash
python lzw_cli.py compress input.txt output.lzw
```

Decompress a file:
```bash
python lzw_cli.py decompress output.lzw restored.txt
```

### Example with Sample File

Try it out with the included sample file:
```bash
# Compress
python lzw_cli.py compress sample.txt sample.lzw

# Decompress
python lzw_cli.py decompress sample.lzw sample_restored.txt

# Verify they match
diff sample.txt sample_restored.txt
```

## API Reference

### `compress(data: str) -> list`
Compress a string into a list of integer codes.

**Parameters:**
- `data` (str): The string to compress

**Returns:**
- `list`: A list of integer codes representing the compressed data

### `decompress(compressed_data: list) -> str`
Decompress a list of codes back to the original string.

**Parameters:**
- `compressed_data` (list): List of integer codes from compression

**Returns:**
- `str`: The decompressed string

### `compress_to_binary(data: str) -> bytes`
Compress a string and convert to binary format for file storage.

**Parameters:**
- `data` (str): The string to compress

**Returns:**
- `bytes`: Binary representation of compressed data

### `decompress_from_binary(binary_data: bytes) -> str`
Decompress binary data back to the original string.

**Parameters:**
- `binary_data` (bytes): Binary compressed data

**Returns:**
- `str`: The decompressed string

## How LZW Works

1. **Initialize Dictionary**: Start with a dictionary containing all single-character strings
2. **Compression**: 
   - Read characters and build sequences
   - When a new sequence is found, output the code for the previous sequence
   - Add the new sequence to the dictionary
   - Continue with the next character
3. **Decompression**:
   - Start with the same initial dictionary
   - Read codes and output their corresponding strings
   - Rebuild the dictionary by adding sequences based on the pattern

## Testing

Run the comprehensive test suite:
```bash
python test_lzw.py -v
```

The test suite includes:
- Empty string handling
- Single character compression
- Repeated patterns
- Long text compression
- Special characters
- Binary compression/decompression
- Edge cases

## Performance Characteristics

- **Best Case**: Highly repetitive data (e.g., "AAAA...") can achieve excellent compression ratios
- **Worst Case**: Random data with no patterns may result in expansion rather than compression
- **Typical Use**: Text files with repeated words and phrases show good compression

## Limitations

- Currently optimized for ASCII text (characters 0-255)
- Uses 2-byte encoding for codes (supports up to 65,536 dictionary entries)
- Not optimized for binary data or very large files

## Integration with Other Projects

This implementation is designed to be easily integrated into other projects:

1. Copy `lzw.py` to your project
2. Import the functions you need:
   ```python
   from lzw import compress, decompress
   ```
3. Use the compression functions in your code

## Contributing

This is an experimental project. Feel free to fork and modify for your needs.

## License

This is an open-source experimental project. Use freely for your own projects.

## References

- [LZW Compression on Wikipedia](https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch)
- Original paper: Welch, Terry A. "A Technique for High-Performance Data Compression." Computer 17.6 (1984): 8-19.