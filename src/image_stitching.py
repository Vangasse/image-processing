
# %%
import os
import cv2
import matplotlib.pyplot as plt
from imutils import paths
import numpy as np
import argparse
import imutils

path = "../img/"

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
images = []
images.append(cv2.imread(os.path.join(path,"ic1.jpg"), cv2.IMREAD_COLOR))
images.append(cv2.imread(os.path.join(path,"ic2.jpg"), cv2.IMREAD_COLOR))
images.append(cv2.imread(os.path.join(path,"ic3.jpg"), cv2.IMREAD_COLOR))
images.append(cv2.imread(os.path.join(path,"ic4.jpg"), cv2.IMREAD_COLOR))

img_stitching(images)
# %%
