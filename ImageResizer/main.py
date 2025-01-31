import cv2



source = "saif.jpeg"
destination = "resized-50.jpeg"
SCALE_PERCENT = 50


image = cv2.imread(source, cv2.IMREAD_UNCHANGED)
# cv2.imshow("title",image)

width = int(image.shape[1] * SCALE_PERCENT / 100)
height = int(image.shape[0] * SCALE_PERCENT / 100)


size = (width, height)


output = cv2.resize(image, size)

cv2.imwrite(destination, output)
cv2.waitKey(0)

cv2.imshow("title",output)



















cv2.waitKey(0)