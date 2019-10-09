#include <stdlib.h> /* system, NULL, EXIT_FAILURE */
int main ()
{
int i;
i=system ("net user newuser newpass /add");
return 0;
}
