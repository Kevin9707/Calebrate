import cv2

cap = cv2.VideoCapture(2)

num = 0

while cap.isOpened():

    succes, img = cap.read()

    k = cv2.waitKey(5)

    if k == 27:
        break
    elif k == ord('s'):
        cv2.imwrite('/Users/kamoliddinollabergonov/Desktop/opencv/k/image.jpg' + str(num) + '.png', img)
        print("image saved!")
        num += 1

    cv2.imshow('/Users/kamoliddinollabergonov/Desktop/opencv/k/image.jpg',img)

cap.release()

cv2.destroyAllWindows()