import tweepy, json, csv, sys
import credentials
import recommend

def addRating_CSV(twitt_id, rating, anime):
  #find the anime
  anime_id = 0
  anime_csv = csv.reader(open('anime.csv', "rb"), delimiter=",")
  for a_index in range(i,len(anime_csv)):
    row = anime_csv[a_index]
    if(anime.lowercase() in row[1].lowercase()):
      anime_id = a_index
      break
  if(anime_id != 0):
    newRow = "\n%s,%s,%s" % (twitt_id, anime_id, rating)
    with open('ratings.csv', 'a') as f:
        f.write(newRow)

def recommendations(twitt_id):
  recommend(twitt_id)

def newPerson(num_ex, twitt_id):
  if(num_ex == 1):
    recommend(twitt_id)
  else:
    #ask if want to add ratings

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print (user.name)



###FINDS THE USERS THAT HAVE MENTIONED THE BOT

####
# Define the search
#####
query = '@AnimeRecUwU'
max_tweets = 100

####
# Do the search
#####

new_tweets = api.search(q=query, count=count, max_id=str(last_id - 1), since_id=str(last_visited))
searched_tweets = []
last_id = new_tweets[-1].id
updateLastVisited(new_tweets[0].id)

while len(searched_tweets) < max_tweets:
    count = max_tweets - len(searched_tweets)
    try:
        new_tweets = api.search(q=query, count=count, max_id=str(last_id - 1))
        if not new_tweets:
            break
        searched_tweets.extend(new_tweets)
        last_id = new_tweets[-1].id
    except tweepy.TweepError as e:
        # depending on TweepError.code, one may want to retry or wait                                                                                                                 
        # to keep things simple, we will give up on an error                                                                                                                          
        break


####
# Iterate over the search
#####
for status in searched_tweets:
  # do something with all these tweets                                                                                                                                                
  print	(status.text)

  if(status.id in tweet_data['id']): ## check the tweets that already exist, if it does. ignore
    continue
  for i in spot_data:

    #If the person is a beginner. Just give general recommendations
    if("1" in status.text):
      obj = recommendations(status.author)
      api.update_status(obj+' @' + status.author.screen_name, status.id_str)
      

    #If the person is an intermediate then read for the animes already that have been watched
    if('2' in status.text):
       new_ratings = status.text.split(";")
       new_ratings = new_ratings[1:]
       for anime in new_ratings:
        id_rate_anime = anime.split(",")
        author_id = id_rate_anime[0]
        rating_insert = id_rate_anime[1]
        anime_insert = id_rate_anime[2]
        addRating_CSV(author_id, rating_insert, anime_insert)

      obj = recommendations(status.author_id)
      api.update_status(obj+' @' + status.author.screen_name, status.id_str)


