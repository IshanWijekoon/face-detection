import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils #accesses the drawing utilities
mp_face_detect = mp.solutions.face_mesh #accesses the face mesh solution in MediaPipe. Use to initialize the model

d_spec = mp_drawing.DrawingSpec(color = (255, 0, 0), thickness = 1, circle_radius=1)

video = cv2.VideoCapture(0) #creates a video capture object to access the default camera (0 = primary webcam)
#video is the object used to read frames from the webcam

with mp_face_detect.FaceMesh(min_detection_confidence= 0.5, min_tracking_confidence = 0.5) as face_mesh:
    pass
    

    while True:
        ret,image=video.read() #Reads a single frame from the webcam
        #ret is a boolean, True if the frame is read correctly
        #image contains the actual frame (image) captured from the webcam

        image = cv2.flip(image, 1)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # convert frames into rgb
        image.flags.writeable = False # making more accurecy
        output = face_mesh.process(image) # process the image
        # print(output)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) # convert frames into bgr
        if output.multi_face_landmarks:
            for face_landmarks in output.multi_face_landmarks:
                mp_drawing.draw_landmarks(image = image,
                                          landmark_list=face_landmarks,
                                          connections=mp_face_detect.FACEMESH_TESSELATION,
                                          landmark_drawing_spec=d_spec,
                                          connection_drawing_spec=d_spec
                                          )
        cv2.imshow("Face Detection", image) #cv2.imshow() shows the image in a real-time window. Face detection is the title of the window

        k=cv2.waitKey(1)
        if k==ord('n'):
            break
        elif cv2.getWindowProperty("Face Detection", cv2.WND_PROP_VISIBLE) < 1:
            break

    video.release() #Releases the webcam so it's no longer being used by your program
    cv2.destroyAllWindows() #Closes all OpenCV windows created during the program