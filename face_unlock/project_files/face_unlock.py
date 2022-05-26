# # !pip install face_recognition matplotlib opencv-python
# import cv2
# import matplotlib.pyplot as plt
# import face_recognition
# cam = VideoCapture(0)

# def face_recog(imgSys, test_image):
#     # copy the images
#     img = imgSys.copy()
#     imgTest = test_image.copy()

#     # encoding the list face encodings
#     encodeImg = face_recognition.face_encodings(img)[0]

#     # getting list of all the faces and encodings
#     encodeTest = face_recognition.face_encodings(imgTest)
    
#     # searching all faces one by one
#     for i in range(len(encodeTest)):
#         #comparing faces
#         result = face_recognition.compare_faces([encodeImg],encodeTest[i])
        
#         if result[0] is True:
#             return True
#     return False 

# imgSys = face_recognition.load_image_file('../input/project-opencv/jeff1.jpeg')
# result, imgCam = cam.read()