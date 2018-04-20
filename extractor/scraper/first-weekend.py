from bs4 import BeautifulSoup
import csv

with open('../data/boi/india-first-weekend_2000.html') as f:
    soup = BeautifulSoup(f)

table = soup.select_one("table.bluelink")
# rows = table[0].find_all('tr')

# headers = [th.text.encode("utf-8") for th in table.select("tr th")]

with open("data/out.csv", "w") as f:
    wr = csv.writer(f)
    # wr.writerow(headers)
    wr.writerows([[td.text.encode("utf-8") for td in row.find_all("td")] for row in table.select("tr")])
