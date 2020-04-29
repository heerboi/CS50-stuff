#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover image\n");
        return 1;
    }
    FILE *file = fopen(argv[1], "r");
    if (!file)
    {
        printf("Cannot open the forensic image.\n");
        return 1;
    }
    //set image var
    int i = 0;
    //allocate 8 bytes for filename
    char *filename = malloc(8);
    //null file pointer
    FILE *file1;
    //array to store 1 block of 512 bytes
    BYTE bytes[512] = {};
    //while eof has not occured
    while (!feof(file))
    {
        //read 1 block of 512 bytes to bytes and store the return value in files
        int files = fread(bytes, 1, 512, file);
        //if the start of jpg is found
        if (bytes[0] == 0xff && bytes[1] == 0xd8 && bytes[2] == 0xff && (bytes[3] & 0xf0) == 0xe0)
        {
            //check if this is first image
            if (i == 0)
            {
                //set the filename to 03d.jpg, 000.jpg in this case
                sprintf(filename, "%03d.jpg", 0);
                //fopen a file with the filename and write to it
                file1 = fopen(filename, "w");
                //write the block of 512 bytes stored in bytes array to file1
                fwrite(bytes, 1, 512, file1);
                //append to the number of images
                i++;
            }
            //if this is not first image
            else
            {
                //close the past file
                fclose(file1);
                //change the filename according to the image var
                sprintf(filename, "%03d.jpg", i);
                //open the file
                file1 = fopen(filename, "w");
                //write another 512 bytes from the array
                fwrite(bytes, 1, 512, file1);
                //append the number of img
                i++;
            }
        }
        //if this is not the start of an image
        else
        {
            //if a file is already open and fread does not return 0,
            //meaning fread has not reached the end as the .raw file has
            //complete 512 byte blocks
            if (i > 0 && files != 0)
            {
                fwrite(bytes, 1, 512, file1);
            }
        }
    }
    //free the memory assigned to filename
    free(filename);
    //close the file1 and file
    fclose(file1);
    fclose(file);
}
