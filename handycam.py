# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 13:50:47 2019

@authors: Anitha Rathnam KV, Anulekha M, Devesh Gupta, Amulya Kathasagaram
"""

import cv2
import numpy as np
import copy
import math
import time


# Environment:
# OS    : Windows 10
# python: 3.6.8
# opencv: 4.1.2.30

# parameters
cap_region_x_begin=0.5  # start point/total width
cap_region_y_end=0.8  # start point/total width
threshold = 60  #  BINARY threshold
blurValue = 41  # GaussianBlur parameter
bgSubThreshold = 50 # classify pixel values
learningRate = 0 # the rate at which model

# variables
isBgCaptured = 0   # bool, whether the background captured
triggerSwitch = False  # if true, keyborad simulator works

def printThreshold(thr):
    print("! Changed threshold to "+str(thr))

# file management
def openFile(cmmd):
    import os
    os.system(cmmd)
    import sys
    sys.exit()

# remove background from the frame
def removeBG(frame):
    fgmask = bgModel.apply(frame,learningRate=learningRate)
    # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    # res = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

    kernel = np.ones((3, 3), np.uint8)
    fgmask = cv2.erode(fgmask, kernel, iterations=1)
    res = cv2.bitwise_and(frame, frame, mask=fgmask)
    return res

# calculate fingers using defects
def calculateFingers(res,drawing):  # -> finished bool, cnt: finger count
    #  convexity defect
    hull = cv2.convexHull(res, returnPoints=False)
    if len(hull) > 3:
        defects = cv2.convexityDefects(res, hull)
        if type(defects) != type(None):  # avoid crashing.   (BUG not found)

            cnt = 0
            for i in range(defects.shape[0]):  # calculate the angle
                s, e, f, d = defects[i][0]
                start = tuple(res[s][0])
                end = tuple(res[e][0])
                far = tuple(res[f][0])
                a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
                b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
                c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
                angle = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))  # cosine theorem
                if angle <= math.pi / 2:  # angle less than 90 degree, treat as fingers
                    cnt += 1
                    cv2.circle(drawing, far, 8, [211, 84, 0], -1)
            return True, cnt
    return False, 0


# Camera setup
camera = cv2.VideoCapture(0)
camera.set(10,200)
# cv2.namedWindow('trackbar')

cv2.createTrackbar('trh1', 'trackbar', threshold, 100, printThreshold)

tv = 'b'
tv1= 0


while camera.isOpened():
    ret, frame = camera.read()
    #threshold = cv2.getTrackbarPos('trh1', 'trackbar')
    threshold= 60
    frame = cv2.bilateralFilter(frame, 5, 50, 100)  # smoothing filter
    frame = cv2.flip(frame, 1)  # flip the frame horizontally
    cv2.rectangle(frame, (int(cap_region_x_begin * frame.shape[1]), 0),
                 (frame.shape[1], int(cap_region_y_end * frame.shape[0])), (255, 0, 0), 2)
    #cv2.imshow('original', frame)

    #  Main operation
    if isBgCaptured == 1:  # this part wont run until background captured
        img = removeBG(frame)
        img = img[0:int(cap_region_y_end * frame.shape[0]),
                    int(cap_region_x_begin * frame.shape[1]):frame.shape[1]]  # clip the ROI
        #cv2.imshow('mask', img)

        # convert the image into binary image
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (blurValue, blurValue), 0)
        #cv2.imshow('blur', blur)
        ret, thresh = cv2.threshold(blur, threshold, 255, cv2.THRESH_BINARY)
        #cv2.imshow('ori', thresh)


        # get the coutours
        thresh1 = copy.deepcopy(thresh)
        contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        length = len(contours)
        maxArea = -1
        if length > 0:
            for i in range(length):  # find the biggest contour (according to area)
                temp = contours[i]
                area = cv2.contourArea(temp)
                if area > maxArea:
                    maxArea = area
                    ci = i

            res = contours[ci]
            hull = cv2.convexHull(res)
            drawing = np.zeros(img.shape, np.uint8)
            cv2.drawContours(drawing, [res], 0, (0, 255, 0), 2)
            cv2.drawContours(drawing, [hull], 0, (0, 0, 255), 3)

            isFinishCal,cnt = calculateFingers(res,drawing)
            if triggerSwitch is True:
                if isFinishCal is True and cnt <= 2:
                    print (cnt)
                    #app('System Events').keystroke(' ')  # simulate pressing blank space
        tv1 = cnt
        
                    
        #print(cnt)
##        if(cnt==1):
##            tv1='c'
             
        #cv2.imshow('output', drawing)

    # Keyboard Operations
    k = cv2.waitKey(10)
    if k == 27 or tv1=='c':  # press ESC to exit
        camera.release()
        cv2.destroyAllWindows()
        break
    elif tv == 'b' or k == ord('b'):  # press 'b' to capture the background
        time.sleep(2)
        bgModel = cv2.createBackgroundSubtractorMOG2(0, bgSubThreshold)
        isBgCaptured = 1
        tv = 'c'
        print( '!!!Background Captured!!!')
    elif k == ord('r'):  # press 'r' to reset the background
        bgModel = None
        triggerSwitch = False
        isBgCaptured = 0
        print ('!!!Reset BackGround!!!')
    elif k == ord('n'):
        triggerSwitch = True
        print ('!!!Trigger On!!!')

    # execution of action
    if tv1==1:
        fo=open("b1dir.boo","r+")
        lel = fo.read()
        fo.close()
        time.sleep(1)
        openFile(lel)
    if tv1==2:
        fo=open("b2dir.boo","r+")
        lel = fo.read()
        fo.close()
        time.sleep(1)
        openFile(lel)
    if tv1==3:
        fo=open("b3dir.boo","r+")
        lel = fo.read()
        fo.close()
        time.sleep(1)
        openFile(lel)
    if tv1==4:
        fo=open("b4dir.boo","r+")
        lel = fo.read()
        fo.close()
        time.sleep(1)
        openFile(lel)
        

