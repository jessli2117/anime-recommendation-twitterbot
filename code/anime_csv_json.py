### Parse the html file

import urllib.request
from bs4 import BeautifulSoup
from collections import OrderedDict
import json
import csv

anime_csv = open('anime.csv', 'rt', encoding = 'utf-8')
#ratings_csv = open('ratings.csv', 'rt', encoding = 'utf-8')

anime_json = open('anime.json', 'w')
#ratings_json = open('ratings.json', 'w')

anime_fields = ("anime_id","name","genre","type","episodes","rating","members")
anime_reader = csv.DictReader(anime_csv, anime_fields)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')