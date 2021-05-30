import tweepy
from tweepy import OAuthHandler
import json
from time import sleep
from newsapi import NewsApiClient
from keyss import *


objeto = tweepy.OAuthHandler(consumer_key,consumer_secret)
objeto.set_access_token(access_token,access_token_secret)

api = tweepy.API(objeto,wait_on_rate_limit=True) 


                        #BUSCAR UN TWEET CON PALABRA COMO FILTRO  #como leer las propiedades del tw?: #tweet_data = json.dumps(tweet._json,indent=4)
FOLLOW= True
for tweet in tweepy.Cursor(api.search,q="Python Programming",tweet_mode="extended").items(20):
    try:
                                #darle like a un tweet
        tweet_id = tweet._json["id"]
        api.create_favorite(tweet_id)                  
        print("He dado like al tweet ID:  " , tweet_id)
        
                                #seguir al usuario del tweet
        if FOLLOW:
            if not tweet.user.following:
                user_id = tweet._json["user"]["screen_name"]
                api.create_friendship(screen_name=user_id)
                print("Ahora sigo al usuario   @" , user_id)
                print("")
            else:
                print("Ya seguia al usuario que publico el tweet")
                print("")
    except:
        pass

                            

api_news = NewsApiClient(api_key= a_key)
datanews = api_news.get_everything(q="Tecnología Informatica",language= "es",page_size=3)
articulosdeldia = datanews["articles"]

for articulo in articulosdeldia:
    url = articulo["url"]
    api.update_status("#Tecnología " + url)
    print("-NOTICIA TWITTEADA-")
    sleep(3)
