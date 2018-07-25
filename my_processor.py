# coding=utf-8
import cv2

MAX_DIFFERENCE = 10

class MyImageProcessor:
    """
    class that decodes images and check if one is the crop of another
    """

    def __init__(self, image_path):
        """

        :param image_path:
        """
        self.image = cv2.imread(image_path)

    def __check_data(self, img, cropped,i_s, j_s):
        """

        :param img: original image
        :param cropped: cropped image
        :param i_s: index of i to start looking
        :param j_s: index of j to start looking
        :return:
        """

        for i in range(i_s, i_s + cropped.shape[0]):
            for j in range(j_s, j_s + cropped.shape[1]):
                for k in range(img.shape[2]):
                    if img[i, j, k] - MAX_DIFFERENCE > cropped[i-i_s, j-j_s, k] or\
                            cropped[i-i_s, j-j_s, k] > MAX_DIFFERENCE+img[i, j, k]:
                        return False

        return True

    def check_sub_image(self, image_path):
        """
        :param image_path:
        :return:
        """
        new_image = cv2.imread(image_path)

        if new_image.shape[0] >= self.image.shape[0] and new_image.shape[1] >= self.image.shape[1] and \
            new_image.shape[2] == self.image.shape[2]:
            orig = new_image
            cropped = self.image
            img_no = 2  # the first image is a crop of the second image
        elif new_image.shape[0] <= self.image.shape[0] and new_image.shape[1] <= self.image.shape[1] and \
            new_image.shape[2] == self.image.shape[2]:
            orig = self.image
            cropped = new_image
            img_no = 1  # the second image is a crop of the first image
        else:
            raise Exception("The images are not cropped from one of them. The image sizes show they can't be")

        i_start = 0
        j_start = 0
        found = False
        for i in range(orig.shape[0]-cropped.shape[0]+1):
            for j in range(orig.shape[1]-cropped.shape[1]+1):
                if self.__check_data(orig, cropped, i, j) is True:
                    found = True
                    i_start = i
                    j_start = j
                    break
            if found:
                break
        if found:
            return (i_start, j_start), img_no

        raise Exception("Images are not cropped")


