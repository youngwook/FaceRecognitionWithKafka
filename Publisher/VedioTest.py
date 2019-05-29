import cv2

cap = cv2.VideoCapture(0)

cap.set(3,640) # set Width
cap.set(4,480) # set Height

while(True):
  
    ret, frame = cap.read()
    
    cv2.imshow('test', frame)

    k = cv2.waitKey(30) & 0xff

    if k == 27: # press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()
