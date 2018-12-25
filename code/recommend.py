#recommend.py
import turicreate as tc

### MAKING A RECOMMENDATION 
def recommend(twitt_id):
	twitt_id = ''
	last_line = [twitt_id,'','','']

	animes = tc.SFrame.read_csv('anime.csv')
	ratings = tc.SFrame.read_csv('ratings.csv')

	## new data
	training_data_n, validation_data_n = tc.recommender.util.random_split_by_user(ratings, 'user_id', 'anime_id')
	model = tc.recommender.create(training_data_n, 'user_id', 'anime_id')

	## get the recommendation
	results = model.recommend([twitt_id], k= 5)
	print(results)

	## prints + adds the recommendations
	anime_titles = []
	anime_rec_ids = results['anime_id']

	for id_m in anime_rec_ids:   
	    anime_titles.append(animes[animes['anime_id'] == id_m]['name'])
	    ## print(animes[animes['anime_id'] == id_m], '\n')
	## print(anime_titles) <-- if want to see all the animes

	### RECOMMENDATION SENT BACK TO THE USER
	twitt_reply = ''
	for rec in anime_titles:
	    for i in range(len(rec)):
	        k = i+1
	        twitt_reply += '#',i ," : ", rec[i]

	return(twitt_reply)





