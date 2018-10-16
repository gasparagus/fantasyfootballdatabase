import nflgame
import csv
import os
import remove_columns as rc
import datetime as dt
import postgres_ongoing_additions as pg
import pandas as pd

current_year = dt.datetime.today().year
# Year set to current so so that truncate and reload only happens for current year
years = [x for x in range(2018, current_year+1)]
weeks = [x for x in range(1,18)]

for year in years:
	for week in weeks:
		try:
			nflgame.combine_max_stats(nflgame.games(year, week=week)).csv(str(year)+'_'+str(week)+'.csv',allfields=True)
		except:
			pass

rc.clean_columns()
pg.load_table()
pg.update_points()

# Dump data to desktop
data = pd.read_sql('select * from fantasy.stats where year = 2018 and pos in (\'RB\', \'QB\', \'WR\', \'TE\')', con='postgresql://postgres:labella@localhost:5432/fantasy')
data.to_csv('C:\Users\Gary\Desktop\\2018_nfl_data.csv', index=False)