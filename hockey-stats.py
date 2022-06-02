from bs4 import BeautifulSoup
import requests 
import xlsxwriter

# This code is scraping data on ESPN 
# You get nhl stanley cup series players stats (from the best to the worst)

url = "https://www.espn.com/nhl/stats/player"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

stats = []
i = 0
colPos = 0
colPlayer = 1
colTeam= 2
colPosition = 3
colGoals= 4
colAssists = 5
colPts = 6


workbook = xlsxwriter.Workbook('stats.xlsx')
worksheet = workbook.add_worksheet("Stanley_Cup_Series")

#############################################

def write_in_excel_file(row, col, content):
        worksheet.write(row, col, content)

def write_header():
    worksheet.write("A1", "Order")
    worksheet.write("B1", "Player")
    worksheet.write("C1", "Team")
    worksheet.write("D1", "Pos")
    worksheet.write("E1", "G")
    worksheet.write("F1", "A")
    worksheet.write("G1", "Pts")

def scrape_pos_player_team():
    i = 0
    for rows in soup.find_all("tr"):                    
        player = rows.find('a', {'class': "AnchorLink"})
        team = rows.find('span', {'class': "pl2 n10 athleteCell__teamAbbrev"})
        position = rows.find('td', {'class': "Table__TD"})

        if player is not None and player.get_text() != 'G':
            write_in_excel_file(i, colPos, position.get_text())
            write_in_excel_file(i, colPlayer, player.get_text())
            write_in_excel_file(i, colTeam, team.get_text())

        i = i + 1

def scrape_position_andBuildStats():
    i = 0
    table = soup.find('table', {'class': "Table Table--align-right"})
    for rows in table.find_all('tr'): 
        pos = rows.find('td')   
        datas = rows.find_all("td")[2:]
        stats.append(datas)
        if pos is not None:
            write_in_excel_file(i, colPosition, pos.get_text())    
        i = i + 1

def write_Stats_in_excel():
    i = 1
    for data in stats:
        if i < 51:
            write_in_excel_file(i, colGoals, stats[i][0].get_text())
            write_in_excel_file(i, colAssists, stats[i][1].get_text())
            write_in_excel_file(i, colPts, stats[i][2].get_text())
        i = i + 1


################################################


write_header()

scrape_pos_player_team()

scrape_position_andBuildStats()

write_Stats_in_excel()

workbook.close()




  

            
            
        
            
            

    
   