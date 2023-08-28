'''
height = 300
width = 400

r = 4
g = 5
b = 6

setPixel(x,y,color)

for x in range(width):
    for y in range(height):
        print(x," ", y)

setPixel(x,y,graphics.Color(b,g,r))
'''

'''
for i in range(0,rows):
    for j in range(0,columns):
        pixel = src_image.getPixel(i,j) 
        src_image.setPixel(i,j,gp.color_rgb(r,g,b))
'''

'''
for i in range(0,rows):
    for j in range(0,columns):
        pixel_list = src_image.getPixel(i,j) #[215,34,96] #[r,g,b]
        pixel_list.reverse()
        src_image.setPixel(i,j,graphics.color_rgb(pixel_list[0]),pixel_list[1],pixel_list[2])
'''

'''
pixel = src_image.getPixel(0,0)
    print(pixel)
    r = pixel[0]
    g = pixel[1]
    b = pixel[2]

    print(r)
    print(g)
    print(b)
'''