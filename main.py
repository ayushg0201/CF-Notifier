# importing the requests library
import requests
import time
from gtts import gTTS
import os

handle = input('ENTER YOUR CODEFORCES HANDLE : \n')

URL = "https://codeforces.com/api/user.status?handle=" + handle + "&from=1&count=1"
print(URL)

# sending get request and saving the response as response object
r = requests.get(url = URL)

# extracting data in json format
data = r.json()

prevSubmissionTime = data['result'][0]['creationTimeSeconds']
language = 'en'


while 1:
# sending get request and saving the response as response object
    r = requests.get(url = URL)

# extracting data in json format
    data = r.json()

    if prevSubmissionTime < data['result'][0]['creationTimeSeconds'] and data['result'][0]['verdict'] != 'TESTING' : 
        mytext = data['result'][0]['verdict']
        
        s = ""
        for i in range(0, len(mytext)):
            if mytext[i] == '_':
                s += ' '
            else:
                s += mytext[i]
        print(s)
        myobj = gTTS(text= s, lang=language, slow= True)
        myobj.save("welcome.mp3")
        os.system("mpg321 welcome.mp3")
        prevSubmissionTime = data['result'][0]['creationTimeSeconds']
        print('hello')

    time.sleep(0.2)

"""

[{'id': 128768322, 'contestId': 1566, 'creationTimeSeconds': 1631566427, 'relativeTimeSeconds': 2147483647, 'problem': {'contestId': 1566, 'index': 'E', 'name': 'Buds Re-hanging', 'type': 'PROGRAMMING', 'points': 2000.0, 'tags': ['constructive algorithms', 'dfs and similar', 'dp', 'greedy', 'trees']}, 'author': {'contestId': 1566, 'members': [{'handle': 'noobiesAG'}], 'participantType': 'PRACTICE', 'ghost': False, 'startTimeSeconds': 1631457300}, 'programmingLanguage': 'GNU C++17 (64)', 'verdict': 'WRONG_ANSWER', 'testset': 'TESTS', 'passedTestCount': 2, 'timeConsumedMillis': 155, 'memoryConsumedBytes': 33689600}]

"""
