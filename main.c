#include <stdio.h>
#include "lzw-compression.h"

int main(void)
{
	array_t dictionary;
	char*  string_to_compress = "ABABABABABAAABABABAAAAABABABABBBB";
	int string_compressed[256] = {0};

	printf("size of char int %zu\n", sizeof(int));
	
	printf("string to compress: %s\n", string_to_compress);

	dictionary = compress(string_compressed, string_to_compress);

	printf("compressed string %s\n", string_compressed);	
	printf("dictionary size: %d\n", dictionary.length);
	return 0;
}
