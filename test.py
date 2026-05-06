

# from: https://plantcv.org/tutorials/simple-rgb-workflow


# Input/Output variables
# Import libraries
from plantcv import plantcv as pcv
from plantcv.parallel import WorkflowInputs

# Input/output options
args = WorkflowInputs(
    images=["./test.jpg"],
    names="test1",
    result="test1.json",
    outdir=".",
    writeimg=False,
    debug="plot"
    )

# Edit display settings if necessary
# Set debug to the global parameter 
pcv.params.debug = args.debug
# Change display settings
pcv.params.dpi = 100
# Increase text size and thickness to make labels clearer
# (size may need to be altered based on original image size)
pcv.params.text_size = 10
pcv.params.text_thickness = 20


# Read the input image
img, path, filename = pcv.readimage(filename=args.test1)


# Crop image if necessary.
# Inputs:
#   img - RGB, grayscale, or hyperspectral image data 
#   x - X coordinate of the top left corner of the box to crop to
#   y - Y coordinate of the top left corner of the box to crop to
#   h - Height of the box to crop to
#   w - Width of the box to crop to

crop_img = pcv.crop(img=img, x=0, y=0, h=350, w=600)



# Optional color correction
# Inputs:
#   rgb_img - RGB image
#   channel - colorspace channel selection (l, a, or b in this case)

b_img = pcv.rgb2gray_lab(rgb_img=crop_img, channel='b')


# Convert the RGB image to LAB and select the B channel
#
# Inputs:
#   rgb_img - RGB image
#   channel - colorspace channel selection (l, a, or b in this case)

b_img = pcv.rgb2gray_lab(rgb_img=crop_img, channel='b')


# Histogram (missing Ipython)
# Inputs:
#   img - image data
#   channel - colorspace channel selection (l, a, or b in this case)

# hist_figure1, hist_data1 = pcv.visualize.histogram(img = b_img, hist_data=True)


# Inputs:
#   gray_img - grayscale image data
#   threshold - Threshold value (0-255)
#   object_type - "light" or "dark" (default: "light"). If object is lighter than the background then standard thresholding is done. 
#                 If object is darker than the background then inverse thresholding is done.

thresh_mask = pcv.threshold.binary(gray_img=b_img, threshold=130, object_type='light')


# Cleaning up the mask

# There are several options for cleaning up and adjusting our mask (fill, fill_holes, dilate, erode, etc). Here we will just use fill to fill in small objects.

# Inputs:
#   bin_img - mask, binary image data
#   size - minimum object area size in pixels (integer), smaller objects will be filled


fill_mask = pcv.fill(bin_img=thresh_mask, size=1000)


# Define the region of interest (ROI).
# Inputs: 
#   img - RGB or grayscale image to plot the ROI on 
#   x - The x-coordinate of the upper left corner of the rectangle 
#   y - The y-coordinate of the upper left corner of the rectangle 
#   h - The height of the rectangle 
#   w - The width of the rectangle 

roi = pcv.roi.rectangle(img=fill_mask, x=100, y=0, h=300, w=400)

# Inputs:
#    mask - the clean mask you made above
#    roi - the region of interest you specified above

kept_mask  = pcv.roi.quick_filter(mask=fill_mask, roi=roi)



# Analysis: Analyze shape and color. The data gets stored to an Outputs class automatically.

# Inputs:
#   img - RGB or grayscale image data 
#   labeled_mask - the mask of each individual object, set by the create_labels function. 
#   n_labels - the number of objects, set by the create_labels function. 

analysis_image = pcv.analyze.size(img=crop_img, labeled_mask=kept_mask)

# Histogram
# Inputs:
#   rgb_img - RGB image data
#   mask - Binary mask of selected contours 
#   colorspaces - 'all' (default), 'rgb', 'lab', or 'hsv'
#                 This is the data to be printed to the SVG histogram file  
#   label - Optional label parameter, modifies the variable name of observations recorded. (default `label="default"`)

# color_histogram = pcv.analyze.color(rgb_img=crop_img, labeled_mask=kept_mask, colorspaces='all', label="default")

pcv.print_image(kept_mask, "b_imgTest.png")

#This saves results for one image, and each image is saved individually if you run another image (it will overwrite the last one)
pcv.outputs.save_results(filename= args.result)