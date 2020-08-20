
#imports 
import cv2
import numpy as np
import argparse
from matplotlib import pyplot as plt

def binarized(image):

	# variable declarations
	window_width = 500
	window_height = 500
	h = 10   # parameter deciding denoising filter strength. 10 is recommended
	templateWindowSize = 7   # size of template for denoising image. Should be odd. (7 is recommended)
	searchWindowSize = 21   # search window size for denoising image. Should be odd. (21 is recommended)
	median_blur_kernel_size = 7   # kernel size for median blur
	dialation_kernel = 13   # size of dialation kernel
	erosion_kernel = 13   # size of dialation kernel

	# Read image matrix
	orig = cv2.imread(image,0)

	# display original image
	cv2.namedWindow('original', cv2.WINDOW_NORMAL)
	cv2.resizeWindow('original', window_width, window_height)
	cv2.imshow('original',orig)

	# Denoising image using Non-local Means Denoising algorithm
	img = cv2.fastNlMeansDenoising(orig, None, h, templateWindowSize, searchWindowSize)

	# Display denoised image
	cv2.namedWindow('denoised', cv2.WINDOW_NORMAL)
	cv2.resizeWindow('denoised', window_width, window_height)
	cv2.imshow('denoised',img)

	# Smoothen the image by median blurring
	img = cv2.medianBlur(img, median_blur_kernel_size)

	# Display smoothed image
	cv2.namedWindow('blurred', cv2.WINDOW_NORMAL)
	cv2.resizeWindow('blurred', window_width, window_height)
	cv2.imshow('blurred',img)
	cv2.waitKey(0)
	#cv2.destroyAllWindows()

	# Applying gaussian blur
	img = cv2.GaussianBlur(img,(7, 7),0)

	# Define Dialation kernel
	kernel_d = np.ones((dialation_kernel, dialation_kernel),np.uint8)

	# Define Erosion kernel
	kernel_e = np.ones((erosion_kernel, erosion_kernel),np.uint8)

	# Binary thresholding the image
	ret,th1 = cv2.threshold(img,101,255,cv2.THRESH_BINARY)

	# Perform dialation to enhance the foreground mask
	th1 = cv2.dilate(th1,kernel_d,iterations = 1)

	# Perform erosion to erode the foreground mask
	th1 = cv2.erode(th1,kernel_e,iterations = 1)

	# show binarized image
	plt.imshow(th1, 'gray')

	# comparing original and binarized image 
	plt.subplot(1,2,1),plt.imshow(orig,'gray')
	plt.title("original Image")

	plt.subplot(1,2,2),plt.imshow(th1,'gray')
	plt.title("Binarized Mask Image")

	plt.show()

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-i', dest='image', action='store', help="pass image to test")
	args = parser.parse_args()
	in_image = args.image
	binarized(in_image)
