# Project3
Repo for project3
# This was made by Tristan Zoeller and Armand Bradford.

from urllib.request import urlretrieve
import os
import re
import collections 

# This goes and gets the file we need for the assignment.
redirectCounter = 0
errorCounter = 0
URL = 'https://s3.amazonaws.com/tcmg476/http_access_log'
# This is where our file will be saved and what it will be called so we can find it later if needed.
LOCAL_FILE = 'http_access_log'
