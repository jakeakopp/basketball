import os

#virtualenv -p python3 env
#source env/bin/activate
#pip3 install -r ../basketball_reference_web_scraper/requirements.txt

import csv
from datetime import date, datetime, timedelta
import sys
sys.path.append("/usr/local/google/home/tjredekopp/projects/basketball_reference_web_scraper")

import basketball_reference_web_scraper as scraper
from basketball_reference_web_scraper import client


def load_scores():
  filename = 'ratings.csv'
  if os.path.exists(filename):
    f = open(filename)
    reader = csv.reader(f)
    rows = []
    for row in reader:
      rows.append(row)
    return rows

  # First day of season is Oct 22, 2019.
  d = date(2019, 10, 22)
  end_date = date(2019, 10, 22) + timedelta(days=2)
#  end_date = datetime.now() - timedelta(days=1)

  games = []
  while d < end_date:
    print('Loading scores for %s.' % d)
    scores = client.team_box_scores(d.day, d.month, d.year)
    if len(scores) % 2 != 0:
      raise Exception('Odd number of scores on %s!' % d)
    i = 0
    while i < len(scores):
      away_stats = scores[i]
      home_stats = scores[i+1]
      games.append([away_stats['team'].name, away_stats['offensive_rating'],
                    home_stats['team'].name, home_stats['offensive_rating']])
      i += 2
    d += timedelta(days=1)

  f = open('ratings.csv', 'w')
  w = csv.writer(f)
  for game in games:
    w.writerow(game)

  f.close()
  return games


games = load_scores()
print(games)
