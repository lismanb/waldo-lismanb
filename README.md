# waldo-lismanb

python3.6 -m pip install opencv-python

python subimage.py ./images/img.jpg ./images/cropped.jpg

MAX_DIFFERENCE is used for comparing pixel values. It can be +-MAX_DIFFERENCE between the original and the cropped image.
I had to do this because of the jpeg encoding providing slightly different values.
I've used 10 for this, but it can be increased if the quality of the cropped is lower.