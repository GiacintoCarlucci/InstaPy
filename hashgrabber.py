# https://www.codeforests.com/2020/10/18/passing-arguments-to-python-script/
import argparse
import os
import json
from datetime import date
from collections import Counter
from pprint import pprint

def goToSaveFolder():
    if os.path.isdir('hashtags') is False:
        os.mkdir('hashtags')
    os.chdir('hashtags')
    if os.path.isdir('mostcommon') is False:
        os.mkdir('mostcommon')
    os.chdir('mostcommon')

def parseArgs():
    global PATH
    global USER
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', help='user to search for logs')
    args = parser.parse_args()
    USER = args.u
    if(USER != None):
        PATH = './logs/' + args.u + '/general.log'
    else:
        PATH = './logs/' + os.listdir('./logs/')[0] + '/general.log'
        USER = os.listdir('./logs/')[0]

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

def save(hashtags):
    goToSaveFolder()
    filename = str(date.today())+'.json'
    with open(filename,'w') as jsonFile:
        json.dump(countHashtags(hashtags),jsonFile)



USER = ''
PATH = ''

def tagsReport():
    hashtags = [] 
    parseArgs()
    print("Analyzing " + USER  + "'s logs...")
    hashtags = extractHashtags(PATH)
    save(hashtags)
