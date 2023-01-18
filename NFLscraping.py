import pandas as pd
import re
import requests


x = "C:/Users/klick/OneDrive/Documents/NflDataStuff/NFLdatasheet16.csv"









teamNames = {'BUF':'Buffalo Bills', 'NE':'New England Patriots', 'MIA': 'Miami Dolphins', 'NYJ':'New York Jets', 'TEN':'Tennessee Titans', 
'IND':'Indianapolis Colts', 'HOU':'Houston Texans', 'JAX':'Jacksonville Jaguars', 'CIN':'Cincinnati Bengals',
            'PIT':'Pittsburgh Steelers', 'CLE':'Cleveland Browns', 'BAL':'Baltimore Ravens', 'KC':'Kansas City Chiefs', 
            'OAK':'Oakland Raiders', 'LAC':'Los Angeles Chargers', 'SD':'San Diego Chargers', 'DEN':'Denver Broncos', 'DAL':'Dallas Cowboys',
            'PHI':'Philadelphia Eagles', 'WAS':'Washington Redskins', 
            'NYG':'New York Giants', 'TB':'Tampa Bay Buccaneers', 'NO':'New Orleans Saints', 
            'ATL':'Atlanta Falcons', 'CAR':'Carolina Panthers', 'GB':'Green Bay Packers', 'MIN':'Minnesota Vikings', 
            'CHI':'Chicago Bears', 'DET':'Detroit Lions', 'LAR':'Los Angeles Rams', 'STL':'St. Louis Rams', 
            'ARI':'Arizona Cardinals', 'SF':'San Francisco 49ers', 'SEA':'Seattle Seahawks'}



def shareDivision(teamCode, team2, year):
    divisions = None
    team1 = teamNames[teamCode]
    if year == '2001':
        divisions = [['New England Patriots', 'Miami Dolphins', 'New York Jets', 'Indianapolis Colts', 'Buffalo Bills'], 
        ['Pittsburgh Steelers', 'Baltimore Ravens', 'Cleveland Browns', 'Tennessee Titans', 'Jacksonville Jaguars', 'Cincinnati Bengals'],
        ['Oakland Raiders', 'Seattle Seahawks', 'Denver Broncos', 'Kansas City Chiefs', 'San Diego Chargers'], 
        ['Philadelphia Eagles', 'Washington Redskins', 'New York Giants', 'Arizona Cardinals', 'Dallas Cowboys'],
        ['Chicago Bears', 'Green Bay Packers', 'Tampa Bay Buccaneers', 'Minnesota Vikings', 'Detroit Lions'],
        ['St. Louis Rams', 'San Francisco 49ers', 'New Orleans Saints', 'Atlanta Falcons', 'Carolina Panthers']]
    else:
        divisions = [['New England Patriots', 'Miami Dolphins', 'New York Jets', 'Buffalo Bills'], 
        ['Pittsburgh Steelers', 'Baltimore Ravens', 'Cleveland Browns', 'Cincinnati Bengals'],
        ['Tennessee Titans', 'Indianapolis Colts', 'Jacksonville Jaguars', 'Houston Texans'],
        ['Oakland Raiders', 'Denver Broncos', 'Kansas City Chiefs', 'San Diego Chargers', 'Los Angeles Chargers'], 
        ['Philadelphia Eagles', 'Washington Redskins', 'New York Giants', 'Dallas Cowboys'],
        ['Chicago Bears', 'Green Bay Packers', 'Minnesota Vikings', 'Detroit Lions'],
        ['Tampa Bay Buccaneers', 'Atlanta Falcons', 'New Orleans Saints', 'Carolina Panthers'], 
        ['St. Louis Rams', 'Los Angeles Rams', 'San Francisco 49ers', 'Seattle Seahawks', 'Arizona Cardinals']]
    for division in divisions:
        if (team1 in division) and (team2 in division):
            return True
    return False

