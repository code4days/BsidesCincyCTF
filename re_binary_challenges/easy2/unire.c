#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <wchar.h>

void auth(char userpass[])
{
	int flag[] = L"bsides{ILearnedThisTrickAtUni}\0";

	int pass[] = L"bsidesisfun";
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
