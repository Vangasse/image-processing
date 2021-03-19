# %%
import os
import cv2
import matplotlib.pyplot as plt

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


# %% Load images
I_a = cv2.imread(os.path.join(path,"coins23.png"), cv2.IMREAD_COLOR)
I_b = cv2.imread(os.path.join(path,"coins234.png"), cv2.IMREAD_COLOR)

# %% Image Difference
plt.subplot("131");plt.title("I_a");plt.imshow(I_a)
plt.subplot("132");plt.title("I_b");plt.imshow(I_b)
plt.subplot("133");plt.title("Difference");plt.imshow(img_diff(I_a, I_b))
plt.show()

# %% AND
plt.subplot("131");plt.title("I_a");plt.imshow(I_a)
plt.subplot("132");plt.title("I_b");plt.imshow(I_b)
plt.subplot("133");plt.title("AND");plt.imshow(img_and(I_a, I_b))
plt.show()
# %% OR
plt.subplot("131");plt.title("I_a");plt.imshow(I_a)
plt.subplot("132");plt.title("I_b");plt.imshow(I_b)
plt.subplot("133");plt.title("OR");plt.imshow(img_or(I_a, I_b))
plt.show()
# %% NOT
plt.subplot("121");plt.title("I_a");plt.imshow(I_a)
plt.subplot("122");plt.title("NOT");plt.imshow(img_not(I_a))
plt.show()
# %% XOR
plt.subplot("131");plt.title("I_a");plt.imshow(I_a)
plt.subplot("132");plt.title("I_b");plt.imshow(I_b)
plt.subplot("133");plt.title("XOR");plt.imshow(img_xor(I_a, I_b))
plt.show()

# %% Image Union
plt.subplot("131");plt.title("I_a");plt.imshow(I_a)
plt.subplot("132");plt.title("I_b");plt.imshow(I_b)
plt.subplot("133");plt.title("Union");plt.imshow(img_union_gray(I_a, I_b), 'gray')
plt.show()
# %%
