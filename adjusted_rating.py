import os
import basketball_reference_web_scraper as scraper
from basketball_reference_web_scraper import client

data = '''
<html>
<div id='main'>
  <div id='sub1'>thisis1</div>
  <!--
    comment
  -->
  <div id='sub2'>thisis2</div>
</div>
</html>
'''
from lxml import html
tree = html.fromstring(data)
print(tree.xpath("//div[@id='sub1']")[0].text)
print(tree.xpath("//div[@id='sub2']")[0].text)


print('\n\n\n')

with open('/tmp/b') as f:
  data = f.read()

tree = html.fromstring(data)
print(tree.xpath("//div"))
print([str(x.get('id')) + x.get('class') for x in tree.xpath("//div")])

fourfactor_text = tree.xpath("//comment()")[0].text
print('ff text:\n\n' + fourfactor_text)

tree2 = html.fromstring(fourfactor_text)
print(tree2)
print(tree2.get('id'))
print('ff:\n' + str(tree2.xpath("//table[@id='four_factors']")))
print('trs:\n' + str(tree2.xpath("//table[@id='four_factors']/tr")))
print([x.get('class') for x in tree2.xpath("//table[@id='four_factors']/tr")])
print('tr[class=='']:\n' + str(tree2.xpath("//table[@id='four_factors']/tr[not(@class)]")))

#TODO: this is also available in the "Advanced Box Score Stats" -> "Team Totals"

#exit(0)

#print(scraper)
#print(help(scraper))
#print(help(client))

def load_schedule():
	if os.path.exists('/tmp/sched'):
		pass
    #TODO: read from this
	schedule = client.season_schedule(2020)



#schedule = load_schedule()
# First day of season is Oct 22, 2019.

scores = client.team_box_scores(22, 10, 2019)
print(scores[0])
