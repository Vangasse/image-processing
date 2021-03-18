# %%
import os
import cv2
import matplotlib.pyplot as plt
from imutils import paths
import numpy as np
import argparse
import imutils

path = "../img/"

# %% Image difference
def img_diff(I_a, I_b):
    
    img = cv2.absdiff(I_a, I_b)

    return img
# %% Logical operations
def img_and(I_a, I_b):

    img = I_a & I_b

    return img

def img_or(I_a, I_b):

    img = I_a | I_b

    return img

def img_not(I_a):

    img = ~I_a

    return img

def img_xor(I_a, I_b):

    img = cv2.bitwise_xor(I_a, I_b)

    return img
# %% Union
def img_union_gray(I_a, I_b):
    I_a_g = cv2.cvtColor(I_a, cv2.COLOR_BGR2GRAY)
    I_b_g = cv2.cvtColor(I_b, cv2.COLOR_BGR2GRAY)

    img = cv2.max(I_a_g, I_b_g)

    return img


# %% Stitching
def img_stitching(images):

    print("[INFO] stitching images...")
    stitcher = cv2.createStitcher() if imutils.is_cv3() else cv2.Stitcher_create()
    (status, stitched) = stitcher.stitch(images)

    # if the status is '0', then OpenCV successfully performed image
    # stitching
    if status == 0:
        # write the output stitched image to disk
        cv2.imwrite("../img/stitch.jpg", stitched)
        # display the output stitched image to our screen
        #cv2.imshow("Stitched", stitched)
        #cv2.waitKey(0)
    # otherwise the stitching failed, likely due to not enough keypoints)
    # being detected
    else:
        print("[INFO] image stitching failed ({})".format(status))


# %%
I_a = cv2.imread(os.path.join(path,"coins23.png"), cv2.IMREAD_COLOR)
I_b = cv2.imread(os.path.join(path,"coins234.png"), cv2.IMREAD_COLOR)

# plt.imshow(img_diff(I_a, I_b))
# plt.imshow(img_and(I_a, I_b))
# plt.imshow(img_or(I_a, I_b))
# plt.imshow(img_not(I_a))
# plt.imshow(img_xor(I_a, I_b))
plt.imshow(img_union_gray(I_a, I_b), 'gray')

# %%
images = []
images.append(cv2.imread(os.path.join(path,"ic1.jpg"), cv2.IMREAD_COLOR))
images.append(cv2.imread(os.path.join(path,"ic2.jpg"), cv2.IMREAD_COLOR))
images.append(cv2.imread(os.path.join(path,"ic3.jpg"), cv2.IMREAD_COLOR))
images.append(cv2.imread(os.path.join(path,"ic4.jpg"), cv2.IMREAD_COLOR))

img_stitching(images)
# %%
