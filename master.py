import random
from routines import *
from hashgrabber import *
from randomhashtags import *
bestTags = [
"travelphotography",
"travel",
"travelgram",
"travelgramitalia",
"travelblogger",
"travelbloggeritaliane",
"travelblog",
"travelawesome",
"traveltheworld",
"traveladdict",
"travellife",
"traveldiary",
"traveldeeper",
"travelholic",
"postcardsfromtheworld",
"wanderlust",
"earthpix",
"trip",
"travelsolo",
"beautifuldestinations",
"vacation",
"trekking",
"trekkingitalia",
"trekkinglovers",
"hiking",
"hikingitaly",
"discoverearth",
"beautifulplaces",
"iamatraveler",
"doyoutravel",]
#tags = getRandomHashtags()
randomFive = random.sample(bestTags,5)
print(randomFive)
likeByTags(randomFive)
tagsReport()

