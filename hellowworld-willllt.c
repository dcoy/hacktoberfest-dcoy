#include <stdio.h>

void main() {
	char* hello = "Hello world!";
	while(*hello) {
		printf("%c\n", *hello++);
	}
}
