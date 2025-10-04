# Integration Guide

This guide shows how to integrate the LZW compression into your project, particularly for LLM-related applications.

## Quick Integration

### Option 1: Copy the Module

Simply copy `lzw.py` into your project:

```bash
# From your project directory
cp /path/to/lzw-compression/lzw.py ./your_project/
```

Then import and use:

```python
from lzw import compress, decompress

# Compress some text
text = "Your data here"
compressed = compress(text)

# Later, decompress it
original = decompress(compressed)
```

### Option 2: Use as a Submodule

Add this repository as a git submodule:

```bash
git submodule add https://github.com/WEREMSOFT/lzw-compression.git
```

Then import from the submodule:

```python
from lzw_compression.lzw import compress, decompress
```

## Use Cases for LLM Projects

### 1. Compressing Training Data

```python
from lzw import compress_to_binary, decompress_from_binary
import json

# Save compressed training data
training_data = json.dumps(your_training_data)
compressed = compress_to_binary(training_data)

with open('training_data.lzw', 'wb') as f:
    f.write(compressed)

# Load and decompress later
with open('training_data.lzw', 'rb') as f:
    compressed = f.read()

training_data = json.loads(decompress_from_binary(compressed))
```

### 2. Caching Tokenized Text

```python
from lzw import compress, decompress

# Compress tokenized sequences
tokens = "token1 token2 token3 " * 100
compressed_tokens = compress(tokens)

# Store compressed tokens (takes less memory)
cache[key] = compressed_tokens

# Later, decompress when needed
original_tokens = decompress(cache[key])
```

### 3. Reducing Model Context Size

```python
from lzw import compress, decompress

class CompressedContext:
    """Store LLM context with compression"""
    
    def __init__(self):
        self.compressed_history = []
    
    def add_message(self, message):
        """Add message to context with compression"""
        compressed = compress(message)
        self.compressed_history.append(compressed)
    
    def get_full_context(self):
        """Get full decompressed context"""
        return [decompress(msg) for msg in self.compressed_history]
    
    def memory_size(self):
        """Get compressed memory size"""
        return sum(len(msg) for msg in self.compressed_history)

# Usage
context = CompressedContext()
context.add_message("User: Hello")
context.add_message("Assistant: Hi there!")
print(f"Memory used: {context.memory_size()} codes")
```

### 4. Storing Embeddings as Text

```python
from lzw import compress_to_binary, decompress_from_binary
import json

# Convert embeddings to string and compress
embeddings = [0.1, 0.2, 0.3, ...]  # Your embedding vector
embedding_str = json.dumps(embeddings)
compressed = compress_to_binary(embedding_str)

# Save to file or database
with open('embeddings.lzw', 'wb') as f:
    f.write(compressed)

# Load later
with open('embeddings.lzw', 'rb') as f:
    compressed = f.read()
embeddings = json.loads(decompress_from_binary(compressed))
```

### 5. Compressing Prompt Templates

```python
from lzw import compress, decompress

# Store prompt templates compressed
PROMPTS = {
    'summarize': compress("Please summarize the following text: {text}"),
    'translate': compress("Translate this to {language}: {text}"),
    'analyze': compress("Analyze the sentiment of: {text}")
}

# Use when needed
def get_prompt(template_name, **kwargs):
    template = decompress(PROMPTS[template_name])
    return template.format(**kwargs)

# Usage
prompt = get_prompt('summarize', text="Long text here...")
```

## Performance Considerations

### When to Use LZW

✅ **Good for:**
- Repetitive text (logs, repeated phrases)
- Template-based content
- Tokenized sequences with patterns
- Storage of historical context
- Caching intermediate results

❌ **Not ideal for:**
- Random data with no patterns
- Already compressed data
- Very small strings (< 20 characters)
- Real-time streaming (compression overhead)

### Memory vs. Speed Trade-off

```python
from lzw import compress, decompress
import time

# Measure compression benefit
text = "Your repeated text " * 100

# Measure compression
start = time.time()
compressed = compress(text)
compress_time = time.time() - start

# Measure decompression
start = time.time()
decompressed = decompress(compressed)
decompress_time = time.time() - start

# Calculate benefit
original_size = len(text)
compressed_size = len(compressed)
memory_saved = original_size - compressed_size

print(f"Memory saved: {memory_saved} characters")
print(f"Compression time: {compress_time*1000:.2f}ms")
print(f"Decompression time: {decompress_time*1000:.2f}ms")

# Decide based on your use case
if memory_saved > 100 and decompress_time < 0.1:
    print("Compression is beneficial!")
```

## Advanced Integration

### Custom Dictionary Initialization

If you know your data patterns, you can modify `lzw.py` to pre-initialize the dictionary:

```python
# In lzw.py, modify the compress function
def compress(data, initial_dict=None):
    if initial_dict:
        dictionary = initial_dict.copy()
        dict_size = max(dictionary.values()) + 1
    else:
        dictionary = {chr(i): i for i in range(256)}
        dict_size = 256
    # ... rest of the function
```

### Batch Processing

For processing multiple files:

```python
from lzw import compress_to_binary, decompress_from_binary
import os

def compress_directory(input_dir, output_dir):
    """Compress all text files in a directory"""
    os.makedirs(output_dir, exist_ok=True)
    
    for filename in os.listdir(input_dir):
        if filename.endswith('.txt'):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename + '.lzw')
            
            with open(input_path, 'r') as f:
                data = f.read()
            
            compressed = compress_to_binary(data)
            
            with open(output_path, 'wb') as f:
                f.write(compressed)
            
            print(f"Compressed {filename}")

# Usage
compress_directory('./data', './data_compressed')
```

## Testing Your Integration

Always test the integration:

```python
import unittest
from lzw import compress, decompress

class TestIntegration(unittest.TestCase):
    def test_your_use_case(self):
        # Test with your actual data patterns
        data = "Your typical data here"
        compressed = compress(data)
        decompressed = decompress(compressed)
        self.assertEqual(data, decompressed)

if __name__ == '__main__':
    unittest.main()
```

## Support

For issues or questions about integration, please open an issue on the GitHub repository.
