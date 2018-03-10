import PIL
import matplotlib.pyplot as plt
import os.path
import numpy as np    
 

 

# Open the files in the same directory as the Python script
directory = os.path.dirname(os.path.abspath(__file__))  
student_file = os.path.join(directory, 'twilight_zone2.jpg')


# Open and show the face image in a new Figure window
face_img = PIL.Image.open(student_file)
fig, axes = plt.subplots(1, 1)
axes.imshow(face_img, interpolation='none')
fig.show

# Display face in second axes and set window to the right eye
axes[1].imshow(face_img, interpolation='none')
axes[1].set_xticks(range(1050, 1410, 100))
axes[1].set_xlim(1050, 1400) #coordinates measured in plt, and tried in iPython
axes[1].set_ylim(1100, 850)


# Open, resize, and display selfie
earth_file = os.path.join(directory, '81rNaPo93WL._AC_UL320_SR266,320_.jpg')
earth_img = PIL.Image.open(earth_file)
earth_small = earth_img.resize((400, 400)) #frame width and height measured in plt
fig2, axes2 = plt.subplots(1, 2)
axes2[0].imshow(earth_img)
axes2[1].imshow(earth_small)

# Open, resize, and display face
self_file = os.path.join(directory, '20170904_094331.jpg')
self_img = PIL.Image.open(self_file)
self_small = self_img.resize((300, 300)) #frame width and height measured in plt



fig3, axes3 = plt.subplots(1, 1)

face_img.paste(earth_small, (1100,250) ) 
face_img.paste(self_small,(1159,300))




red_img = plt.imread(student_file)

height = len(red_img)
width = len(red_img)
for row in range(411, 670):
                for column in range(1537, 1880):
                    red_img[row][column] = [132, 7, 7] # Red
                    
                    
                    
                    
                    
                    
# Display

axes3.imshow(face_img, interpolation='none')


fig3.show()