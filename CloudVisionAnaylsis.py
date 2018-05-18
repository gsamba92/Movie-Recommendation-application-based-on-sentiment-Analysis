import cv2
import argparse
import io
import os
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

def getSentiment():
    #Emotions
    emo = ['Angry', 'Surprised','Sad', 'Happy']
    emotion = 'No sentiment'
    ############## Spanish version #################
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="Emotion detection movie recom-485e2d9da22c.json"
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser(description='Process some image to find sentiment in faces (if any)')
    ap.add_argument("-f", "--file_name", required=False, default="imgs\Image.jpeg", help="path to image")
    args = vars(ap.parse_args())

    file_name = args["file_name"]
    #path = 'test.jpg'
    # Instantiates a client
    vision_client = vision.ImageAnnotatorClient()
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
        image = types.Image(content=content)
    #image = vision_client.image(filename=file_name)

    #faces = image.detect_faces(limit=20)
    faces = vision_client.face_detection(image=image).face_annotations
    #print ('Number of faces: ', len(faces))

    img = cv2.imread(file_name)
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                           'LIKELY', 'VERY_LIKELY')
    for face in faces:

        sentiment = [likelihood_name[face.surprise_likelihood],likelihood_name[face.anger_likelihood],likelihood_name[face.sorrow_likelihood],likelihood_name[face.joy_likelihood] ]
        
        for item, item2 in zip(emo, sentiment):
            print(item, ": ", item2)

        if not (all( item == 'VERY_UNLIKELY' for item in sentiment) ):

            if any( item == 'VERY_LIKELY' for item in sentiment):
                state = sentiment.index('VERY_LIKELY')
                # the order of enum type Likelihood is:
                #']\', 'POSSIBLE', 'UNKNOWN', 'UNLIKELY', 'VERY_LIKELY', 'VERY_UNLIKELY'
                # it makes sense to do argmin if VERY_LIKELY is not present, one would espect that VERY_LIKELY
                # would be the first in the order, but that's not the case, so this special case must be added
            elif any( item == 'LIKELY' for item in sentiment):
                state = sentiment.index('LIKELY')
            elif any( item == 'UNLIKELY' for item in sentiment):
                state = sentiment.index('UNLIKELY')
            
            else:
                state = sentiment.index('POSSIBLE')#np.argmin(sentiment)

            emotion = emo[state]
        print(emotion)
        box = [(vertex.x, vertex.y)
                   for vertex in face.bounding_poly.vertices]    
        pts = box + [box[0]]
        print(pts[0],pts[2])
        
        cv2.putText(img,emotion, pts[0], cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)
        cv2.rectangle(img, pts[0], pts[2], (0, 255, 0), 2)
        
    cv2.imshow("Analysis", img)
    cv2.waitKey(0)
    cv2.imwrite('static/output_'+emotion+'.jpeg',img)
    return emotion
