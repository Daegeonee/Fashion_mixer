"""****************************************

Title      : Fashion_Mixer
Date       : 2018.07.14
Author     : Lee Daegeon
Description: this code written to combine dress images into fashion suggestions
             this code has following steps
        1. sort_image module categorizes image files into top, bottom, shoes
        2. image_crop module crops images(solid or transparent background)
        3. scale_image module scales image to fit combination canvas
        4. loop for top, bottom, shoes
        5. image save placed at the end of shoes loop
****************************************"""


# import  Pillow and copy
from PIL import Image
import copy
# module
from sort_image import sort_by_name
from image_crop import crop
from image_scale import scale_image

# image category
category_name = ['t', 'b', 's']
open_path = './images/'
save_path = './combination/'
# categories is a dictionary key = category, value = file names
categories = sort_by_name(open_path, category_name)
# create list to contain image names
t = categories.get('t')
b = categories.get('b')
s = categories.get('s')
# output size
width = 100
length = 300
# image size vars
s_pos_x = b_pos_x = t_pos_x = int(width / 2)
t_l = b_pos_y = int(length * 2 / 6)
s_pos_y = int(length * 5 / 6)

# image new, open, resize, paste, save
for i in range(len(t)):
    im_name_t = t[i]
    combination = Image.new("RGBA", (width, length), (0, 0, 0, 0))
    im1 = Image.open(open_path + im_name_t)
    im1 = crop(im1)
    im1 = scale_image(im1, 0, t_l)
    half_width = im1.size[0]/2
    x1, y1 = int(t_pos_x - half_width), 0
    x2, y2 = int(t_pos_x + half_width), t_l
    combination.paste(im1, (x1, y1, x2, y2))

    for j in range(len(b)):
        im_name_b = b[j]
        im2 = Image.open(open_path + im_name_b)
        im2 = crop(im2)
        im2 = scale_image(im2, width / 2, 0)
        x1, y1 = int(b_pos_x - (im2.size[0]/2)), b_pos_y
        x2, y2 = int(b_pos_x + (im2.size[0]/2)), b_pos_y + im2.size[1]
        combination2 = copy.deepcopy(combination)
        combination2.paste(im2, (x1, y1, x2, y2))

        for k in range(len(s)):
            im_name_s = s[k]
            im3 = Image.open(open_path + im_name_s)
            im3 = crop(im3)
            im3 = scale_image(im3, 0, length - s_pos_y)
            x1, y1 = int(s_pos_x - (im3.size[0]/2)), s_pos_y
            x2, y2 = int(s_pos_x + (im3.size[0]/2)), s_pos_y + im3.size[1]
            combination3 = copy.deepcopy(combination2)
            combination3.paste(im3, (x1, y1, x2, y2))
            combination3.save(save_path + im_name_t[:-4] + im_name_b[:-4] + im_name_s[:-4] + '.png')
