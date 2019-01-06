import cv2,time
import numpy as np
import face_recognition
import sqlite3

webcam= cv2.VideoCapture(0)

#Now we load all the pictures from the data base

conn= sqlite3.connect("Database/knownUsers.db")

command="SELECT * from Known"
cur= conn.cursor()

cur.execute(command)

imagesInDB= cur.fetchall()

#Now we load the pictures and learn to recognize them

faceEncodes=[]
faceName=[]
for row in imagesInDB:
    imgPath="Photos/"+row[1]+".jpg"
    imageLoad= face_recognition.load_image_file(imgPath)
    faceEncodes.append(face_recognition.face_encodings(imageLoad)[0])
    faceName.append(row[0])
    

#Now we compare with the webcam
checker= True
faceNames=[]
faceLoc=[]
faceEnc=[]

while True:
    ret, frame= webcam.read()
    #This is something i found on Google to help face recoginition to run faster
    sFrame= cv2.resize(frame,(0,0),fx=0.25,fy=0.25)

    #Now we need to convert the image from BGR which cv uses to RGB to face_recoginiton
    rgb_sFrame= sFrame[:,:,::-1]

    if checker:
        faceLoc= face_recognition.face_locations(rgb_sFrame)
        faceEnc= face_recognition.face_encodings(rgb_sFrame,faceLoc)
        
    foundNames=[]
    
    for face in faceEnc:
        #Compare the face encoings in this frame with the known
        matches= face_recognition.compare_faces(faceEncodes,face)
        
        name="Unknown"
        
        #If we found one face encoding to match the frame, we found someone we know
        if True in matches:
            indexOfMatch=matches.index(True)
            name= faceName[indexOfMatch]
            
        #Add to this list of all the names found in the frame    
        foundNames.append(name)
        
    #We do this so we don't process the same frame each time
    checker= not checker

    for(top,right,bottom,left), name in zip(faceLoc,foundNames):
        top *=4
        right *=4
        left *=4
        bottom *=4
        #Draw a box around the frame with, with color red and width 2
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        #Another box for the name
        cv2.rectangle(frame,(left,bottom-35),(right,bottom),(0,0,255),cv2.FILLED)
        #Name font name
        font=cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame,name,(left+6,bottom-6),font,1.0,(255,255,255),1)

    cv2.imshow("Project",frame)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
webcam.release()
cv2.destroyAllWindows()

        
