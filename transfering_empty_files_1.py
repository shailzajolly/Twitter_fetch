#The script transfers empty files to a folder

import cv2
import glob, os
import sys
import numpy as np

counter = 0
cnt = 0
correct_image_names = []
not_correct_image_names = []
os.mkdir('/home/jolly/task_for_verified_accounts/non_error_images/')
#os.mkdir('/home/jolly/task_for_verified_accounts/error_images/')
os.chdir("/home/jolly/task_for_verified_accounts/images_verified/")

for filename in glob.glob("*.jpg"):
  img = cv2.imread(filename)
  if img is not None:
    print filename
    correct_image_names.append(filename)
    print img.shape
    cnt +=1
    print cnt
    cv2.imwrite(os.path.join('/home/jolly/task_for_verified_accounts/non_error_images',filename), img)

  else:
    counter += 1
    print "Empty Image Number is" + str(counter) + "\n"+ filename
    not_correct_image_names.append(filename)
    f = open("/home/jolly/task_for_verified_accounts/error_images.txt","a+") #opens file with name of "test.txt"
    f.write(filename  +  "\n")
    f.close()
		
