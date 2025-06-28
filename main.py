import cv2

video = cv2.VideoCapture(0) #creates a video capture object to access the default camera (0 = primary webcam)
#video is the object used to read frames from the webcam

while True:
    ret,image=video.read() #Reads a single frame from the webcam
    #ret is a boolean, True if the frame is read correctly
    #image contains the actual frame (image) captured from the webcam

    image = cv2.flip(image, 1)
    cv2.imshow("Face Detection", image) #cv2.imshow() shows the image in a real-time window. Face detection is the title of the window

    k=cv2.waitKey(1)
    if k==ord('n'):
        break
    elif cv2.getWindowProperty("Face Detection", cv2.WND_PROP_VISIBLE) < 1:
        break

video.release() #Releases the webcam so it's no longer being used by your program
cv2.destroyAllWindows() #Closes all OpenCV windows created during the program