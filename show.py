'''
This script should accept as command line arguments a file name and then 
display that file using th egraphics Plus libary
'''

#import in the graphics libary and the libary needed for CLI

import graphicsPlus as gp
import sys
import filter

#get the frame
#import the image
#get the rgb values for each pixel
#adjust the rgb values based off an algorithim
#swap the vales to create a filter

def main(argv):

    #check to make sure you have the correct number of arguments
    #print a usage statement if needed
        
        #picture_file = "maine3.ppm"
        
        if len(argv) < 2:
            print("This program needs at least two arguments to run.")
            print("The first should be the name of the program (show.py).")
            print("The second should be the image you'd like to use.")
            sys.exit()
        

        '''
        create a variable to hold the image load it in with the Image 
        method from the imported lib
        '''
        
        src_image = gp.Image(gp.Point(0,0), sys.argv[1])

        '''
        create variables for width and height load them with the 
        appropriate methods
        '''

        #print(type(image.getHeight()))
        #print(type(image.getWidth()))
        width = src_image.getWidth()
        height = src_image.getHeight()
        #print(width, " ", height)

        '''
        create a variable to hold a window object and create that object
        with GraphWin()
        '''

        window = gp.GraphWin("This is a window", width, height)

        '''
        move the image to the center of the window. The center would be
        1/2 the width and 1/2 the height
        '''
        
        src_image.move(width*0.5,height*0.5)

        '''
        draw the image and then call the getMouse method to pause
        '''

        #filter.swapRedBlue(src_image)
        #filter.greyscale(src_image)
        filter.inverse(src_image)
        src_image.draw(window)
        window.getMouse()
    
#What's this for?
if __name__ == "__main__":
	main(sys.argv)
