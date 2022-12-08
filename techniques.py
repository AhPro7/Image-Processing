# this module for image processing techniques used in the openCV and other needed libraries and packages
# every technique is a function that takes an image as input and returns the processed image as output
# every function has a docstring that describes the technique and the parameters used
# every function name wrote in snake_case
# every function has a test code in the end of the file
# the techniques are:1- gray_scale
#                   2- thresholding
#                   3- canny_edge_detection
#                   4- sobel_edge_detection
#                   5- laplacian_edge_detection
#                   6- gaussian_blur
#                   7- median_blur
#                   8- bilateral_blur
#                   9- erosion
#                   10- dilation
#                   11- contrast_enhancement
#                   12- brightness_enhancement
#                   13- histogram_equalization
#                   14- histogram_matching
#                   15- image_cropping
#                   16- low_light_enhancement
#                   17- image_enhancement
#                   18- rotation
#                   19- translation
#                   20- scaling
#                   21- affine_transformation

# Author: Ahmed Haytham

# import the needed libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import exposure
import os


# gray_scale function
def gray_scale(image):
    """
    this function takes an image as input and returns the gray scale of the image
    :param image: the input image
    :return: the gray scale of the image
    """
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# thresholding function
def thresholding(image, threshold_value):
    """
    this function takes an image and a threshold value as input and returns the thresholded image
    :param image: the input image
    :param threshold_value: the threshold value ex: 127
    :return: the thresholded image
    """
    return cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)[1]

# canny_edge_detection function
def canny_edge_detection(image, threshold1, threshold2):
    """
    this function takes an image and two threshold values as input and returns the canny edge detection of the image
    :param image: the input image
    :param threshold1: the first threshold value ex: 100
    :param threshold2: the second threshold value ex: 200
    :return: the canny edge detection of the image
    """
    return cv2.Canny(image, threshold1, threshold2)

# sobel_edge_detection function
def sobel_edge_detection(image, kernel_size):
    """
    this function takes an image and a kernel size as input and returns the sobel edge detection of the image
    :param image: the input image
    :param kernel_size: the kernel size ex: 3
    :return: the sobel edge detection of the image
    """
    return cv2.Sobel(image, cv2.CV_64F, 1, 1, ksize=kernel_size)

# laplacian_edge_detection function
def laplacian_edge_detection(image, kernel_size):
    """
    this function takes an image and a kernel size as input and returns the laplacian edge detection of the image
    :param image: the input image
    :param kernel_size: the kernel size ex: 3
    :return: the laplacian edge detection of the image
    """
    return cv2.Laplacian(image, cv2.CV_64F, ksize=kernel_size)

# gaussian_blur function
def gaussian_blur(image, kernel_size):
    """
    this function takes an image and a kernel size as input and returns the gaussian blur of the image
    :param image: the input image
    :param kernel_size: the kernel size ex: 3
    :return: the gaussian blur of the image
    """
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

# median_blur function
def median_blur(image, kernel_size):
    """
    this function takes an image and a kernel size as input and returns the median blur of the image
    :param image: the input image
    :param kernel_size: the kernel size ex: 3
    :return: the median blur of the image
    """
    return cv2.medianBlur(image, kernel_size)

# bilateral_blur function
def bilateral_blur(image, kernel_size, sigma_color, sigma_space):
    """
    this function takes an image and three parameters as input and returns the bilateral blur of the image
    :param image: the input image
    :param kernel_size: the kernel size ex: 3
    :param sigma_color: the sigma color ex: 75
    :param sigma_space: the sigma space ex: 75
    :return: the bilateral blur of the image
    """
    return cv2.bilateralFilter(image, kernel_size, sigma_color, sigma_space)

# erosion function
def erosion(image, kernel_size):
    """
    this function takes an image and a kernel size as input and returns the erosion of the image
    :param image: the input image
    :param kernel_size: the kernel size ex: 3
    :return: the erosion of the image
    """
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    return cv2.erode(image, kernel, iterations=1)

# dilation function
def dilation(image, kernel_size):
    """
    this function takes an image and a kernel size as input and returns the dilation of the image
    :param image: the input image
    :param kernel_size: the kernel size ex: 3
    :return: the dilation of the image
    """
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    return cv2.dilate(image, kernel, iterations=1)

# contrast_enhancement function
def contrast_enhancement(image):
    """
    this function takes an image as input and returns the contrast enhanced image
    :param image: the input image
    :return: the contrast enhanced image
    """
    return exposure.equalize_hist(image)

# brightness_enhancement function
def brightness_enhancement(image, gamma):
    """
    this function takes an image and a gamma value as input and returns the brightness enhanced image
    :param image: the input image
    :param gamma: the gamma value ex: 0.5
    :return: the brightness enhanced image
    """
    return exposure.adjust_gamma(image, gamma)

# histogram_equalization function
def histogram_equalization(image):
    """
    this function takes an image as input and returns the histogram equalized image
    :param image: the input image
    :return: the histogram equalized image
    """
    return exposure.equalize_hist(image)

# histogram_matching function
def histogram_matching(image, reference_image):
    """
    this function takes an image and a reference image as input and returns the histogram matched image
    :param image: the input image
    :param reference_image: the reference image ex: the image of the same class
    :return: the histogram matched image
    """
    return exposure.match_histograms(image, reference_image, multichannel=True)

# image_cropping function
def image_cropping(image, x, y, width, height):
    """
    this function takes an image and four parameters as input and returns the cropped image
    :param image: the input image
    :param x: the x value ex: 0
    :param y: the y value ex: 0
    :param width: the width ex
    :param height: the height ex: 100
    :return: the cropped image
    """
    return image[y:y + height, x:x + width]

# image_enhancement function
def image_enhancement(image):
    """
    this function takes an image as input and returns the enhanced image
    :param image: the input image
    :return: the enhanced image
    """
    return cv2.xphoto.createAutoWhiteBalance().balanceWhite(image)

# image_rotation function
def image_rotation(image, angle):
    """
    this function takes an image and an angle as input and returns the rotated image
    :param image: the input image
    :param angle: the angle ex: 90
    :image_center: the center of the image
    :rot_mat: the rotation matrix
    :return: the rotated image
    """
    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
    result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
    return result

# translation function
def translation(image, x, y):
    """
    this function takes an image and two parameters as input and returns the translated image
    :param image: the input image
    :param x: the x value ex: 100
    :param y: the y value ex: 100
    :return: the translated image
    """
    rows, cols = image.shape[:2]
    M = np.float32([[1, 0, x], [0, 1, y]])
    return cv2.warpAffine(image, M, (cols, rows))

# image_scaling function
def image_scaling(image, x, y):
    """
    this function takes an image and two parameters as input and returns the scaled image
    :param image: the input image
    :param x: the x value ex: 0.5
    :param y: the y value ex: 0.5
    :return: the scaled image
    """
    return cv2.resize(image, None, fx=x, fy=y, interpolation=cv2.INTER_CUBIC)

# compare function to see the difference between the original image and the processed image
def compare(original_image, processed_image):
    """
    this function takes two images as input and returns the difference between the two images
    :param original_image: the original image
    :param processed_image: the processed image
    :return: the difference between the two images
    """
    return cv2.subtract(original_image, processed_image)
#_______________________________________________________________________________________________________________________
#def convertToQtFormat(img):
#    height, width, channel = img.shape
#    bytesPerLine = 3 * width
#    convertToQtFormat = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
#    p = convertToQtFormat.scaled(600, 400, Qt.KeepAspectRatio)
#    return QPixmap.fromImage(p)
