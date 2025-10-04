#include <stdio.h>
#include "lzw-compression.h"

int main(void)
{
	int i;
	int *element;
	int string_to_compress_length;
	array_t dictionary;
	array_t compressed_array;
	array_t *dictionary_entry;
	char* string_to_compress = "Nosotros no somos como los Orozco Yo los conozco, son ocho los monos: Pocho, Toto, Cholo, Tom, Moncho, Rodolfo, Otto, Pololo Yo pongo los votos sólo por Rodolfo Los otros son locos, yo los conozco, no los soporto Stop. Stop.";
	char decompressed_string[2048] = {0};

	string_to_compress_length = strlen(string_to_compress);
	printf("string to compress: %s\n", string_to_compress);
	printf("length of string to compress: %d\n", string_to_compress_length);

	compressed_array = compress(string_to_compress, &dictionary);

	printf("dictionary size: %d\n", dictionary.length);
	printf("compressed string size: %d\n", compressed_array.length);
	printf("compression rate: %.2f%%\n", (float)compressed_array.length / (float)string_to_compress_length * 100);

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
