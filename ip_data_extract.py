"""
This script extracts table from html files. Assumes there is only one table (Which was the case for me).
The purpose of the script in my project is to extract login IP data provided by google, which is in .html format.

The raw data will not be shared, but this script should work for ANY .html file with only one table in it.
"""
from bs4 import BeautifulSoup
import csv

def html_to_csv(html_file, csv_file):
    with open(html_file, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'lxml')
    table = soup.find('table') 
    rows = table.find_all('tr')
    data = []

    for row in rows:
        cells = row.find_all(['th', 'td'])
        row_data = [cell.get_text(strip=True) for cell in cells]
        data.append(row_data)
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(data)
    print(f"CSV file '{csv_file}' created successfully.")

html_file_path = input("Path to HTML file: ") #Prompts the user for the path of the .html file. I have put this on purpose for reproducability.
csv_file_path = html_file_path.split(sep="/")[-1].replace(".html","")+"_iptable.csv" #The last string could be modified for other usecases
html_to_csv(html_file_path, csv_file_path)
