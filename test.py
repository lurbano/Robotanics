

# from: https://plantcv.org/tutorials/simple-rgb-workflow

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

# Set debug to the global parameter 
pcv.params.debug = args.debug
# Change display settings
pcv.params.dpi = 100
# Increase text size and thickness to make labels clearer
# (size may need to be altered based on original image size)
pcv.params.text_size = 10
pcv.params.text_thickness = 20

img, path, filename = pcv.readimage(filename=args.test1)

# Inputs:
#   rgb_img - RGB image
#   channel - colorspace channel selection (l, a, or b in this case)

b_img = pcv.rgb2gray_lab(rgb_img=crop_img, channel='b')
