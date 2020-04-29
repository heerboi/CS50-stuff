#include "helpers.h"
#include <math.h>
#include <string.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            //average the rgb values of pixel and assign them to each of the rgb values
            float avg = (image[i][j].rgbtRed + image[i][j].rgbtBlue + image[i][j].rgbtGreen) / 3.0;
            image[i][j].rgbtRed = image[i][j].rgbtBlue = image[i][j].rgbtGreen = round(avg);
        }
    }
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // plug the formulas for sepia rgb values
            float red = 0.393 * image[i][j].rgbtRed + 0.769 * image[i][j].rgbtGreen + 0.189 * image[i][j].rgbtBlue;
            float green = 0.349 * image[i][j].rgbtRed + 0.686 * image[i][j].rgbtGreen + 0.168 * image[i][j].rgbtBlue;
            float blue = 0.272 * image[i][j].rgbtRed + 0.534 * image[i][j].rgbtGreen + 0.131 * image[i][j].rgbtBlue;
            //cap the rgb values at 255
            if (red > 255)
            {
                red = 255;
            }
            if (green > 255)
            {
                green = 255;
            }
            if (blue > 255)
            {
                blue = 255;
            }
            //round the values and assign them where needed
            image[i][j].rgbtRed = round(red);
            image[i][j].rgbtGreen = round(green);
            image[i][j].rgbtBlue = round(blue);
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++) //iterate through half of width so that swaps dont overlap and redo
        {
            //save the current pixel in a temp. var and swap the original
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - (j + 1)];
            image[i][width - (j + 1)] = temp;
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    //create a temp array to store edited elements as
    //original elements should be preserved
    RGBTRIPLE image1[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            //assign needed variables to zero
            float count = 0, sumr = 0, sumg = 0, sumb = 0;
            //iterate from one column next to current element to
            //column right to the current element
            for (int l = i - 1; l <= i + 1; l++)
            {
                //skip iteration if the current element is out of bounds
                if (l < 0 || l > (height - 1))
                {
                    continue;
                }
                //iterate from one row to the left to
                // one row to the right
                for (int k = j - 1; k <= j + 1; k++)
                {
                    //skip iteration if the current element is out of bounds
                    if (k < 0 || k > (width - 1))
                    {
                        continue;
                    }
                    //add to the individual sums and append count on every pixel in bounds
                    sumr += image[l][k].rgbtRed;
                    sumg += image[l][k].rgbtGreen;
                    sumb += image[l][k].rgbtBlue;
                    count++;
                }
            }
            //initialize the values at particular indexes in the new array after each
            //individual element iteration
            image1[i][j].rgbtRed = fmin(255, round(sumr / count));
            image1[i][j].rgbtGreen = fmin(255, round(sumg / count));
            image1[i][j].rgbtBlue = fmin(255, round(sumb / count));
        }
    }
    //use memcpy to copy the elements of image1 to image, using the size of struct RGBTRIPLE
    //and the number of elements
    memcpy(image, image1, sizeof(RGBTRIPLE) * height * width);
}
