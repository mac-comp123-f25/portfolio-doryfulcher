from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def crop_picture(image, x_coord, y_coord,width, height):
    for target_x in range(width):
        for target_y in range(height):
            source_x = x_coord + target_x
            source_y = y_coord + target_y
            source_pixel = image.getPixel(image, source_x, source_y)
            target_pixel = image.getPixel(image, target_x, target_y)
            image.setColor(target_pixel, image.getColor(source_pixel))

    return image

dam = Picture("../SampleImages/hooverDam.jpg")
dam_crop1 = crop_picture(dam, 260, 90, 240, 210)
dam_crop2 = crop_picture(dam, 100, 150, 100, 150)
dam_crop1.show()
dam_crop2.show()

keep_windows_open()