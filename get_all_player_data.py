import nflgame
import csv
import os
import remove_columns as rc
import datetime as dt

current_year = dt.datetime.today().year
years = [x for x in range(2009,current_year)]
weeks = [x for x in range(1,18)]

for year in years:
	for week in weeks:
		nflgame.combine_max_stats(nflgame.games(year, week=week)).csv(str(year)+'_'+str(week)+'.csv',allfields=True)
'''
		inputs = open(str(year)+'_'+str(week)+'.csv', 'rb')
		outputs = open(str(year)+'_Week_'+str(week)+'.csv', 'wb')
		writer = csv.writer(outputs)
		for row in csv.reader(inputs):
			if row:
				writer.writerow(row)
		inputs.close()
		outputs.close()
'''

rc.clean_columns()
