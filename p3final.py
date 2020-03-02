# Project3
# Repo for project3
# This was made by Tristan Zoeller and Armand Bradford.

from urllib.request import urlretrieve
import os
import re
import collections

redirectCounter = 0
errorCounter = 0
# URL of the file
URL = 'https://s3.amazonaws.com/tcmg476/http_access_log'
# Where to save our log file and what its called
LOCAL_FILE = 'local_copy.log'

# This assigns a value to each month
months_count = {
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

janlogs = open("january.txt", "a+");
feblogs = open("february.txt", "a+");
marlogs = open("march.txt", "a+");
aprlogs = open("april.txt", "a+");
maylogs = open("may.txt", "a+");
junlogs = open("june.txt", "a+");
jullogs = open("july.txt", "a+");
auglogs = open("august.txt", "a+");
seplogs = open("september.txt", "a+")
octlogs = open("octlogs.txt", "a+");
novlogs = open("november.txt", "a+");
declogs = open("december.txt", "a+")

i = 0


def file_len(LOCAL_FILE):
    with open(LOCAL_FILE) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


# find all files that are inbetween GET requests and HTTP protocols"

def fileCount():
    filelog = []
    leastcommon = []
    with open(LOCAL_FILE) as logs:
        for line in logs:
            try:
                filelog.append(line[line.index("GET") + 4:line.index("HTTP")])
            except:
                pass
    counter = collections.Counter(filelog)
    # checking for file requests that only occur once because they may be the ones that get the least amount of requests
    for count in counter.most_common(1):
        print("Most commonly requested file: {} with {} requests.".format(str(count[0]), str(count[1])))
    for count in counter.most_common():
        if str(count[1]) == '1':
            leastcommon.append(count[0])
    if leastcommon:
        # there are a lot of files that only happen once in the entire file
        response = input(
            "It seem's there are {} file(s) that were requested only once, show all? (y/n)".format(len(leastcommon)))
        if response == 'y' or response == 'Y':
            for file in leastcommon:
                print(file)


# If the file isn't already there
if not os.path.isfile(LOCAL_FILE):
    # Download the file and save it to local_file
    urlretrieve(URL, LOCAL_FILE)

# Our regex that we are using
pattern = r'(.*?) - (.*) \[(.*?)\] \"(.*?) (.*?)\"? (.+?) (.+) (.+)'

# Create a list with each line from the file
lines = open(LOCAL_FILE, 'r').readlines()

# This is the most important part of our code. It goes through and finds all the matches that we are looking for.
for line in lines:
    # Match the patterns to the lines so we can answer the questions in the assignment
    match = re.match(pattern, line)

    # This is for if there is no match
    if not match:
        continue

    # You can get all the info you need from the match groups we created a second ago
    # original line
    match.group(0)
    # timestamp
    match.group(3)
    timestamp = match.group(3)
    month = timestamp[3:6]
    months_count[month] += 1
    match.group(7)
    # This is the code
    # This is what actually does all the work to go through the file and match up the things we are looking for in the file we were given for the asignment.
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
# This is what prints out the asnwers to the questions we are answering for the assignment and is displayed in the output panel of VS code.
print("Request Made")
print(file_len(LOCAL_FILE))
totalResponses = file_len(LOCAL_FILE)
print("Month AVG:", round(totalResponses / 12, 2))
print("Week AVG: ", round(totalResponses / 52, 2))
print("Daily AVG: ", round(totalResponses / 365, 2))
print("Month Count:", months_count)
print("Redirects:", redirectCounter)
print("Redirect Percentage (3xx): {0:.2%}".format(redirectCounter / totalResponses))
print("Errors:", errorCounter)
print("Client error (4xx) requests: {0:.2%}".format(errorCounter / totalResponses))
fileCount()
# End of assignment