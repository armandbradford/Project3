# Project3
Repo for project3
# This was made by Tristan Zoeller and Armand Bradford.

from urllib.request import urlretrieve
import os
import re
import collections 

#This goes and gets the file we need for the assignment.
redirectCounter = 0
errorCounter = 0
URL = 'https://s3.amazonaws.com/tcmg476/http_access_log'
#This is where our file will be saved and what it will be called so we can find it later if needed.
LOCAL_FILE = 'http_access_log'

#These are the months that we will be using to parse the data
months_count ={
  "Jan": 0,
  "Feb": 0,
  "Mar": 0,
  "Apr": 0,
  "May": 0,
  "Jun": 0,
  "Jul": 0,
  "Aug": 0,
  "Sep": 0,
  "Oct": 0,
  "Nov": 0,
  "Dec": 0
}

janlogs=open("january.txt", "a+"); feblogs=open("february.txt", "a+"); marlogs=open("march.txt", "a+"); 
aprlogs=open("april.txt", "a+"); maylogs=open("may.txt", "a+"); junlogs=open("june.txt", "a+");
jullogs=open("july.txt", "a+"); auglogs=open("august.txt", "a+"); seplogs=open("september.txt", "a+")
octlogs=open("octlogs.txt", "a+"); novlogs=open("november.txt", "a+"); declogs=open("december.txt", "a+")   

i=0





