import cv2
import time
from cvzone.HandTrackingModule import HandDetector
import  math
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np



cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()
vol= volume.SetMasterVolumeLevel(0.0, None)
minVol= volRange[0]
maxVol= volRange[1]

while True:
        # Get image frame
        success, img = cap.read()
        # Find the hand and its landmarks
        hands, img = detector.findHands(img)  # with draw
        # hands = detector.findHands(img, draw=False)  # without draw

        if hands:
            # Hand 1
    
            hand1 = hands[0]
            lmList1 = hand1["lmList"]  # List of 21 Landmark points
            bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
            centerPoint1 = hand1['center']  # center of the hand cx,cy
            handType1 = hand1["type"]  # Handtype Left or Right

            fingers1 = detector.fingersUp(hand1)

            if len(hands) == 1:
                # Hand 2
                hand1 = hands[0]
                lmList1 = hand1["lmList"]  # List of 21 Landmark points
                bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
                centerPoint1 = hand1['center']  # center of the hand cx,cy
                handType1 = hand1["type"]  # Hand Type "Left" or "Right"

                fingers1 = detector.fingersUp(hand1)

            # Find Distance between two Landmarks. Could be same hand or different hands
            length, info, img = detector.findDistance(lmList1[4][0:2], lmList1[8][0:2], img)  # with draw
            # length, info = detector.findDistance(lmList1[8], lmList2[8])  # with draw
            # print(length)

            vol = np.interp(length,[50,150],[minVol,maxVol])
            print(vol)
            volume.SetMasterVolumeLevel(vol,None)
                
                    
          
         # if length<50:
               
     # Display
        cv2.imshow("Image", img)
        if cv2.waitKey(5) & 0xFF == 27 :
           break
     #    if close == 0:
     #        break
     #    else:
     #         continue


   






























