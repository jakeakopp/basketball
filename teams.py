from lxml import html

from basketball_reference_web_scraper.data import TEAM_NAME_TO_TEAM
from basketball_reference_web_scraper.utilities import str_to_float
from basketball_reference_web_scraper.utilities import str_to_int


def parse_team_total(footer, adv_footer, team):
    cells = footer.xpath('tr/td')
    adv_cells = adv_footer.xpath('tr/td')
    return {
        "team": team,
        "minutes_played": str_to_int(cells[0].text_content()),
        "made_field_goals": str_to_int(cells[1].text_content()),
        "attempted_field_goals": str_to_int(cells[2].text_content()),
        "made_three_point_field_goals": str_to_int(cells[4].text_content()),
        "attempted_three_point_field_goals": str_to_int(cells[5].text_content()),
        "made_free_throws": str_to_int(cells[7].text_content()),
        "attempted_free_throws": str_to_int(cells[8].text_content()),
        "offensive_rebounds": str_to_int(cells[10].text_content()),
        "defensive_rebounds": str_to_int(cells[11].text_content()),
        "assists": str_to_int(cells[13].text_content()),
        "steals": str_to_int(cells[14].text_content()),
        "blocks": str_to_int(cells[15].text_content()),
        "turnovers": str_to_int(cells[16].text_content()),
        "personal_fouls": str_to_int(cells[17].text_content()),
        "personal_fouls": str_to_int(cells[17].text_content()),
        "true_shooting_percentage": str_to_float(adv_cells[1].text_content()),
        "effective_field_goal_percentage": str_to_float(adv_cells[2].text_content()),
        "three_point_attempt_rate": str_to_float(adv_cells[3].text_content()),
        "free_throw_attempt_rate": str_to_float(adv_cells[4].text_content()),
        "offensive_rebound_percentage": str_to_float(adv_cells[5].text_content()),
        "defensive_rebound_percentage": str_to_float(adv_cells[6].text_content()),
        "total_rebound_percentage": str_to_float(adv_cells[7].text_content()),
        "assist_percentage": str_to_float(adv_cells[8].text_content()),
        "steal_percentage": str_to_float(adv_cells[9].text_content()),
        "block_percentage": str_to_float(adv_cells[10].text_content()),
        "turnover_percentage": str_to_float(adv_cells[11].text_content()),
        "offensive_rating": str_to_float(adv_cells[13].text_content()),
        "defensive_rating": str_to_float(adv_cells[14].text_content()),
    }


def parse_team_totals(page):
    with open('/tmp/asdf', 'w') as f:
      f.write(page.decode('utf-8'))
    tree = html.fromstring(page)
    teams = [
        TEAM_NAME_TO_TEAM[anchor.text_content().upper()]
        for anchor in tree.xpath('//div[@class="scorebox"]//a[@itemprop="name"]')
    ]
    tables = tree.xpath('//table[contains(@class, "stats_table")]')
    footers = [
        footer
        for table in tables
        if "game-basic" in table.attrib["id"]
        for footer in table.xpath("tfoot")
    ]
    adv_footers = [
        footer
        for table in tables
        if "game-advanced" in table.attrib["id"]
        for footer in table.xpath("tfoot")
    ]
    ret = []
    for i in range(len(footers)):
        x = parse_team_total(footer=footers[i],adv_footer=adv_footers[i], team=teams[i])
        ret.append(x)

    return ret

