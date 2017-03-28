#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char *magic(char *key, char *string, int n)
{
    int i = 0;
    int keyLength = strlen(key);
    char* newstring = malloc(strlen(string) + 1);
    for( i = 0 ; i < n ; i++ )
    {
        newstring[i]=string[i]^key[i%keyLength];
    }
    return newstring;
}
int main(int argc, char *argv[]) {
  if ( argc != 2 ){
    printf("Please enter a password\n");
  }
  else{
      char cipher[]="\x06\x2e\x24\x0f\x03\x14\x2a\x20\x22\x0f\x0f\x21\x2c\x24\x1e\x0c\x03";
      char key[] = "CVGcvg";
      size_t input_len = strlen(argv[1]) + 1;
      int n = strlen(cipher);
      char* input = malloc(input_len);
      strncpy(input, argv[1], input_len);
      char* magicstr = magic(key, input, n);

      if(strncmp(magicstr, cipher, 35) == 0 && strlen(cipher) == strlen(input)){
          printf("Congrats! Your flag is flag{%s}\n", argv[1]);
      }
      else{
          printf("Try again\n");
      }
      free(input);
      free(magicstr);
  }
}
