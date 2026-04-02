from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Webdriver
browser = webdriver.Chrome("D:/setup/chromedriver_win32/chromedrive.exe")
browser.get(START_URL)

time.sleep(10)


scarped_data = []

def scrape():
    soup = BeautifulSoup(browser.page_source, "html.parser")

    bright_star_table = soup.find("table", attrs={"class", "wikitable"})
    table_body = bright_star_table.find('tbody')
    table_rows = table_body.find_all('tr')

    for row in table_rows:
        table_col = row.find_all('td')
        print(table_col)
        temp_list = []

        for col_data in table_col:
            data = col_data.text.strip()
            print(data)

            temp_list.append(data)
        scarped_data.append(temp_list)

scrape()

######################################################################

stars_data = []

for i in range(0,len(scarped_data)):

    Star_names = scarped_data[i][1]
    Distance = scarped_data[i][3]
    Mass = scarped_data[i][5]
    Radius = scarped_data[i][6]
    Lum = scarped_data[i][7]

    require_data = [Star_names, Distance, Mass, Radius, Lum]
    stars_data.append(require_data)

print(stars_data)

header = ['Star_names', 'Distance', 'Mass', 'Radius', 'Lumiosity']

star_df_1 = pd.DataFrame(stars_data, columns=header)

star_df_1.to_csv('scraped_data.csv',index=True, index_label="id")