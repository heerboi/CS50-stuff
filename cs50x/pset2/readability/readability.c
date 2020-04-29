#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

int count_letters(string t);
int count_words(string t);
int count_sen(string t);

int main(void)
{
    string text = get_string("Text: ");

    //stores function obtained values
    int let = count_letters(text);
    int words = count_words(text);
    int sen = count_sen(text);

    // calculates L, S
    float L = (100 * let) / (float)words;
    float S = (100 * sen) / (float)words;
    //calculates index and rounds it
    float index = (0.0588 * L) - (0.296 * S) - 15.8;
    int grade = round(index);
    if (grade >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %d\n", grade);
    }

}

//iterates throught strlen to and adds to
//count if letters
int count_letters(string t)
{
    int count = 0;
    for (int i = 0; i < strlen(t); i++)
    {
        if (isalpha(t[i]))
        {
            count++;
        }
    }
    return count;
}

//iterates through strlen and adds to
//count if spots a whitespace
int count_words(string t)
{
    int count = 1;
    for (int i = 0; i < strlen(t); i++)
    {
        if (i < strlen(t) - 1 && isspace(t[i]))
        {
            count++;
        }
    }
    return count;
}

//iterates through strlen and adds to
//count if spots ., !, ?
int count_sen(string t)
{
    int count = 0;
    for (int i = 0; i < strlen(t); i++)
    {
        if (i > 0 && (t[i] == '.' || t[i] == '!' || t[i] == '?') && isalnum(t[i - 1]))
        {
            count++;
        }
    }
    return count;
}