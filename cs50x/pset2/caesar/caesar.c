#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int main(int argc, string argv[])
{
    //checks if there are 2 args
    if (argc == 2)
    {
        int brk = 1;
        for (int i = 0, t = strlen(argv[1]); i < t; i++)
        {
            //returns 1 if the arg is not an int
            if (!isdigit(argv[1][i]))
            {
                brk = 0;
                printf("Usage: ./ceasar key\n");
                return 1;
            }
        }
        int key = atoi(argv[1]);
        string plaintext = get_string("plaintext: ");
        printf("ciphertext: ");
        //iterates through len of input and prints cipher
        for (int i = 0, l = strlen(plaintext); i < l; i++)
        {
            //checks if char is upper
            if (isupper(plaintext[i]))
            {
                //if ascii exceeds the range,
                //key is / by 26 and subtracted 26 to keep it in range
                if (plaintext[i] + (key % 26) > 90)
                {
                    printf("%c", plaintext[i] + (key % 26) - 26);
                }
                //else the key is just / by 26 and added
                else
                {
                    printf("%c", plaintext[i] + (key % 26));
                }
            }
            else if (islower(plaintext[i]))
            {
                if (plaintext[i] + (key % 26) > 122)
                {
                    printf("%c", plaintext[i] + (key % 26) - 26);
                }
                else
                {
                    printf("%c", plaintext[i] + (key % 26));
                }
            }
            else
            {
                printf("%c", plaintext[i]);
            }
        }
        printf("\n");
    }
    else
    {
        printf("Usage: ./ceasar key\n");
        return 1;
    }
}