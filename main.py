import cv2
filePath = 'jayvee.jpg'
imgFlag = int(1)
img = cv2.imread(filePath,imgFlag)
cv2.imshow("ako",img)
cv2.waitKey(0)
cv2.destroyAllWindows()