from VideoDetection import *
import json

def main():
    # Stuff bring returned 

    json_obj = {
    "Driving_time": 20,
    "Distraction_time": 15,
    "Score": 75
   }
    ##To clear the image slate 
    ClearImageFolder()
    
    ##Instantiate the class object
    facedetection = VideoCapture()
    
    main_list = json.dumps(json_obj)

    return main_list

if __name__ == '__main__':
    main()