def shareConference(teamCode, team2, year):
    Conferences = None
    team1 = teamNames[teamCode]
    if year == '2001':
        Conferences = [['New England Patriots', 'Miami Dolphins', 'New York Jets', 'Indianapolis Colts', 'Buffalo Bills', 
        'Pittsburgh Steelers', 'Baltimore Ravens', 'Cleveland Browns', 'Tennessee Titans', 'Jacksonville Jaguars', 'Cincinnati Bengals',
        'Oakland Raiders', 'Seattle Seahawks', 'Denver Broncos', 'Kansas City Chiefs', 'San Diego Chargers'], 
        ['Philadelphia Eagles', 'Washington Redskins', 'New York Giants', 'Arizona Cardinals', 'Dallas Cowboys',
        'Chicago Bears', 'Green Bay Packers', 'Tampa Bay Buccaneers', 'Minnesota Vikings', 'Detroit Lions',
        'St. Louis Rams', 'San Francisco 49ers', 'New Orleans Saints', 'Atlanta Falcons', 'Carolina Panthers']]
    else:
        Conferences = [['New England Patriots', 'Miami Dolphins', 'New York Jets', 'Buffalo Bills', 
        'Pittsburgh Steelers', 'Baltimore Ravens', 'Cleveland Browns', 'Cincinnati Bengals',
        'Tennessee Titans', 'Indianapolis Colts', 'Jacksonville Jaguars', 'Houston Texans',
        'Oakland Raiders', 'Denver Broncos', 'Kansas City Chiefs', 'San Diego Chargers', 'Los Angeles Chargers'], 
        ['Philadelphia Eagles', 'Washington Redskins', 'New York Giants', 'Dallas Cowboys',
        'Chicago Bears', 'Green Bay Packers', 'Minnesota Vikings', 'Detroit Lions',
        'Tampa Bay Buccaneers', 'Atlanta Falcons', 'New Orleans Saints', 'Carolina Panthers', 
        'St. Louis Rams', 'Los Angeles Rams', 'San Francisco 49ers', 'Seattle Seahawks', 'Arizona Cardinals']]
    for Conference in Conferences:
        if (team1 in Conference) and (team2 in Conference):
            return True
    return False


df = pd.read_csv(x)
#NOTE: PER GAME CATEGORIES E.G. PointsScoredPerGame ARE CALCULATED ONLY FROM REGULAR SEASON. 
#Src = https://www.pro-football-reference.com/
sitecode = {'BUF':'buf', 'NE':'nwe', 'MIA': 'mia', 'NYJ':'nyj', 'TEN':'oti', 'IND':'clt', 'HOU':'htx', 'JAX':'jax', 'CIN':'cin',
            'PIT':'pit', 'CLE':'cle', 'BAL':'rav', 'KC':'kan', 'OAK':'rai', 'LAC':'sdg', 'SD':'sdg', 'DEN':'den', 'DAL':'dal',
            'PHI':'phi', 'WAS':'was', 'NYG':'nyg', 'TB':'tam', 'NO':'nor', 'ATL':'atl', 'CAR':'car', 'GB':'gnb', 'MIN':'min', 
            'CHI':'chi', 'DET':'det', 'LAR':'ram', 'STL':'ram', 'ARI':'crd', 'SF':'sfo', 'SEA':'sea'}

df = df.astype('str')




#STL -> LAR; SD -> LAC
for i in range(len(df)):
    
    if ',' not in df.loc[i]['CoachFirst']:
       continue


    else:
        site1 = 'https://www.pro-football-reference.com/teams/%s/%s.htm' %(sitecode[df.loc[i]['team']], df.loc[i]['year'])
        tables = pd.read_html(site1)
        weekByWeek = tables[1]
        weekByWeek.columns = weekByWeek.columns.droplevel(0)
        weekByWeek.columns = ['Week', 'Day', 'Date', 'Unnamed: 3_level_1', 'Unnamed: 4_level_1',
       'Unnamed: 5_level_1', 'OT', 'Rec', 'Home', 'OppName', 'Tm',
       'Opp', '1stD', 'TotYd', 'PassY', 'RushY', 'TO', '1stD', 'TotYd',
       'PassY', 'RushY', 'TO', 'Offense', 'Defense', 'Sp. Tms']
        site2 = 'https://www.pro-football-reference.com/years/%s/attendance.htm' % df.loc[i]['year']
        attendance = pd.read_html(site2)
        attendance = attendance[0]
        index = attendance.index[attendance['Tm'] == teamNames[df.loc[i]['team']]].tolist()[0]

        weeks = str(df.at[i, 'CoachLast'])
        weeks1 = re.search('.*\(Weeks:(.*)\) ?,.*', weeks)
        weeks1 = weeks1.group(1)
        weeks2 = re.search('.*\(Weeks:.*\) ?,.*\(Weeks:(.*)\).*', weeks)
        weeks2 = weeks2.group(1)
        weeks1 = weeks1.split(',')
        weeks2 = weeks2.split(',')
        dates1 = []
        dates2 = []
        for item in weeks1:
            dates = item.split('-')
            start = int(dates[0])
            try:    
                end = int(dates[1])
            except IndexError:
                end = start
            dates1 = dates1+ list(range(start, end+1))
        for item in weeks2:
            dates = item.split('-')
            start = int(dates[0])
            try:    
                end = int(dates[1])
            except IndexError:
                end = start
            dates2 = dates2+ list(range(start, end+1))
        

        homeweeks = []
        for j in range(17):
            if pd.isna(weekByWeek.loc[j]['Home']) and weekByWeek.loc[j]['OppName'] != 'Bye Week':
                homeweeks.append(int(weekByWeek.loc[j]['Week']))
        
        total = [0,0]
        games = [0,0]
        avg = ['None', 'None']


        for j in homeweeks:
            weekX = 'Week ' + str(j)
            number = attendance.loc[index][weekX]
            if j in dates1:
                total[0] += int(number)
                games[0] += 1 
            elif j in dates2:
                total[1] += int(number)
                games[1] += 1 
        
        if games[0] != 0:
            avg[0] = total[0] / games[0]
        if games[1] != 0:
            avg[1] = total[1] / games[1]


        df.at[i, 'AverageHomeAttendance'] = str(avg[0]) + ', ' + str(avg[1])
        
    print(df.loc[i]['team'], df.loc[i]['year'])
        
    


