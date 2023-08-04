import cv2
image = cv2.imread("D:\DSML\openCV\Turtle_Tortoise (1462).jpg", 1)
print(image.shape)
img_resize=cv2.resize(image, (1400,1200),interpolation=cv2.INTER_NEAREST)
cv2.imshow("Resized", img_resize)
#cv2.imwrite('img_resize.jpg',img_resize)
cv2.waitKey(0)
cv2.destroyAllWindows()


