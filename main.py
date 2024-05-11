from ultralytics import YOLO
import cv2 as cv
from util import get_car,read_license_plate,write_csv

results = {}

#load models

vehcile_detector_model = YOLO('./Models/yolov9e.pt')
license_plate_model = YOLO('./Models/license_plate_detector.pt')

#load video
Video_capture = cv.VideoCapture('./sample.mp4')

rec = True

vechile = [2,3,5,7]

frame_no = -1

while rec :
    frame_no +=1
    rec,frame = Video_capture.read()
    
    if rec : 
        results[frame_no] = {}
        
        #detect and track vehcile
        detections = vehcile_detector_model.track(frame,persist=True,tracker='bytetrack.yaml')
        detection_boxes = []
        for detection in detections[0].boxes.data.tolist() :
            x1,y1,x2,y2,vechile_id,conf,class_id = detection
            if int(class_id) in vechile :
                detection_boxes.append([x1,y1,x2,y2,vechile_id])       
                        
        
         #detect license Plate  
        license_plates =  license_plate_model(frame)[0]  
        for license_plate in license_plates.boxes.data.tolist() :
            x1,y1,x2,y2,conf,class_id = license_plate
            
            #asign license plate to car
            xcar1,ycar1,xcar2,ycar2,car_id = get_car(license_plate,detection_boxes)
            
            #crop license plate
            if car_id != -1:

                # crop license plate
                license_plate_crop = frame[int(y1):int(y2), int(x1): int(x2), :]

                # process license plate
                license_plate_crop_gray = cv.cvtColor(license_plate_crop, cv.COLOR_BGR2GRAY)
                _, license_plate_crop_thresh = cv.threshold(license_plate_crop_gray, 64, 255, cv.THRESH_BINARY_INV)

                # read license plate number
                license_plate_text, license_plate_text_score = read_license_plate(license_plate_crop_thresh)

                if license_plate_text is not None:
                    results[frame_no][car_id] = {'car': {'bbox': [xcar1, ycar1, xcar2, ycar2]},
                                                  'license_plate': {'bbox': [x1, y1, x2, y2],
                                                                    'text': license_plate_text,
                                                                    'bbox_score': conf,
                                                                    'text_score': license_plate_text_score}}

# write results
write_csv(results, './test.csv')
            
            
            
            
                  



