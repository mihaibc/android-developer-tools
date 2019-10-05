import os, sys
import PIL.Image as Image
from enum import Enum

class Density(Enum):
    __order__ = 'mdpi hdpi xhdpi xxhdpi xxxhdpi'
    mdpi = 1
    hdpi = 1.5
    xhdpi = 2
    xxhdpi = 3
    xxxhdpi = 4

output_folder = ""
input_file = sys.argv[1]
input_file_dimen = sys.argv[2]
if len(sys.argv) == 4:
    output_folder = sys.argv[3]

def create_resized_image(destination_density : Density):
    input_image_name = (os.path.splitext(input_file)[0]).split("\\")[-1]
    output_directory = os.path.join(output_folder,"drawable-" + destination_density._name_) if output_folder != "" else "drawable-" + destination_density._name_
    output_file_path = os.path.join(output_directory, input_image_name + ".png")
    if not os.path.isdir(output_directory):
        os.makedirs(output_directory)
    try:
        im = Image.open(input_file)
        out_width = int(im.size[0] * (destination_density.value / int(input_file_dimen)))
        out_height = int(im.size[1] * (destination_density.value / int(input_file_dimen)))
        output_image = im.resize((out_width,out_height), Image.ANTIALIAS)
        output_image.save(output_file_path, "PNG")
    except IOError as e:
        print (e)


for density in Density:
    if(density.value <= int(input_file_dimen)):
        create_resized_image(density)
