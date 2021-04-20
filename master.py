import argparse
import random
from routines import *
from hashgrabber import *
from randomhashtags import *
from appModules import constants

global PATH
global USER

parser = argparse.ArgumentParser()
parser.add_argument('-u', help='user to search for logs')
args = parser.parse_args()
USER = args.u

if(USER != None):
    PATH = './logs/' + constants.profiles[USER]["username"] + '/general.log'
else:
    PATH = './logs/' + os.listdir('./logs/')[0] + '/general.log'
    USER = os.listdir('./logs/')[0]


username = constants.profiles[USER]["username"]
password = constants.profiles[USER]["password"]
tags = random.sample(constants.profiles[USER]["bestHashtags"],5)

print(tags)

likeByTags(tags, username, password)
tagsReport(username, PATH)

