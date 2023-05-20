#!/usr/bin/env python

from gimpfu import *

def python_fu_batch(image, drawable):
    # function code goes here...
    
    pdb.gimp_message("Initiating script")  
    
    # Defining paths variables, define your directory where image files exists as well as the txt file
    path_data = 'C:\\data.txt'
    path_image_base = 'C:\\image_base.jpeg'
    path_ouput_directory = 'C:\\'
    name_base_file = 'image_base_modified_'

    # Beginning of iteration, reads file of path_data and runs the code for every line of the file
    with open(path_data) as file:
        for line in file:
            try:
                
                pdb.gimp_message("Creating image for "+line) 

                # Loading base image from which names will be added then saved
                image = pdb.file_jpeg_load(path_image_base, path_image_base)                
                   
                # Set foreground which text layer will take to create the text
                # inputs are RGB values
                gimp.set_foreground(8,8,80)
                
                
                ### Defining variables before creating the text layer
                # x and y offset set to 0 temporarily
                x=0
                y=0                
                # strip() is used to remove line breask, if not added exporting throws error as will try to save a files including a line break
                text=line.strip()
                border=10
                size=180
                fontname="Lucida Sans Italic"
                
                
                # Creating text layer at the first corner of the base image
                pdb.gimp_text_fontname(image, None, x, y, text, border, TRUE, size, PIXELS, fontname)
                
                ### Placing text layer in the middle of our x-axis base image
                # Text layer width will depend of the characters of the name read in path_data file, then it's needed to find width of the text layer that was just created
                
                # Selecting fist layer as we know is the text layer
                text_layer = image.layers[0]
                
                # Get widh of text layer and save in a variable width
                width = text_layer.width
                
                ## Calculating the x offset that will place text layer in the middle
                # Calculation sustracts the width of the base image and the width of text layer
                # The x offset needed will be half of the previous sustract
                offx=(image.width - text_layer.width)/2
                
                # y offset is set fixed as it doest not depend on the number of characters of text layer
                # change it depending of the sizes of your image base
                offy=998
                
                # Setting new x and y offset of text layer
                pdb.gimp_layer_set_offsets(text_layer, offx, offy)
                
                # Merging text layer and base image before exporting image 
                theDrawable = pdb.gimp_image_flatten(image)
                
                # Setting the file name as variable depending on the data that is being read in file
                outputPath=path_ouput_directory+name_base_file+text+'.jpeg'
                
                #Export file as jpeg
                # Defining variables 
                pdb.file_jpeg_save(image, theDrawable, outputPath, outputPath, 1, 1, 0, 0, "Scripting with GIMP", 2, 0, 0, 0)
                
            except Exception as err:
                gimp.message("Unexpected error: " + str(err))
    # End of iteration
    
    pdb.gimp_message("End of script")  
    
register(
    "python_fu_batch",
    "python_fu_batch",
    "python_fu_batch",
    "Jeison Beraun", "Jeison Beraun", "2023",
    "python_fu_batch",
    "", # type of image it works on (*, RGB, RGB*, RGBA, GRAY etc...)
    [
        (PF_IMAGE, "image", "takes current image", None),
        (PF_DRAWABLE, "drawable", "Input layer", None)
    ],
    [],
    python_fu_batch, menu="<Image>/File")  # second item is menu location

main()
