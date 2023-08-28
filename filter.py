'''
Jovienne Trotta
CS 5001 | Fall 2022
5001 Lab 6 : Warhol Image Generator

This includes the filter functions used in both warhol.py and extension.py.
'''

import graphicsPlus as gp
import sys

def swapRedBlue(src_image):

    '''
    This filter will swap the r and b values. 
    Parameters: an image file
    Returning: a changed image file; a string
    '''

    rows = src_image.getWidth()
    columns = src_image.getHeight()

    for i in range (0,rows):
        for j in range(0,columns):
            pixel_list = src_image.getPixel(i,j)
            src_image.setPixel(i,j,gp.color_rgb((pixel_list[2]),(pixel_list[1]),(pixel_list[0])))

    print("Red and Blue values swapped for image.")

def greyscale(src_image):

    '''
    This filter will average the r, g, b values, creating a greyscale effect. 
    Parameters: an image file
    Returning: a changed image file; a string
    '''

    rows = src_image.getWidth()
    columns = src_image.getHeight()

    for i in range (0,rows):
        for j in range(0,columns):
            pixel_list = src_image.getPixel(i,j)
            r = pixel_list[0]
            g = pixel_list[1]
            b = pixel_list[2]
            r_new = int((r+g+b)/3)
            g_new = int((r+g+b)/3)
            b_new = int((r+g+b)/3)
            src_image.setPixel(i,j,gp.color_rgb(r_new,g_new,b_new))
            
    print("Greyscale added to image.")
   
def inverse(src_image):
    
    '''
    This filter will subtract the r, g, and b values from 255, creating an "inverse" . 
    Parameters: an image file
    Returning: a changed image file; a string
    '''

    rows = src_image.getWidth()
    columns = src_image.getHeight()

    for i in range (0,rows):
        for j in range(0,columns):
            pixel_list = src_image.getPixel(i,j)
            r = pixel_list[0]
            g = pixel_list[1]
            b = pixel_list[2]
            r_new = (abs(255 - r))
            g_new = (abs(255 - g))
            b_new = (abs(255 - b))
            src_image.setPixel(i,j,gp.color_rgb(r_new,g_new,b_new))
            
    print("The image has been flipped to its inverse.")

def more_red(src_image):
    
    '''
    This filter will decrease the b and g values. 
    Parameters: an image file
    Returning: a changed image file; a string
    '''

    rows = src_image.getWidth()
    columns = src_image.getHeight()

    for i in range (0,rows):
        for j in range(0,columns):
            pixel_list = src_image.getPixel(i,j)
            r = pixel_list[0]
            g = pixel_list[1]
            b = pixel_list[2]
            g_new = (abs(g - 50))
            b_new = (abs(g - 50))
            src_image.setPixel(i,j,gp.color_rgb(r,g_new,b_new))
            
    print("All image values except the red value have been decreased.")

def three_way_swap(src_image):
    
    '''
    This filter will swap the r, g, and b values. 
    Parameters: an image file
    Returning: a changed image file; a string
    '''

    rows = src_image.getWidth()
    columns = src_image.getHeight()

    for i in range (0,rows):
        for j in range(0,columns):
            pixel_list = src_image.getPixel(i,j)
            src_image.setPixel(i,j,gp.color_rgb(pixel_list[2],pixel_list[0],pixel_list[1]))
              
    print("All r, g, b values have been swapped.")