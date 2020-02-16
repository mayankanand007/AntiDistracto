import cv2, numpy,os,argparse

DEFAULT_OUTPUT_PATH = 'OpenCV Results/'
DEFAULT_CASCADE_INPUT_PATH = 'watch_cascade.xml'
watch_cascade = cv2.CascadeClassifier('/Users/umanggupta/Desktop/RecipePy_working_tensorflow_2/Src/watch_cascade.xml')
watch = False


class VideoCapture:
    
    def __init__(self):
        self.count = 0
        #self.argsObj = Parse()
        #self.faceCascade = cv2.CascadeClassifier(self.argsObj.input_path)
        self.videoSource = cv2.VideoCapture(0)
        
    def CaptureFrames(self) -> str:
        #Our main search query
        search_key = ' step by step recipes using '

        while True:
            
            ##Create a unique number for each frame
            frameNumber = '%08d' % (self.count) 
            
            ##Capturing Frame by Frame
            ret, frame = self.videoSource.read()
            
            ##Setting the screen color to grey, so that the haar cascade can easily detect the edges and the faces
            screenColor = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

            ##Customize how the cascade detects the watch
            watches = watch_cascade.detectMultiScale(
               screenColor,
               scaleFactor = 1.05,
               minNeighbors = 5,
               minSize = (20,20),
               flags = 0)
            
            ##Displaying the resulting frame
            cv2.imshow('Detecting Ingredients!!' , screenColor)
            
           
            print ('Umang\'s app is detecting ingredients')
                   
            ##Graphing the watch and drawing the rectangle around it:
            for (x,y,w,h) in watches:
                roi_color = frame[y:y+h, x:x+w]
                font = cv2.FONT_HERSHEY_SIMPLEX
                #Watch detected
                cv2.putText(frame, 'Watch',(x,y) , font,0.5,(0,255,0),2,cv2.LINE_AA)
                cv2.imwrite(DEFAULT_OUTPUT_PATH + frameNumber + '.png',frame)
                watch = True
                
            
            ##Incremeting count for each of the frames
            self.count += 1
            
            ##In every 1 millisecond, new frame is captured. As soon as the escape key is pressed,
            ##we exit out of the loop and no more frames are captured and the while loop ends
            if cv2.waitKey(1) == 27:
                break
        
        ##When the recording is done, close the webcam connection and close all the windows.  
        self.videoSource.release() ##close the webcam
        cv2.waitKey(500)
        cv2.destroyAllWindows()
        cv2.waitKey(500)
       
        #Building the search query
        if watch == True:
          search_key += "Tomatoes "

        return search_key      

def Parse():
    parser =  argparse.ArgumentParser(description='Cascade path for Face Detection')
    parser.add_argument('-i','--input_path', type = str , default = DEFAULT_CASCADE_INPUT_PATH,help = 'CASCADE input Path',required =True)
    parser.add_argument('-o','--output_path',type = str, default = DEFAULT_OUTPUT_PATH, help = 'Output path for pics taken',required=True)
    args = parser.parse_args()
    return args     

def ClearImageFolder():
    if not (os.path.exists(DEFAULT_OUTPUT_PATH)):
        os.makedirs(DEFAULT_OUTPUT_PATH)
        
    else:
        for files in os.listdir(DEFAULT_OUTPUT_PATH):
            filePath = os.path.join(DEFAULT_OUTPUT_PATH, files)
            if os.path.isfile(filePath):
                os.unlink(filePath)
            else:
                continue