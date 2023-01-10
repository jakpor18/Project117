#Importing Operating system and Camera Library
import os
import cv2


path = "Images"

images = []

# Gets the files and directories present in a given path
for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
 #The append method takes an object as an argument and adds it to the end of an existing list
        images.append(file_name)
#for printing the length of total number of images in this folder      
print(len(images))
count = len(images)
#loads an image from the specified file
frame=cv2.imread(images[0])
#To display the height and width of the frame shape
height,width, channel=frame.shape
size=(width,height)
# Writes the desired FPS of the output video file. We then have the width and height of output video
out=cv2.VideoWriter("Friendships.mp4",cv2.VideoWriter_fourcc(*"DIVX"),0.8,size)

for i in range(0,count-1):
    frame=cv2.imread(images[i])
    out.write(frame)
#After the Output is finsihed done is printed in the command prompt
out.release()
print("done")