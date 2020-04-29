// Implements a dictionary's functionality
#include <stdio.h>
#include <stdbool.h>
#include <ctype.h>
#include <stdlib.h>
#include <strings.h>
#include <string.h>
#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
const unsigned int N = 65536;
// Total size
int totalwords = 0;
// Hash table
node *table[N];
//if hash table is loaded
int loaded = false;
// Returns true if word is in dictionary else false
bool check(const char *word)
{
    // Obtain the index
    unsigned long int h = hash(word);
    node *tmp = table[h];
    // Iterate through the linked list till last element
    while (tmp != NULL)
    {
        if (strcasecmp(word, tmp->word) == 0)
        {
            return true;
        }
        tmp = tmp->next;
    }
    return false;
}

// Hashes word to a number
// hash obtained from https://stackoverflow.com/a/45641002
unsigned int hash(const char *word)
{
    // Hash
    int a;
    // Iterate through the string until null character
    for (a = 0; *word != '\0'; word++)
    {
        //append on each iteration
        a = tolower(*word) + 31 * a;
    }
    //return hash mod total buckets so it doesnt go out of range
    return a % N;
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    //open dict
    FILE *file = fopen(dictionary, "r");
    //if failed
    if (file == NULL)
    {
        unload();
        return false;
    }
    //assign a char array to store the scanned words
    char word1[LENGTH + 1];
    //while fscanf doesnt result in EOF
    while (fscanf(file, "%s", word1) != EOF)
    {
        //assign memory for the new node
        node *n = malloc(sizeof(node));
        //if failed
        if (n == NULL)
        {
            return false;
        }
        //copy the scanned word to the new node
        strcpy(n->word, word1);
        //obtain the hash for the word
        unsigned int index = hash(word1);
        //set the new node pointer to whatever the linked list is pointing at
        n->next = table[index];
        //set the new node as the first node
        table[index] = n;
        //append to the total words
        totalwords++;
        /*node *tmp1 = malloc(sizeof(node));
        tmp1->next =  NULL;
        for (node *tmp = table[index]; tmp->next != NULL; tmp = tmp->next)
        {
            tmp1->next = tmp->next;
        }
        tmp1 = n;*/
    }
    //close the dict
    fclose(file);
    loaded = true;
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    if (loaded)
    {
        return totalwords;
    }
    else
    {
        return 0;
    }
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    //iterate through the array
    for (int i = 0; i < N; i++)
    {
        //if the linked list is empty, continue
        if (table[i] == NULL)
        {
            continue;
        }
        //set a temp node pointing to whatever the linked list is pointing at
        node *cursor = table[i];
        //while the next element is not null
        while (cursor != NULL)
        {
            //set a temp node point at the whatever cursor points at
            //so we dont lose the other elements
            node *temp = cursor;
            //shift the cursor to the next element
            cursor = cursor->next;
            //erase the element pointed to by temp
            free(temp);
        }
        //free the cursor
        free(cursor);
    }
    return true;
}
