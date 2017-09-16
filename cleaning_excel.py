#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 10:56:18 2017

@author: shailzajolly
"""
#This script first gets numbers from error file.txt and then use that list of numbers to to extract invalid rows from an existing .excel and store them to a newexcel.

import numpy as np
import os
import re
import csv
numbers_of_error_images = []
rows_of_error_images = []
os.chdir('/home/jolly/task_for_verified_accounts/')

def converting_values_to_list():
   error_images = open("error_images.txt","r")
   for i in error_images:
      number = re.findall('\d+', i)
      numbers_of_error_images.append(number)
   
def removing_listvalues_from_excel():
   out1 = os.chdir('/home/jolly/task_for_verified_accounts/scripts_fr_getting_verified_logos/logos_verified/')  
   with open('out1.csv','r') as csvfile:
      spamreader = csv.reader(csvfile,delimiter = ' ')
      next(spamreader,None) #skip the headers
      for row in spamreader:
            number1=re.findall(r'^\D*(\d+)', row[0][0])
            for y in numbers_of_error_images[:]:
               if number1 == y:
                  with open('error_images.csv','wb') as csvfile:
                     spamwriter1 = csv.writer(csvfile)
                     spamwriter1.writerow(row)
               else:
                   with open('non_error_images.csv','wb') as csvfile:
                      spamwriter1 = csv.writer(csvfile)
                      spamwriter1.writerow(row)

def main():
   print "Hello" + "/n"
   converting_values_to_list()
   print len(numbers_of_error_images)
   removing_listvalues_from_excel()
   print "done"

if __name__ == "__main__": main()
     

