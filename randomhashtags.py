import os
import random
import json

def getRandomHashtags():
    basePath = './hashtags/mostcommon/'
    firstFile = sorted(os.listdir(basePath),reverse=True)[0]
    path = basePath + firstFile
    print('getting 5 random hashtags from: ', path)
    loadedArray = []
    with open(path,'r') as jsonFile:
        loadedArray = json.load(jsonFile)
    choices = random.choices(loadedArray, k=5)
    hashtags = []
    for couple in choices:
        hashtags.append(couple[0])
    print(hashtags)
    return hashtags

