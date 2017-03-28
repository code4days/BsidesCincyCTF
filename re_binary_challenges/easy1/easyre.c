#include <stdio.h>
#include <string.h>
#include <ctype.h>

void auth(char userpass[])
{
	char flag[] = "bsides{TheyWontAllBeThisEasy}\0";

	char pass[] = "cincinnati";
	char fail[] = "nope";

	if(strncmp(pass, userpass, 10) == 0){
		puts(flag);
	}
	else{
		puts(fail);
	}
}

int main(){

	char input[100];
	
	printf("Enter the password: ");
	gets(input);
	auth(input);
	return 0;
}
