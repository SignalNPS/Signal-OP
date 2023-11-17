import cv2
import speech_recognition as sr
import os





listener = sr.Recognizer()
try:
    with sr.Microphone() as source:
        print("Go ahead, I'm listening.")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        if "signal" in command:
            print( "You just said", command)
        else:
            pass




except:
    pass


for i in command:
    path = r'C:\Users\rushi\Downloads\grade10csproject_digitaldreams\images\images'

    if i ==' ':
        rushilchad = os.path.join(path,'space')+'.jpeg'
        img = cv2.imread(rushilchad ,cv2.IMREAD_GRAYSCALE)
        cv2.imshow('space',img)
        cv2.waitKey(1000)
        cv2.destroyWindow('space')
    else:  
        rushilchad = os.path.join(path,i)+'.jpeg'
        img = cv2.imread(rushilchad ,cv2.IMREAD_GRAYSCALE)
        cv2.imshow(i,img)
        cv2.waitKey(1000)
        cv2.destroyWindow(i)
        

        

cv2.destroyAllWindows()






        


        
        
