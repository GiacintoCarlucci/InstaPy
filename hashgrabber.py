# https://www.codeforests.com/2020/10/18/passing-arguments-to-python-script/
import argparse
import os
import json
from datetime import date
from collections import Counter
from pprint import pprint

def goToSaveFolder(username):
    if os.path.isdir('hashtags') is False:
        os.mkdir('hashtags')
    os.chdir('hashtags')
    if os.path.isdir(username) is False:
        os.mkdir(username)
    os.chdir(username)
    if os.path.isdir('mostcommon') is False:
        os.mkdir('mostcommon')
    os.chdir('mostcommon')

def extractHashtags(path):
    hashtags = []
    with open(path, encoding='utf8') as f:
        for line in f:
            splittedLine = line.strip().split()
            for word in splittedLine:
                if (word.startswith("#")):
                    for hashtag in word.split("#"):
                        hashtag = hashtag.strip('"').strip('\'')
                        if(hashtag):
                            hashtags.append(hashtag)
    return hashtags

def countHashtags(hashtags):
    return Counter(hashtags).most_common()[:100]

def save(hashtags, username):
    goToSaveFolder(username)
    filename = str(date.today())+'.json'
    with open(filename,'w') as jsonFile:
        json.dump(countHashtags(hashtags),jsonFile)

def tagsReport(username, path):
    hashtags = []
    print("Analyzing " + username  + "'s logs...")
    hashtags = extractHashtags(path)
    save(hashtags,username)
