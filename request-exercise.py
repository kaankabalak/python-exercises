import requests
r = requests.get('https://www.mysportsfeeds.com/api/feed/pull/nba/2016-2017-regular/cumulative_player_stats.json?player=harden&playerstats=FG%25,FT%25,PTS/G,3PM/G,REB/G,AST/G,STL/G,BS/G,TOV/G')
print r