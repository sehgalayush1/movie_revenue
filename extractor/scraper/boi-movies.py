#!/usr/bin/env python

import os
import re
import csv
from bs4 import BeautifulSoup

html_files = []
path = '../data/boi_movies/'

# def find_by_label(soup, label):
#     return soup.find("div", text=re.compile(label)).next_sibling

def value_or_none(item):
    if item:
        return item[0].next_sibling
    else:
        return 'None'

for file in os.listdir("../data/boi_movies"):
    if file.endswith(".html"):
        html_files.append(file)

final_data = [['movie_name', 'release_date', 'runtime', 'genre', 'hitfactor', 'screens', 'footfall', 'budget', 'first_day', 'first_weekend', 'first_week',
               'worldwide_first_weekend', 'worldwide_first_week', 'india_gross', 'worldwide_gross']]

counter = 0

for file in html_files:
    try:
        file_path = path + file
        with open(file_path) as fp:
            soup = BeautifulSoup(fp, "lxml")
        # Movie Title
        title = soup.find_all("div", class_="blue_tlte")
        title = title[0].find_all("a")
        movie_name = title[0].text
        
        # Release Date, Runtime and Genre
        release_date = soup.find_all("div", class_="movieboxsright")
        release_date = release_date[0].find_all("div", class_="movieboxssec")
        runtime = release_date[0].find_all("a")
        genre = runtime[-1].text
        runtime = runtime[0].next_sibling
        release_date = release_date[0].find_all("span", class_="redtext")
        release_date = release_date[0].text
        
        # Hitfactor
        hitfactor = soup.find('div', class_="mobileredverdictext").text

        # Screens, First Day, First Weekend and Total Gross
        main_div = soup.find('div', {"id": "adafter1"})
        # total_gross_div = main_div.find_all('div')[-1]
        # total_gross = total_gross_div.find_all('span')
        # total_gross = total_gross[0].next_sibling

        other_div = main_div.find_all('div')[0]
        screen_div = other_div.find_all('div')[0]
        screen_div_table = screen_div.find('table')
        screens = screen_div_table.find_all('tr')[0]
        screens = screens.find_all('td')[-1].text

        first_day = screen_div_table.find_all('tr')[-1]
        first_day = first_day.find_all('td')[-1]
        first_day = first_day.find_all('span')
        first_day = value_or_none(first_day)

        first_weekend_div = other_div.find_all('div')[-1]
        first_weekend_div_table = first_weekend_div.find('table')
        first_weekend = first_weekend_div_table.find_all('tr')[1]
        first_weekend = first_weekend.find_all('td')[-1]
        first_weekend = first_weekend.find_all('span')
        first_weekend = value_or_none(first_weekend)
        
        # Budget, First week and Footfalls
        box = soup.find_all('td', class_='opt1')
        left_box = box[0]
        right_box = box[1]

        first_week = left_box.find_all('tr')[0]
        first_week = first_week.find_all('td')[-1]
        first_week = first_week.find_all('span')
        first_week = value_or_none(first_week)
        
        budget = left_box.find_all('tr')[1]
        budget = budget.find_all('td')[-1]
        budget = budget.find_all('span')
        budget = value_or_none(budget)
        
        india_gross = left_box.find_all('tr')[2]
        india_gross = india_gross.find_all('td')[-1]
        india_gross = india_gross.find_all('span')
        india_gross = value_or_none(india_gross)
        
        worldwide_gross = left_box.find_all('tr')[4]
        worldwide_gross = worldwide_gross.find_all('td')[-1]
        worldwide_gross = worldwide_gross.find_all('span')
        worldwide_gross = value_or_none(worldwide_gross)

        footfall = right_box.find_all('tr')[1]
        footfall = footfall.find_all('td')[-1].text
        
        box2 = soup.find('div', {'id': 'adafter2'})
        box2_table = box2.find('table', class_='hide_in_mobile')
        data_row = box2_table.find_all('tr')[-1]
        
        worldwide_first_weekend = data_row.find_all('td')[1].text
        worldwide_first_week = data_row.find_all('td')[3].text
        if worldwide_first_weekend == '--':
            worldwide_first_weekend = 'None'
        elif worldwide_first_week == '--':
            worldwide_first_week = 'None'

        data_list = [movie_name, release_date, runtime, genre, hitfactor, screens, footfall, budget, first_day, first_weekend, first_week, worldwide_first_weekend, worldwide_first_week, india_gross, worldwide_gross]
        final_data.append(data_list)
    except:
        print('Error occured in file' + file)
    
    counter += 1
    print("Scraping movie %s" % counter)


# Save csv
with open('data/movie_data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(final_data)

print("CSV Saved!")