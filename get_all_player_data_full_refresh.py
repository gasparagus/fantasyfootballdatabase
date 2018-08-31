import nflgame
import csv
import os
import remove_columns as rc
import datetime as dt
import postgres_ongoing_additions as pg

current_year = dt.datetime.today().year
# Year set to current so so that truncate and reload only happens for current year
years = [x for x in range(2018, current_year)]
weeks = [x for x in range(1,18)]

for year in years:
	for week in weeks:
		nflgame.combine_max_stats(nflgame.games(year, week=week)).csv(str(year)+'_'+str(week)+'.csv',allfields=True)

rc.clean_columns()
pg.load_table()
pg.update_points()
