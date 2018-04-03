import tweepy #https://github.com/tweepy/tweepy
import csv

#Credenciales de API TWITTER
consumer_key = " "
consumer_secret = " "
access_key = " "
access_secret = " "


def get_all_tweets(screen_name):
    
    #3205 Tweets
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)


    alltweets = []  

    new_tweets = api.user_timeline(screen_name = screen_name,count=200)

    alltweets.extend(new_tweets)

    oldest = alltweets[-1].id - 1

    while len(new_tweets)>0:
       
        print "Extrayendo tweets %s" % (oldest)

        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)

        alltweets.extend(new_tweets)

        oldest = alltweets[-1].id - 1

        print "...%s descargando tweets" % (len(alltweets))

    outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]

    # Guardadndo en archivo csv 
    with open('%s_tweets.csv' % screen_name, 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(["ID","Fecha","Texto"])
        writer.writerows(outtweets)

    pass

if __name__ == '__main__':
    #Usuario de Twitter
    get_all_tweets("nicolasmaduro")
