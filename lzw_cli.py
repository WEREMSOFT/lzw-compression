#!/usr/bin/env python3
"""
Command-line interface for LZW compression
"""

import argparse
import sys
from lzw import compress_to_binary, decompress_from_binary


def compress_file(input_path, output_path):
    """
    Compress a file using LZW algorithm.
    
    Args:
        input_path (str): Path to input file
        output_path (str): Path to output compressed file
    """
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            data = f.read()
        
        compressed = compress_to_binary(data)
        
        with open(output_path, 'wb') as f:
            f.write(compressed)
        
        original_size = len(data)
        compressed_size = len(compressed)
        ratio = original_size / compressed_size if compressed_size > 0 else 0
        
        print(f"Compression complete!")
        print(f"Original size: {original_size} bytes")
        print(f"Compressed size: {compressed_size} bytes")
        print(f"Compression ratio: {ratio:.2f}:1")
        print(f"Space saved: {((1 - compressed_size/original_size) * 100):.1f}%")
        
    except FileNotFoundError:
        print(f"Error: Input file '{input_path}' not found", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error during compression: {e}", file=sys.stderr)
        sys.exit(1)


def decompress_file(input_path, output_path):
    """
    Decompress a LZW compressed file.
    
    Args:
        input_path (str): Path to compressed file
        output_path (str): Path to output decompressed file
    """
    try:
        with open(input_path, 'rb') as f:
            compressed = f.read()
        
        decompressed = decompress_from_binary(compressed)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(decompressed)
        
        print(f"Decompression complete!")
        print(f"Compressed size: {len(compressed)} bytes")
        print(f"Decompressed size: {len(decompressed)} bytes")
        
    except FileNotFoundError:
        print(f"Error: Input file '{input_path}' not found", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error during decompression: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    """Main entry point for CLI"""
    parser = argparse.ArgumentParser(
        description='LZW Compression Tool - Compress and decompress files using LZW algorithm',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Compress a file
  python lzw_cli.py compress input.txt output.lzw
  
  # Decompress a file
  python lzw_cli.py decompress output.lzw restored.txt
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Command to execute')
    subparsers.required = True
    
    # Compress command
    compress_parser = subparsers.add_parser('compress', help='Compress a file')
    compress_parser.add_argument('input', help='Input file to compress')
    compress_parser.add_argument('output', help='Output compressed file')
    
    # Decompress command
    decompress_parser = subparsers.add_parser('decompress', help='Decompress a file')
    decompress_parser.add_argument('input', help='Input compressed file')
    decompress_parser.add_argument('output', help='Output decompressed file')
    
    args = parser.parse_args()
    
    if args.command == 'compress':
        compress_file(args.input, args.output)
    elif args.command == 'decompress':
        decompress_file(args.input, args.output)


if __name__ == "__main__":
    main()
