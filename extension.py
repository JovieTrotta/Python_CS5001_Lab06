'''
Jovienne Trotta
CS 5001 | Fall 2022
5001 Lab 6 : Warhol Image Generator

This is my extension for Lab 6.
It includes a larger grid for six images, two extra image filters, and more text methods.
'''

import graphicsPlus as gp
import sys
import filter

def main(argv):
    
   #this is the usage message that will display if the incorrect number of arguments is entered    
   if len(argv) != 2:
      print("This program needs at least two arguments to run.")
      print("The first should be the name of the program (extension.py).")
      print("The second should be the image you'd like to use.")
      sys.exit()
        
   #creates a variable for each image  
   src_image = gp.Image(gp.Point(0,0), sys.argv[1])
   top_right = gp.Image(gp.Point(0,0), sys.argv[1])
   bottom_left = gp.Image(gp.Point(0,0), sys.argv[1])
   bottom_right = gp.Image(gp.Point(0,0), sys.argv[1])
   extension_top = gp.Image(gp.Point(0,0), sys.argv[1])
   extension_bottom = gp.Image(gp.Point(0,0), sys.argv[1])

   #logs width an height of the image  
   width = src_image.getWidth()
   height = src_image.getHeight()

   #uses width and height to make sure the window is large enough to hold the image
   window = gp.GraphWin("This is art!", width*3, height*2)

   #centers the images
   src_image.move(width*0.5,height*0.5)
   top_right.move(width*1.5,height*0.5)
   bottom_left.move(width*0.5,height*1.5)
   bottom_right.move(width*1.5,height*1.5)
   extension_top.move(width*2.5,height*0.5)
   extension_bottom.move(width*2.5,height*1.5)

   #draws the source image without any filters
   src_image.draw(window)
   message_top_left = gp.Text(gp.Point(width*0.5,height*0.5), "This")
   message_top_left.setTextColor("white")
   message_top_left.setSize(36)
   message_top_left.draw(window)

   #draws the source image and then applies a filter
   #this filter will swap the red and blue values
   filter.swapRedBlue(top_right)
   top_right.draw(window)
   message_top_right = gp.Text(gp.Point(width*1.5,height*0.5), "is")
   message_top_right.setTextColor("white")
   message_top_right.setSize(36)
   message_top_right.draw(window)

   #draws the source image and then applies a filter
   #this filter will swap all three r, g, and b values
   filter.three_way_swap(extension_top)
   extension_top.draw(window)
   message_bottom_right = gp.Text(gp.Point(width*2.5,height*0.5), "the")
   message_bottom_right.setTextColor("white")
   message_bottom_right.setSize(36)
   message_bottom_right.draw(window)

   #draws the source image and then applies a filter
   #this filter will add greyscale
   filter.greyscale(bottom_left)
   bottom_left.draw(window)
   message_bottom_left = gp.Text(gp.Point(width*0.5,height*1.5), "extension")
   message_bottom_left.setTextColor("white")
   message_bottom_left.setSize(36)
   message_bottom_left.draw(window)

   #draws the source image and then applies a filter
   #this filter will subtract the r, g, and b values from 255
   filter.inverse(bottom_right)
   bottom_right.draw(window)
   extension_message_1 = gp.Text(gp.Point(width*1.5,height*1.5), "for")
   extension_message_1.setTextColor("white")
   extension_message_1.setSize(36)
   extension_message_1.draw(window)

   #draws the source image and then applies a filter
   #this filter will decrease everything but the red value
   filter.more_red(extension_bottom)
   extension_bottom.draw(window)
   extension_message_2 = gp.Text(gp.Point(width*2.5,height*1.5), "lab06")
   extension_message_2.setTextColor("white")
   extension_message_2.setSize(36)
   extension_message_2.draw(window)

   #this will pause the program so the image can be viewed
   #clicking the window will close the program
   window.getMouse()
    
if __name__ == "__main__":
	main(sys.argv)
