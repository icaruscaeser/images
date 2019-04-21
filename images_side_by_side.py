import cv2


img_left = cv2.imread('work/left.jpg',1)
img_right = cv2.imread('work/right.jpg',1)

new_image = cv2.resize(img_left,(1200,900))
img_left = cv2.resize(img_left,(600,900))
img_right = cv2.resize(img_right,(600,900))

for x in range(0,900):
    for y in range(0,600):
        #print(x,y)
        new_image[x,y] = img_left[x,y]

for x in range(0,900):
    for y in range(0,600):
        #print(x,y)
        new_image[x,y+600] = img_right[x,y]


cv2.imwrite('work/new.jpg',new_image)


