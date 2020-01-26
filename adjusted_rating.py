import os

#virtualenv -p python3 env
#source env/bin/activate
#pip3 install -r ../basketball_reference_web_scraper/requirements.txt

import sys
sys.path.append("/usr/local/google/home/tjredekopp/projects/basketball_reference_web_scraper")

import basketball_reference_web_scraper as scraper
from basketball_reference_web_scraper import client


def load_schedule():
	if os.path.exists('/tmp/sched'):
		pass
    #TODO: read from this
	schedule = client.season_schedule(2020)



#schedule = load_schedule()
# First day of season is Oct 22, 2019.

scores = client.team_box_scores(22, 10, 2019)
print(scores[0])
