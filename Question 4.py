#First we found the middle point in each red block. Afterwards we got it's corresponding RGB values for that pixel
#Once we got that value we noticed that red was the only value.
#Once we got all the red pixel values for each pixel we examined each value and noticed that it corresponded to ascii values. 
#We then converted each red value to the corresponding ascii letter and it spelt out The Hulk

from PIL import Image      #PIL has a package has useful class called image which gets RGB values for a pixel.

file = input("Insert file path to image: ")

image = Image.open(file)


image_rgb = image.convert("RGB")

#get RGB value for approximate middle pixel in each square respectivly
rgb_pixel_value = image_rgb.getpixel((102,47))
rgb_pixel_value2 = image_rgb.getpixel((132,47))
rgb_pixel_value3 = image_rgb.getpixel((162,47))
rgb_pixel_value4 = image_rgb.getpixel((192,47))
rgb_pixel_value5 = image_rgb.getpixel((222,47))
rgb_pixel_value6 = image_rgb.getpixel((252,47))
rgb_pixel_value7 = image_rgb.getpixel((282,47))
rgb_pixel_value8 = image_rgb.getpixel((312,47))

print(chr(rgb_pixel_value[0])+chr(rgb_pixel_value2[0])+chr(rgb_pixel_value3[0])+chr(rgb_pixel_value4[0])+chr(rgb_pixel_value5[0])+chr(rgb_pixel_value6[0])+chr(rgb_pixel_value7[0])+chr(rgb_pixel_value8[0]))

