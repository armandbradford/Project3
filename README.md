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
LOCAL_FILE = 'local_copy.log'

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


def fileCount():
	filelog = []
	leastcommon = []
	with open(LOCAL_FILE) as logs:
		for line in logs:
			try:
				filelog.append(line[line.index("GET")+4:line.index("HTTP")])	
			except:
				pass
	counter = collections.Counter(filelog)
	for count in counter.most_common(1):														
		print("The most requested file was: {} with {} requests.".format(str(count[0]), str(count[1])))
	for count in counter.most_common():					#Files w/ only one request
		if str(count[1]) == '1':
			leastcommon.append(count[0]), 
	if leastcommon:
    print(file)
  
  #Multiple files with only one request so we need to list them all
		#response = input(" There were {} file(s) that were requested only once, show all? 
		#(y/n)".format(len(leastcommon)))
		#if response == 'y' or response == 'Y':
			#for file in leastcommon:
				#print(file)
# If the file isn't already there
#if not os.path.isfile(LOCAL_FILE):
    # Download the file and save it to LOCAL_FILE
    #urlretrieve(URL, LOCAL_FILE)
    
   #Matching patterns to lines
   match.group(0)
    match.group(3) 
    timestamp = match.group(3)
    month = timestamp[3:6]
    months_count[month] += 1
    match.group(7) 
    
 #This is what actually does all the work and find the matches in the file such as requests each month or most requested form.
   if (match.group(7)[0] == "3"):
        redirectCounter += 1
    elif (match.group(7)[0] == "4"):
        errorCounter += 1
    if (month == "Jan"): 
        janlogs.write(line)
    elif (month == "Feb"): 
        feblogs.write(line)
    elif (month == "Mar"): 
        marlogs.write(line)
    elif (month == "Apr"): 
        aprlogs.write(line)
    elif (month == "May"): 
        maylogs.write(line)
    elif (month == "Jun"): 
        junlogs.write(line)
    elif (month == "Jul"): 
        jullogs.write(line)
    elif (month == "Aug"): 
        auglogs.write(line)
    elif (month == "Sep"): 
        seplogs.write(line)
    elif (month == "Oct"): 
        octlogs.write(line)
    elif (month == "Nov"): 
        novlogs.write(line)
    elif (month == "Dec"): 
        declogs.write(line)
    
   else:
        continue
#This is what is going to go and print the answers to the questions for the assignment and display it to us
print("Request Made")
print(file_len(LOCAL_FILE))
totalResponses = file_len(LOCAL_FILE)
print("Average number for month:", round(totalResponses/12,2))
print("Average number for week: ",round(totalResponses/52,2))
print("Average number for day: ", round(totalResponses/365,2))
print("Month Count:", months_count)
print("Total number of redirects:",redirectCounter)
print("Percentage of all requests that were redirects (3xx): {0:.2%}".format(redirectCounter/totalResponses))
print("Total number of Errors:",errorCounter)
print("Percentage of client error (4xx) requests: {0:.2%}".format(errorCounter/totalResponses))	
fileCount()

#end of assignment
