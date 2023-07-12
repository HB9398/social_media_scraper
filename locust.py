import os
import tweepy as tw
import pandas as pd
consumer_key= &#39;nLPRDSP0wQfjLbJsm7wk54zXO&#39;
consumer_secret= &#39;UFMinuIYEWDAtHMtVIiHedqzoLnwyJ8aBXxOyO3oZfduB5sgH8&#39;
access_token= &#39;1276869412432130048-D4v40owVsXviU8rzWqRUGNjmZpTbvz&#39;
access_token_secret= &#39;wO3ZqKAuKJljpA5vQ7w28K7UEkMuCri8erbgwYDX8DSPj&#39;

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)
search_words = &quot;#locusts&quot;
date_since = &quot;2020-1-1&quot;
tweets = tw.Cursor(api.search,
q=search_words,
lang=&quot;en&quot;,
since=date_since,include_entities=True).items(2000)
tweets
#&lt;tweepy.cursor.ItemIterator at 0x7fafc296e400&gt;
# Collect tweets