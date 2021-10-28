import cv2 as cv
import numpy as np
import os as os
from matplotlib import pyplot as plt



def get_requirements():
    print("OpenCV - Computer Vision Library (install this version: opencv-contrib-python")
    print("1. Image Processing and Manipulation. \n")
    print("2. Import necessary libraries.\n")
    print("3. Research how to install any missing packages, if necessary.\n")
    print("4. Create at least three functions that are called by the program:\n")
    print("\ta. main(): calls at least two other functions.\n")
    print("\tb. get_requirements(): displays the program requirements.\n")
    print("\tc. opencv(): displays the following data.\n")
    print("5. Use provided media files. \n")
    print("6. When running program:\n")
    print("\ta. Document any issues.\n")
    print("\tb. Document solutions attempted.\n")
    print("\tc. Note: ***Research how to make it work using Jupyter Notebook!***")

def opencv():
    img_dog = cv.imread('dog.jpg')

    #image dimensions
    dimensions = img_dog.shape

    #image height, width, number of channels
    height = img_dog.shape[0]
    width = img_dog.shape[1]
    channels = img_dog.shape[2]

    print('\nMetadata (Note: Number of Channels (3) represent RGB channels.):')
    print('Dimensions: ', dimensions)
    print('Height: ', height)
    print('Channels: ', channels)

    # imshow() takes 2 args: name of window to display, and matrix of pixels to display
    cv.imshow('Dog1', img_dog)

    #time in milliseconds for any key press
    cv.waitKey(0)

    #next: Read larger image

    img_dog_large = cv.imread('dog_large.jpg')

    cv.imshow('Dog2', img_dog_large)

    #here, resized to 50% of its original size
    resized_dog = rescaleFrame(img_dog_large)
    cv.imshow('Dog Resize', resized_dog)
    cv.waitKey(0)

    #video
    vid_dog = cv.VideoCapture('dog.mp4')

    while True:
        isTrue, frame = vid_dog.read() 

        if type(frame) == type(None):
            break

        frame_resized = rescaleFrame(frame)

        cv.imshow('Dog', frame)
        cv.imshow('Dog Resized', frame_resized)

        if cv.waitKey(20) & 0xFF == ord('q'):
            break 

    vid_dog.release()
    cv.destroyAllWindows()

    #draw shapes and write text on images 

    height = 480 # np rows
    width = 640 # np cols
    num_colors = 3 #np channels

    #np.zeros: returns new array of given shape and type, filled with zeros
    #a. display blank image
    blank_img = np.zeros((height, width, num_colors), dtype="uint8")
    cv.imshow('Blank', blank_img)

    #b. color image (BGR values)
    blank_img[:] = 255, 0, 0
    cv.imshow('Blue', blank_img)

    #c. color only range of pixels (red square in blue image)
    blank_img[100:200, 300:400] = 0, 0, 255
    cv.imshow('Blue w/Red Square', blank_img)

    #d. draw rectangle (img, start_point, end_point, color, thickness)
    cv.rectangle(blank_img, (0, 0), (200, 200), (0, 255, 0), thickness=2)
    cv.imshow('Rectangle', blank_img)

    #e. draw rectangle w/filled color
    cv.rectangle(blank_img, (0, 0), (200, 200),
                (0, 255, 0), thickness=cv.FILLED)
    cv.imshow('Rectangle Filled', blank_img)

    cv.rectangle(blank_img, (0, 0), (blank_img.shape[1] // 4, blank_img.shape[0] // 4),
                (255, 255, 255), thickness=-1)
    cv.imshow('Rectangle Filled Ratio', blank_img)

    #f. draw circle
    cv.circle(blank_img, (blank_img.shape[1] // 2, blank_img.shape[0] // 2), 30,
                (0, 0, 0), thickness=3)
    cv.imshow('Circle', blank_img)

    #g. draw line
    cv.line(blank_img, (blank_img.shape[1], blank_img.shape[0]), (blank_img.shape[1] // 2, blank_img.shape[0] // 2),
            (255, 255, 255), thickness=1)
    cv.imshow('Line', blank_img)

    #h. write text (img, text, origin, fontface, fontscale, color, thickness)
    cv.putText(blank_img, 'Hello World!',
                (blank_img.shape[1] // 2, blank_img.shape[0] // 2), cv.FONT_HERSHEY_SCRIPT_COMPLEX, 1.5, (0, 255, 0), thickness=2)
    cv.imshow('Text', blank_img)
    cv.waitKey(0)

    #resize/rescale images
    #function accepts frame, and scale value

def rescaleFrame(frame, scale=.50):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    #resize frame to specific dimensions
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    #only works for live video
    capture.set(3, width)
    capture.set(4, height)

def notebookImg(resized_dog, img_dog):
    plt.imshow(resized_dog)
    plt.show()
    plt.imshow(img_dog)
    plt.show()

def main():
    get_requirements()
    opencv() 
    notebookImg()

main()


    


        

    


