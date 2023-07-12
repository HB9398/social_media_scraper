import os
import tweepy as tw
import pandas as pd
consumer_key= ''
consumer_secret= ''
access_token= ''
access_token_secret= ''

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)
search_words = "#locusts"
date_since = "2020-1-1"
tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since,include_entities=True).items(2000)
tweets
#<tweepy.cursor.ItemIterator at 0x7fafc296e400>
# Collect tweets


#image
#for status in tweets:
 #   media = status.entities.get('media', [])
  #  if(len(media) > 0):
   #     print("PIX")
    #else:
     #   print("No pix")
   
users_locs = [[tweet.user.screen_name,tweet.user.location,tweet.coordinates ] for tweet in tweets]
#last_words = users_locs.applymap(lambda x: x.split()[-1])
users_locs
tweet_text = pd.DataFrame(data=users_locs, 
                    columns=['user', "location", "Coordinates"])
tweet_text

test_list = tweet_text.location
for i in range(len(test_list)):
    test_list[i] = test_list[i].lower()
from collections import Counter 
 
res = dict(Counter(i for i in test_list)) 

print(res)
newDict = dict()
# Iterate over all the items in dictionary and filter items which has even keys
for (key, value) in res.items():
   if value > 2:
       newDict[key] = value
#print('Filtered Dictionary : ')

import matplotlib.pyplot as plt
import numpy as np
#plt.hist(Counter(i for i in test_list), 
f, ax = plt.subplots(figsize=(18,5)) 
ax.legend(fontsize = 8)
plt.bar(newDict.keys(), newDict.values(), color='g')

 
from opencage.geocoder import OpenCageGeocode

key = ''
geocoder = OpenCageGeocode(key)

lon=[]
lat=[] 
for i in test_list:
    
    query = "u"+i 
    
    results = geocoder.geocode(query)

    if results and len(results):
        longitude = results[0]['geometry']['lng']
        lat.append(longitude)
        latitude  = results[0]['geometry']['lat']
        lon.append(latitude)
        #print(u'%f;%f;' % (latitude, longitude))
    #else:
        #print("lol")
        # 40.416705;-3.703582;Madrid,Spain
print("Done")        


%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import pandas as pd
import math 

fig = plt.figure(figsize=(15,15))

m = Basemap(projection='merc', 
              lat_0=0, lon_0=0,
              llcrnrlat=-80,urcrnrlat=80,llcrnrlon=-180,urcrnrlon=180)

m.drawmapboundary(fill_color='aqua')
m.fillcontinents(color='coral',lake_color='aqua')
m.drawcoastlines()

#m.drawcoastlines(color='gray')
#m.drawcountries(color='gray')
#m.drawstates(color='gray')
#print(lon,"\t",lat)
# 2. scatter city data, with color reflecting population
# and size reflecting area
for i in range(0,len(lat)):
    
    
    m.tissot( lat[i], lon[i], 1, 50)
    
    #m.scatter(lon[i], lat[i], marker='D',color='WHITE')

# 3. create colorbar and legend


# make legend with dummy points
for a in [100, 300, 500]:
    plt.scatter([], [], c='k', alpha=0.5, s=a,
                label=str(a) + ' km$^2$')
plt.legend(scatterpoints=1, frameon=False,
           labelspacing=1, loc='lower left');
plt.show()
 
