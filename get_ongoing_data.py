import nflgame
import csv
import os
import remove_columns as rc
import datetime as dt

# Try this once the current season starts. The 2017 season starts on 9/7/2017 which is week 36
# but the final game of the week (Monday) is on week 37. You should probably run the script on
# Tuesday and take that week number as a base.
current_year = dt.datetime.today().year
current_full_date = dt.datetime.now()
current_week_number = current_full_date.isocalendar()[1]

# May need to update next year if the week depending on when the season ends.
nfl_season_weeks = [x for x in range(1,18)]
week_2017 = [x for x in range(37,53)]
# Add week 1 to end of 2017 list since file wont run until 1/2 (week 1)
week_2017.append(1)
week_mappings = zip(week_2017,nfl_season_weeks)

current_nfl_week = [week[1] for week in week_mappings if week[0] == current_week_number]

# Delete next line if script works in the beginning of season.
#nflgame.combine_max_stats(nflgame.games(current_year, week=week_number)).csv(str(current_year)+'_'+str(week_number)+'.csv',allfields=True)
nflgame.combine_max_stats(nflgame.games(current_year, week=current_nfl_week)).csv(str(current_year)+'_'+
		str(current_nfl_week)+'.csv',allfields=True)

# Run cleanup of columns.
rc.clean_columns()