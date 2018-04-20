#!/usr/bin/env python

from bs4 import BeautifulSoup

html_file = '../data/boi_movies/movie_1.html'

with open(html_file) as fp:
    soup = BeautifulSoup(fp, 'lxml')

box = soup.find_all('td', class_='opt1')
left_box = box[0]
right_box = box[1]

first_week = left_box.find_all('tr')[0]
first_week = first_week.find_all('td')[-1]
first_week = first_week.find_all('span')

print(first_week[0].next_sibling)
