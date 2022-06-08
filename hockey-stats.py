import xlsxwriter
import json
from urllib.request import urlopen

# This code is scraping data on ESPN 
# You get nhl stanley cup series players stats (from the best to the worst)

colPos = 0
colPlayer = 1
colTeam= 2
colPosition = 3
colGoals= 4
colAssists = 5
colPts = 6

workbook = xlsxwriter.Workbook('stats.xlsx')
worksheet = workbook.add_worksheet("Stanley_Cup_Series")

def write_in_excel_file(row, col, content):
        worksheet.write(row, col, content)

def writeHeader():
    worksheet.write("A1", "Order")
    worksheet.write("B1", "Player")
    worksheet.write("C1", "Team")
    worksheet.write("D1", "Pos")
    worksheet.write("E1", "G")
    worksheet.write("F1", "A")
    worksheet.write("G1", "Pts")

def getStatsInfo():
    response = urlopen("https://site.web.api.espn.com/apis/common/v3/sports/hockey/nhl/statistics/byathlete?region=us&lang=en&contentorigin=espn&isqualified=false&limit=335&sort=offensive%3Apoints%3Adesc&category=skaters").read().decode('utf-8')  
    responseJson = json.loads(response)
    return responseJson

def buildExcelFileWithStats():
    i = 1
    j = 0
    while(j != 335):
        player = arrayOfStats["athletes"][j]["athlete"]["displayName"]
        team = arrayOfStats["athletes"][j]["athlete"]["teamShortName"]
        goals = arrayOfStats["athletes"][j]["categories"][1]["totals"][0]
        assists = arrayOfStats["athletes"][j]["categories"][1]["totals"][1]
        pts = arrayOfStats["athletes"][j]["categories"][1]["totals"][2]
        position = arrayOfStats["athletes"][j]["athlete"]["position"]["abbreviation"]
        write_in_excel_file(i, colPlayer, player)
        write_in_excel_file(i, colPos, i)
        write_in_excel_file(i, colTeam, team)
        write_in_excel_file(i, colPosition, position)
        write_in_excel_file(i, colGoals, goals)
        write_in_excel_file(i, colAssists, assists)
        write_in_excel_file(i, colPts, pts)
        i = i + 1
        j = j + 1

arrayOfStats = getStatsInfo()

writeHeader()

buildExcelFileWithStats()

workbook.close()




  

            
            
        
            
            

    
   