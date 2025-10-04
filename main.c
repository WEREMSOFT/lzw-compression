#include <stdio.h>
#include "lzw-compression.h"

int main(void)
{
	int i;
	int *element;
	array_t dictionary;
	array_t compressed_array;
	array_t *dictionary_entry;
	char* string_to_compress = "ABABABABABAAABABABAAAAABABABABBBB";
	char decompressed_string[256] = {0};

	printf("size of char int %zu\n", sizeof(int));
	
	printf("string to compress: %s\n", string_to_compress);

	compressed_array = compress(string_to_compress, &dictionary);

	printf("dictionary size: %d\n", dictionary.length);

	for(i = 0; i < compressed_array.length; i++)
	{
		element = array_get_element_at(compressed_array, i);
		printf("%d-", *element);
	}
/*
printf("\nDictionary\n");
for(i = 256; i < dictionary.length; i++)
{
	dictionary_entry = array_get_element_at(dictionary, i);
	printf("%s\n", dictionary_entry->data);
}
*/

	printf("\nDecompressed string\n");
	for(i = 0; i < compressed_array.length; i++)
	{
		element = array_get_element_at(compressed_array, i);
		dictionary_entry = array_get_element_at(dictionary, *element);
		strcat(decompressed_string, (char *)dictionary_entry->data);
		printf("%s", (char *)dictionary_entry->data);
	}
	printf("\n");

	if(strcmp(string_to_compress, decompressed_string) == 0)
	{
		printf("strings are identical\n");
	} else 
	{
		printf("strings are different\n");
	}
	return 0;
}
