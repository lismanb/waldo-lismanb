# coding=utf-8
import os
import sys
from my_processor import MyImageProcessor
import logging


logger = logging.getLogger(__name__)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: subimage <path_to_image1> <path_to_image_2>")
        exit(-1)

    if os.path.exists(sys.argv[1]) is False:
        print ("Image %s doesn't exist" % sys.argv[1])
        exit(-2)

    if os.path.exists(sys.argv[2]) is False:
        print ("Image %s doesn't exist" % sys.argv[2])
        exit(-2)

    try:
        obj = MyImageProcessor(sys.argv[1])
        top_left, image_number = obj.check_sub_image(sys.argv[2])

        if image_number == 1:
            print ("The image %s is a crop of image %s starting at position %d,%d" % (sys.argv[2],
                                                                                 sys.argv[1],
                                                                                 top_left[0],
                                                                                 top_left[1]))
        else:
            print("The image %s is a crop of image %s starting at position %d,%d" % (sys.argv[1],
                                                                                sys.argv[2],
                                                                                top_left[0],
                                                                                top_left[1]))
    except Exception as e:
        logger.error(e)
        exit(-3)
