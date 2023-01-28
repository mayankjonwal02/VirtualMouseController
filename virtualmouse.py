import cv2
import mediapipe as mp
import pyautogui
hand_detector=mp.solutions.hands.Hands()
drawing_utils=mp.solutions.drawing_utils
screenwidth,screenheight=pyautogui.size()

cap = cv2.VideoCapture(0)                      
while True:
    _,frame=cap.read()
    frame=cv2.flip(frame,1)
    
    rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output=hand_detector.process(rgb_frame)
    hands=output.multi_hand_landmarks
    fheight,fwidth,_=frame.shape
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame,hand)
            landmarks=hand.landmark
            for id,landmark in enumerate(landmarks):
                x=int(landmark.x*fwidth)
                y=int(landmark.y*fheight)

                #print(x,y)
                if id==8:
                    cv2.circle(img=frame,center=(x,y),radius=20,color=(0,0,255))
                    indexx=screenwidth/(fwidth-60)*x
                    indexy=screenheight/(fheight-60)*y
                    try:
                        pyautogui.moveTo(indexx,indexy)
                    except:
                        pass
                if id==4:
                    cv2.circle(img=frame,center=(x,y),radius=20,color=(0,0,255))
                    thumbx=screenwidth/fwidth*x
                    thumby=screenheight/fheight*y
                if id==12:
                    cv2.circle(img=frame,center=(x,y),radius=20,color=(0,0,255))
                    middlex=screenwidth/fwidth*x
                    middley=screenheight/fheight*y
                    print('outside',abs(thumby-middley))
                    if abs(thumby-middley)<40:
                        print('clicked')
                        try:
                            pyautogui.doubleClick()
                        except:
                            pass
                        pyautogui.sleep(1)
                        
                if id==16:
                    cv2.circle(img=frame,center=(x,y),radius=20,color=(0,0,255))
                    ringx=screenwidth/fwidth*x
                    ringy=screenheight/fheight*y 
                    if abs(thumby-ringy)<40:
                        print('clicked')
                        try:
                            pyautogui.middleClick()
                        except:
                            pass
                        
                if id==20:
                    cv2.circle(img=frame,center=(x,y),radius=20,color=(0,0,255))
                    littlex=screenwidth/fwidth*x
                    littley=screenheight/fheight*y 
                    if abs(thumby-littley)<40:
                        print('clicked')
                        try:
                            
                            print('a task is done')
                        except:
                            pass
                               
    cv2.imshow('virtual mouse',frame)
    cv2.waitKey(1)

