import cv2
from object_detector import *
import numpy as np

Parameters_Creation = cv2.aruco.DetectorParameters_create()
aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_50)
Detector = HomogeneousBgDetector()

Image = cv2.imread('phone_cover.jpg')

Image1 = cv2.resize(Image,(600, 500))

corners, _, _ = cv2.aruco.detectMarkers(Image1, aruco_dict, parameters= Parameters_Creation)
int_corner = np.int0(corners)
cv2.polylines(Image1, int_corner, True, (0, 255, 0),5)
aruco_perimeter = cv2.arcLength(corners[0], True)
print(aruco_perimeter)
pixel_cm_2_ratio = aruco_perimeter / 16
print(pixel_cm_2_ratio)

Contours = Detector.detect_objects(Image1)
for Contour in Contours:

    Rect = cv2.minAreaRect(Contour)
    (x, y), (L, B), Angle = Rect
    Object_Width = B / pixel_cm_2_ratio
    Object_Height = L / pixel_cm_2_ratio

    box = cv2.boxPoints(Rect)
    box = np.int0(box)
    cv2.circle(Image1, (int(x), int(y)), 5, (0, 255, 0), -1)
    cv2.polylines(Image1, [box], True, (255, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(Image1, "Width {} cm".format(round(Object_Width,1)), (int(x - 100), int(y - 20)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.putText(Image1, "Height {} cm".format(round(Object_Height, 1)), (int(x - 100), int(y + 20)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

cv2.imshow('OUTPUT', Image1)
cv2.waitKey(0)

