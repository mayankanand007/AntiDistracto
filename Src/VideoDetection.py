import cv2, numpy,os,argparse
import numpy as np
import cv2
import base64


def VideoCapture():

    cap = cv2.VideoCapture(0)

    # Capture frame-by-frame
    ret, frame = cap.read()

    decoded_data = base64.b64decode(frame)

    np_data = np.fromstring(decoded_data,np.uint8)

    img = cv2.imdecode(np_data,cv2.IMREAD_UNCHANGED)

    cv2.imshow("frame", frame)

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    return img
# def live_video(camera_port=0):
#         """
#         Opens a window with live video.
#         :param camera:
#         :return:
#         """

#         video_capture = cv2.VideoCapture(camera_port)

#         while True:
#             # Capture frame-by-frame
#             ret, frame = video_capture.read()

#             # Display the resulting frame
#             cv2.imshow('Video', frame)

#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break

#         # When everything is done, release the capture
#         video_capture.release()
#         cv2.destroyAllWindows() 

# class VideoCapture:
    
#     def __init__(self):
#         self.count = 0
#         #self.argsObj = Parse()
#         #self.faceCascade = cv2.CascadeClassifier(self.argsObj.input_path)
#         self.videoSource = cv2.VideoCapture(0)
        
#     def CaptureFrames(self) -> str:
#         #Our main search query
#         search_key = ' step by step recipes using '

#         # while True:
            
#         ##Create a unique number for each frame
#         frameNumber = '%08d' % (self.count) 
        
#         ##Capturing Frame by Frame
#         ret, frame = self.videoSource.read()
        
#         ##Setting the screen color to grey, so that the haar cascade can easily detect the edges and the faces
#         screenColor = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

#         ##Customize how the cascade detects the watch
#         watches = watch_cascade.detectMultiScale(
#             screenColor,
#             scaleFactor = 1.05,
#             minNeighbors = 5,
#             minSize = (20,20),
#             flags = 0)
        
#         ##Displaying the resulting frame
#         cv2.imshow('Detecting Ingredients!!' , screenColor)
        
        
#         print ('Umang\'s app is detecting ingredients')
                
#         ##Graphing the watch and drawing the rectangle around it:
#         for (x,y,w,h) in watches:
#             roi_color = frame[y:y+h, x:x+w]
#             font = cv2.FONT_HERSHEY_SIMPLEX
#             #Watch detected
#             cv2.putText(frame, 'Watch',(x,y) , font,0.5,(0,255,0),2,cv2.LINE_AA)
#             cv2.imwrite(DEFAULT_OUTPUT_PATH + frameNumber + '.png',frame)
#             watch = True
            
        
#             ##Incremeting count for each of the frames
#             self.count += 1
            
#             ##In every 1 millisecond, new frame is captured. As soon as the escape key is pressed,
#             ##we exit out of the loop and no more frames are captured and the while loop ends
#             # if cv2.waitKey(1) == 27:
#             #     break
        
#         ##When the recording is done, close the webcam connection and close all the windows.  
#         self.videoSource.release() ##close the webcam
#         cv2.waitKey(500)
#         cv2.destroyAllWindows()
#         cv2.waitKey(500)
       
#         #Building the search query
#         if watch == True:
#           search_key += "Tomatoes "

#         return search_key      

# def Parse():
#     parser =  argparse.ArgumentParser(description='Cascade path for Face Detection')
#     parser.add_argument('-i','--input_path', type = str , default = DEFAULT_CASCADE_INPUT_PATH,help = 'CASCADE input Path',required =True)
#     parser.add_argument('-o','--output_path',type = str, default = DEFAULT_OUTPUT_PATH, help = 'Output path for pics taken',required=True)
#     args = parser.parse_args()
#     return args     

# def ClearImageFolder():
#     if not (os.path.exists(DEFAULT_OUTPUT_PATH)):
#         os.makedirs(DEFAULT_OUTPUT_PATH)
        
#     else:
#         for files in os.listdir(DEFAULT_OUTPUT_PATH):
#             filePath = os.path.join(DEFAULT_OUTPUT_PATH, files)
#             if os.path.isfile(filePath):
#                 os.unlink(filePath)
#             else:
#                 continue