df.to_csv('C:/Users/klick/OneDrive/Documents/NflDataStuff/NFLdatasheet17.csv')
        
# Green (Weeks:1-16),Tice (Weeks:17)
# .*\(Weeks: ?(.+?)\).*
    

   
    #         df.at[i, 'PointsScoredPG'] = weekByWeek.loc[0]['PF'] / 16
    #         df.at[i, 'PointsAllowedPG'] = weekByWeek.loc[1]['PF'] / 16
    #         df.at[i, 'YardsGainedPG'] = weekByWeek.loc[0]['Yds-T'] / 16
    #         df.at[i, 'YardsAllowedPG'] = weekByWeek.loc[1]['Yds-T'] / 16
    #         df.at[i, 'TurnoversTotal'] = weekByWeek.loc[0]['TO-T']
    #         df.at[i, 'TurnoversCausedTotal'] = weekByWeek.loc[1]['TO-T']
    #         print(df.loc[i]['team'], df.loc[i]['year'])



# if str(weekByWeek.loc[j-1]['OppName']) != 'Bye Week':
            #         if weekByWeek.loc[j-1]['Result'] == 'W':
            #             wins[1] += 1
            #             if shareConference(df.loc[i]['team'], weekByWeek.loc[j-1]['OppName'], df.loc[i]['year']):
            #                 confwins[1] += 1
            #                 if shareDivision(df.loc[i]['team'], weekByWeek.loc[j-1]['OppName'], df.loc[i]['year']):
            #                     divwins[1] += 1
            #         elif weekByWeek.loc[j-1]['Result'] == 'L':
            #             losses[1] += 1
            #             if shareConference(df.loc[i]['team'], weekByWeek.loc[j-1]['OppName'], df.loc[i]['year']):
            #                 conflosses[1] += 1
            #                 if shareDivision(df.loc[i]['team'], weekByWeek.loc[j-1]['OppName'], df.loc[i]['year']):
            #                     divlosses[1] += 1
            #         elif weekByWeek.loc[j-1]['Result'] == 'T':
            #             ties[1] += 1
            #             if shareConference(df.loc[i]['team'], weekByWeek.loc[j-1]['OppName'], df.loc[i]['year']):
            #                 confties[1] += 1
            #                 if shareDivision(df.loc[i]['team'], weekByWeek.loc[j-1]['OppName'], df.loc[i]['year']):
            #                     divties[1] += 1






        
        # for j in range(17):
        #     try:
        #         if weekByWeek.loc[j]['Result'] == 'W':
        #             wins += 1
        #             if shareConference(df.loc[i]['team'], weekByWeek.loc[j]['OppName'], df.loc[i]['year']):
        #                 confwins += 1
        #                 if shareDivision(df.loc[i]['team'], weekByWeek.loc[j]['OppName'], df.loc[i]['year']):
        #                     divwins += 1
        #         elif weekByWeek.loc[j]['Result'] == 'L':
        #             losses += 1
        #             if shareConference(df.loc[i]['team'], weekByWeek.loc[j]['OppName'], df.loc[i]['year']):
        #                 conflosses += 1
        #                 if shareDivision(df.loc[i]['team'], weekByWeek.loc[j]['OppName'], df.loc[i]['year']):
        #                     divlosses += 1
        #         elif weekByWeek.loc[j]['Result'] == 'T':
        #             ties += 1
        #             if shareConference(df.loc[i]['team'], weekByWeek.loc[j]['OppName'], df.loc[i]['year']):
        #                 confties += 1
        #                 if shareDivision(df.loc[i]['team'], weekByWeek.loc[j]['OppName'], df.loc[i]['year']):
        #                     divties += 1
        #     except KeyError:
        #         break
        

    # site = requests.get(site)
    # record = re.search(htmlPattern, site.text)
    # record = record.group(1)
    # print(df.loc[i]['team'], df.loc[i]['year'])
    # print(record)
    # print()

    # df.at[i, 'DivisionRank'] = record
 

    
            


