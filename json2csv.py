import json
import csv

with open('./input_data/cl_news.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

data_rows = data[0]['data']

data_file = open('cl_news.csv', 'w', encoding='utf-8')

csv_writer = csv.writer(data_file)

count = 0

for d in data_rows:
    if count == 0:

        # Writing headers of CSV file
        header = d.keys()
        csv_writer.writerow(header)
        count += 1

    # Writing data of CSV file
    csv_writer.writerow(d.values())

data_file.close()