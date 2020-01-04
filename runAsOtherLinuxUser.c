#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
int main( int argc, char *argv[] )
{
	setreuid(1000, 1000);
	printf("ID: %d\n", geteuid());
	execve("/bin/sh", NULL, NULL);
}	