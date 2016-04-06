import csv


def save(dict):
    writer = csv.writer(open('/Users/vitalik/Desktop/ClilkBan/resources/bad-good.csv', 'wb'))
    for key, value in dict.items():
        writer.writerow([key.encode('utf-8'), value.encode('utf-8')])