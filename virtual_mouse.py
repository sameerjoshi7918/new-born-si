import cv2
import mediapipe as mp
import pyautogui as pg
import time
import math

def cc():
    

    cap = cv2.VideoCapture(0)
    hand_detector = mp.solutions.hands.Hands()
    drawing_utils = mp.solutions.drawing_utils
    screen_width, screen_height = pg.size()
    index_y = 0
    while True:
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)
        frame_height, frame_width, _ = frame.shape
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = hand_detector.process(rgb_frame)
        hands = output.multi_hand_landmarks
        if hands:
            for hand in hands:
                drawing_utils.draw_landmarks(frame, hand)
                landmarks = hand.landmark
                for id, landmark in enumerate(landmarks):
                    x = int(landmark.x*frame_width)
                    y = int(landmark.y*frame_height)
                    if id == 8:
                        cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                        index_x = screen_width/frame_width*x
                        index_y = screen_height/frame_height*y

                    if id == 4:
                        cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                        thumb_x = screen_width/frame_width*x
                        thumb_y = screen_height/frame_height*y
                        
                    if id == 12:
                        cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                        middle_x = screen_width/frame_width*x
                        middle_y = screen_height/frame_height*y
                        
                    if id == 16:
                        cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                        ring_x = screen_width/frame_width*x
                        ring_y = screen_height/frame_height*y
                        
                    if id == 20:
                        cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                        pinky_x = screen_width/frame_width*x
                        pinky_y = screen_height/frame_height*y

                        ########  THUMB TO INDEX  ########                             #1
                        x1=thumb_x
                        y1=thumb_y
                        x2=index_x
                        y2=index_y
                        
                        X1=(x2-x1)*(x2-x1)
                        X2=(y2-y1)*(y2-y1)
                        pro=X1+X2
                        dist_of_thumb_to_index=math.sqrt(pro)
                        ##################################

                        ######### THUMB TO MIDDLE #########                            #2
                        x1=thumb_x
                        y1=thumb_y
                        x2=middle_x
                        y2=middle_y
                        
                        X1=(x2-x1)*(x2-x1)
                        X2=(y2-y1)*(y2-y1)
                        pro=X1+X2
                        dist_of_thumb_to_middle=math.sqrt(pro)
                        ###################################

                        ######## THUMB TO RING ############                             #3 
                        x1=thumb_x
                        y1=thumb_y
                        x2=ring_x
                        y2=ring_y
                        
                        X1=(x2-x1)*(x2-x1)
                        X2=(y2-y1)*(y2-y1)
                        pro=X1+X2
                        dist_of_thumb_to_ring=math.sqrt(pro)
                        ###################################

                        ######## THUMB TO RING ############                             #4 
                        x1=thumb_x
                        y1=thumb_y
                        x2=pinky_x
                        y2=pinky_y
                        
                        X1=(x2-x1)*(x2-x1)
                        X2=(y2-y1)*(y2-y1)
                        pro=X1+X2
                        dist_of_thumb_to_pinky=math.sqrt(pro)
                        ###################################
                        
                            
                        if dist_of_thumb_to_index<80 and dist_of_thumb_to_middle>80:
                            pg.hotkey('ctrl','win','right')
                            time.sleep(1)
                        elif dist_of_thumb_to_middle<80 and dist_of_thumb_to_pinky>80:
                            pg.hotkey('ctrl','win','left')
                            time.sleep(1)
                        elif dist_of_thumb_to_ring<80 and dist_of_thumb_to_index>80:
                            pg.hotkey('win','d')
                            time.sleep(1)
                        #elif dist_of_thumb_to_pinky<80:
                        #    pg.moveTo(thumb_x,thumb_y)
                        #    pg.click()
                        #    time.sleep(1)
                        elif dist_of_thumb_to_index<80 and dist_of_thumb_to_middle<80 and dist_of_thumb_to_ring<80 and dist_of_thumb_to_pinky<80:
                            pg.moveTo(thumb_x,thumb_y)
                        







                        
                        #print('outside', abs(index_y - thumb_y))
                        #if abs(index_y - thumb_y) < 20:
                            #pyautogui.click()
                        #    pyautogui.sleep(1)
                        #elif abs(index_y - thumb_y) < 100:
                        #    pyautogui.moveTo(index_x, index_y)
        #cv2.imshow('Virtual Mouse', frame)
        #cv2.waitKey(1)
#cc()
