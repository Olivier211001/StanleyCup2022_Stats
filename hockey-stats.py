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

workbook = xlsxwriter.Workbook('stats.xlsx')
worksheet = workbook.add_worksheet("Stanley_Cup_Series")

worksheet.write("A1", "Order")
worksheet.write("B1", "Player")
worksheet.write("C1", "Team")
worksheet.write("D1", "Pos")
worksheet.write("E1", "G")
worksheet.write("F1", "A")
worksheet.write("G1", "Pts")


for rows in soup.find_all("tr"):                    
    player = rows.find('a', {'class': "AnchorLink"})
    team = rows.find('span', {'class': "pl2 n10 athleteCell__teamAbbrev"})
    position = rows.find('td', {'class': "Table__TD"})

    if player is not None and player.get_text() != 'G':
        worksheet.write(i, 0, position.get_text())
        worksheet.write(i, 1, player.get_text())
        worksheet.write(i, 2, team.get_text())

    i = i +1
i = 0


table = soup.find('table', {'class': "Table Table--align-right"})
for rows in table.find_all('tr'): 
    pos = rows.find('td')   
    datas = rows.find_all("td")[2:]
    stats.append(datas)
    if pos is not None:
        worksheet.write(i, 3, pos.get_text())    
    i = i + 1

i = 1

for data in stats:
    if i < 51:
        worksheet.write(i, 4, stats[i][0].get_text())
        worksheet.write(i, 5, stats[i][1].get_text())
        worksheet.write(i, 6, stats[i][2].get_text())
    i = i + 1

workbook.close()   
  

            
            
        
            
            

    
   