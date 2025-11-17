from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def crop_picture(image, x_coord, y_coord,width, height):
    new_pic=Picture(width, height)
    for target_x in range(width):
        for target_y in range(height):
            source_x = x_coord + target_x
            source_y = y_coord + target_y
            color=image.getColor(source_x, source_y)
            new_pic.setColor(target_x, target_y, color)

    return new_pic

dam = Picture("../SampleImages/hooverDam.jpg")
dam_crop1 = crop_picture(dam, 260, 90, 240, 210)
dam_crop2 = crop_picture(dam, 100, 150, 100, 150)
dam.show()
dam_crop1.show()
dam_crop2.show()

keep_windows_open()